#!/usr/bin/env node
/**
 * Serveur MCP — administration de serveurs distants via SSH.
 *
 * Expose à Claude des outils pour se connecter à des serveurs (auth par CLÉ ou par
 * MOT DE PASSE), installer des paquets, lancer des tests et vérifier l'état — le tout
 * encadré par des GARDE-FOUS configurables (allowlist d'hôtes, commandes destructrices
 * bloquées, mode lecture seule, confirmation pour la prod, dry-run, journal d'audit).
 *
 * Les secrets ne sont JAMAIS écrits dans le dépôt : le fichier hosts.json (gitignoré)
 * référence les mots de passe par variable d'environnement (`passwordEnv`) et les clés
 * par chemin de fichier (`privateKeyPath`).
 */

import { readFileSync, appendFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, resolve, isAbsolute } from "node:path";
import { fileURLToPath } from "node:url";
import { Client } from "ssh2";
import { z } from "zod";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const __dirname = dirname(fileURLToPath(import.meta.url));

// ---------------------------------------------------------------------------
// Chargement des secrets depuis .env (sans dépendance externe)
// ---------------------------------------------------------------------------
// L'app Desktop ne source pas .env : on le charge nous-mêmes pour peupler
// process.env (SSH_PASS_*). Les valeurs déjà présentes dans l'environnement
// ont priorité ; on n'écrase rien. Chemin surchargeable via SSH_MCP_ENV.
function loadDotEnv(envPath) {
  if (!existsSync(envPath)) return;
  for (const raw of readFileSync(envPath, "utf8").split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith("#")) continue;
    const eq = line.indexOf("=");
    if (eq === -1) continue;
    const key = line.slice(0, eq).trim();
    if (!key || key in process.env) continue;
    let val = line.slice(eq + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    process.env[key] = val;
  }
}
loadDotEnv(
  resolve(process.env.SSH_MCP_ENV || resolve(__dirname, "..", "..", ".env"))
);

// ---------------------------------------------------------------------------
// Chargement de la configuration
// ---------------------------------------------------------------------------

const CONFIG_PATH = resolve(
  process.env.SSH_MCP_CONFIG || resolve(__dirname, "hosts.json")
);
const AUDIT_LOG = resolve(
  process.env.SSH_MCP_AUDIT_LOG || resolve(__dirname, "ssh-mcp-audit.log")
);

/** Garde-fous par défaut, surchargés par la section `guardrails` du hosts.json. */
const DEFAULT_GUARDRAILS = {
  // Motifs (regex) refusés partout, même après confirmation. Fail-closed.
  blockedPatterns: [
    "rm\\s+-[a-zA-Z]*r[a-zA-Z]*f[a-zA-Z]*\\s+(/|/\\*|~|\\$HOME)(\\s|$)",
    "rm\\s+-[a-zA-Z]*f[a-zA-Z]*r[a-zA-Z]*\\s+(/|/\\*|~|\\$HOME)(\\s|$)",
    "mkfs(\\.|\\s)",
    "\\bdd\\b.*\\bof=/dev/",
    ">\\s*/dev/sd[a-z]",
    ":\\(\\)\\s*\\{\\s*:\\|:&\\s*\\}\\s*;\\s*:", // fork bomb
    "\\b(shutdown|halt|poweroff)\\b",
    "\\bchmod\\s+-R\\s+777\\s+/(\\s|$)",
    "\\bchown\\s+-R\\b.*\\s/(\\s|$)",
    "\\bmv\\b\\s+/\\s",
    "\\bwipefs\\b",
    "\\bfdisk\\b",
  ],
  // Commande considérée « sensible » => exige confirm=true (hors prod aussi).
  sensitivePatterns: [
    "\\b(apt|apt-get|dnf|yum|apk|pacman)\\b.*\\b(install|remove|purge|upgrade|dist-upgrade)\\b",
    "\\bpip3?\\b.*\\b(install|uninstall)\\b",
    "\\bnpm\\b.*\\b(install|uninstall|ci)\\b",
    "\\bsystemctl\\b.*\\b(start|stop|restart|reload|disable|mask)\\b",
    "\\b(reboot|init\\s+[06])\\b",
    "\\bufw\\b|\\biptables\\b|\\bnft\\b|\\bfirewall-cmd\\b",
    "\\b(DROP|TRUNCATE|DELETE)\\b",
    "\\brm\\b",
    "\\bgit\\b.*\\b(reset\\s+--hard|clean\\s+-[a-z]*f|push\\s+--force)",
  ],
  // Toujours exiger confirm=true quand l'hôte est en environnement "prod".
  requireConfirmForProd: true,
  // Délai max d'exécution d'une commande (ms).
  commandTimeoutMs: 120000,
};

/**
 * Préfixes de commandes considérés strictement en lecture (mode readOnly).
 * Fail-closed : tout ce qui n'est pas listé est refusé quand readOnly est actif.
 */
const READ_ONLY_ALLOWED = [
  "ls", "cat", "echo", "pwd", "whoami", "id", "date", "uptime", "hostname",
  "hostnamectl", "uname", "df", "free", "top", "ps", "ss", "netstat", "ip",
  "grep", "egrep", "find", "head", "tail", "wc", "stat", "du", "env", "which",
  "lsb_release", "nproc", "journalctl", "dmesg", "docker", "kubectl", "systemctl",
  "getent", "mount", "lsblk", "vmstat", "iostat", "sensors", "true",
];
// Sous-commandes autorisées pour des binaires à double usage (lecture seule).
const READ_ONLY_SUBCOMMANDS = {
  docker: ["ps", "images", "logs", "inspect", "stats", "version", "info", "top"],
  kubectl: ["get", "describe", "logs", "top", "version", "cluster-info", "explain"],
  systemctl: ["status", "is-active", "is-enabled", "list-units", "list-unit-files", "show"],
};

function loadConfig() {
  if (!existsSync(CONFIG_PATH)) {
    throw new Error(
      `Fichier de configuration introuvable : ${CONFIG_PATH}\n` +
        `Copie hosts.example.json vers hosts.json et renseigne tes serveurs, ` +
        `ou définis SSH_MCP_CONFIG.`
    );
  }
  let raw;
  try {
    raw = JSON.parse(readFileSync(CONFIG_PATH, "utf8"));
  } catch (e) {
    throw new Error(`hosts.json illisible (JSON invalide) : ${e.message}`);
  }
  const hosts = raw.hosts || {};
  const userGr = raw.guardrails || {};
  // Les listes de motifs sont ADDITIVES : la config ne peut qu'ajouter des garde-fous,
  // jamais désactiver ceux par défaut (les commandes destructrices restent bloquées).
  const guardrails = {
    ...DEFAULT_GUARDRAILS,
    ...userGr,
    blockedPatterns: [
      ...DEFAULT_GUARDRAILS.blockedPatterns,
      ...(userGr.blockedPatterns || []),
    ],
    sensitivePatterns: [
      ...DEFAULT_GUARDRAILS.sensitivePatterns,
      ...(userGr.sensitivePatterns || []),
    ],
  };
  return { hosts, guardrails };
}

// ---------------------------------------------------------------------------
// Utilitaires
// ---------------------------------------------------------------------------

function expandHome(p) {
  if (!p) return p;
  if (p === "~") return homedir();
  if (p.startsWith("~/")) return resolve(homedir(), p.slice(2));
  return isAbsolute(p) ? p : resolve(p);
}

function audit(entry) {
  const line = JSON.stringify({ ts: new Date().toISOString(), ...entry });
  try {
    appendFileSync(AUDIT_LOG, line + "\n");
  } catch {
    /* le journal d'audit ne doit jamais bloquer une opération */
  }
}

function firstToken(cmd) {
  // Ignore les affectations d'env en tête (FOO=bar cmd ...) et sudo.
  const tokens = cmd.trim().split(/\s+/);
  let i = 0;
  while (i < tokens.length && /^[A-Za-z_][A-Za-z0-9_]*=/.test(tokens[i])) i++;
  if (tokens[i] === "sudo") i++;
  return { cmd: tokens[i] || "", next: tokens[i + 1] || "" };
}

function isReadOnlyCommand(command) {
  // Refuse tout enchaînement / redirection en écriture par prudence.
  if (/[;&|]|`|\$\(|>>?/.test(command)) {
    // On tolère les pipes vers des filtres lecture (grep/head/…) mais fail-closed
    // sur les redirections en écriture (> >>) et le chaînage ; && ||.
    if (/>>?\s*\S/.test(command) || /;|&&|\|\|/.test(command)) return false;
  }
  const { cmd, next } = firstToken(command);
  if (!READ_ONLY_ALLOWED.includes(cmd)) return false;
  const subs = READ_ONLY_SUBCOMMANDS[cmd];
  if (subs && next && !subs.includes(next)) return false;
  return true;
}

function matchesAny(patterns, command) {
  return patterns.some((p) => {
    try {
      return new RegExp(p, "i").test(command);
    } catch {
      return false;
    }
  });
}

/** Vérifie un hôte + une commande contre les garde-fous. Renvoie {ok, reason?, needsConfirm?}. */
function evaluateGuardrails(hostAlias, hosts, guardrails, command, { confirm, dryRun }) {
  const host = hosts[hostAlias];
  if (!host) {
    return {
      ok: false,
      reason: `Hôte « ${hostAlias} » inconnu. Hôtes autorisés : ${Object.keys(hosts).join(", ") || "(aucun)"}.`,
    };
  }
  // 1) Commandes destructrices : refus absolu.
  if (matchesAny(guardrails.blockedPatterns, command)) {
    return {
      ok: false,
      reason: `Commande bloquée par un garde-fou (motif destructeur). Refusée même avec confirmation.`,
    };
  }
  // 2) Mode lecture seule de l'hôte.
  if (host.readOnly && !isReadOnlyCommand(command)) {
    return {
      ok: false,
      reason: `L'hôte « ${hostAlias} » est en mode LECTURE SEULE : seules les commandes de consultation sont permises. Commande refusée.`,
    };
  }
  // 3) Confirmation requise (prod ou commande sensible).
  const isProd = (host.environment || "").toLowerCase() === "prod";
  const sensitive = matchesAny(guardrails.sensitivePatterns, command);
  const mustConfirm =
    (isProd && guardrails.requireConfirmForProd) || sensitive;
  if (mustConfirm && !confirm && !dryRun) {
    return {
      ok: false,
      needsConfirm: true,
      reason:
        `⚠️ Confirmation requise avant exécution sur « ${hostAlias} »` +
        `${isProd ? " (environnement PROD)" : ""}${sensitive ? " (commande sensible)" : ""}.\n` +
        `Cible : ${host.user}@${host.host}:${host.port || 22} — env=${host.environment || "?"}\n` +
        `Commande : ${command}\n` +
        `Relance le même appel avec confirm:true si tu veux l'exécuter, ` +
        `ou dryRun:true pour un test à blanc.`,
    };
  }
  return { ok: true, host, isProd, sensitive };
}

// ---------------------------------------------------------------------------
// Exécution SSH
// ---------------------------------------------------------------------------

function resolveAuth(host) {
  const auth = host.auth || {};
  const base = {
    host: host.host,
    port: host.port || 22,
    username: host.user,
    readyTimeout: 15000,
  };
  if (auth.type === "password") {
    const pw = auth.passwordEnv ? process.env[auth.passwordEnv] : auth.password;
    if (!pw) {
      throw new Error(
        `Mot de passe absent pour cet hôte : définis la variable d'environnement ` +
          `« ${auth.passwordEnv || "(non spécifiée)"} ».`
      );
    }
    return { ...base, password: pw };
  }
  // Par défaut : authentification par clé.
  const keyPath = expandHome(auth.privateKeyPath);
  if (!keyPath || !existsSync(keyPath)) {
    throw new Error(
      `Clé privée introuvable : « ${auth.privateKeyPath || "(non spécifiée)"} ». ` +
        `Utilise auth.type="password" ou corrige privateKeyPath.`
    );
  }
  const cfg = { ...base, privateKey: readFileSync(keyPath) };
  const passphrase = auth.passphraseEnv
    ? process.env[auth.passphraseEnv]
    : auth.passphrase;
  if (passphrase) cfg.passphrase = passphrase;
  return cfg;
}

function runSSH(host, command, timeoutMs) {
  return new Promise((resolvePromise) => {
    let connCfg;
    try {
      connCfg = resolveAuth(host);
    } catch (e) {
      return resolvePromise({ ok: false, error: e.message });
    }
    const conn = new Client();
    let settled = false;
    let stdout = "";
    let stderr = "";
    const timer = setTimeout(() => {
      if (settled) return;
      settled = true;
      conn.end();
      resolvePromise({
        ok: false,
        error: `Délai dépassé (${timeoutMs} ms) — commande interrompue.`,
        stdout,
        stderr,
      });
    }, timeoutMs);

    conn
      .on("ready", () => {
        conn.exec(command, (err, stream) => {
          if (err) {
            if (!settled) {
              settled = true;
              clearTimeout(timer);
              conn.end();
              resolvePromise({ ok: false, error: err.message });
            }
            return;
          }
          stream
            .on("close", (code) => {
              if (settled) return;
              settled = true;
              clearTimeout(timer);
              conn.end();
              resolvePromise({ ok: true, code, stdout, stderr });
            })
            .on("data", (d) => (stdout += d.toString()))
            .stderr.on("data", (d) => (stderr += d.toString()));
        });
      })
      .on("error", (err) => {
        if (settled) return;
        settled = true;
        clearTimeout(timer);
        resolvePromise({ ok: false, error: `Connexion échouée : ${err.message}` });
      })
      .connect(connCfg);
  });
}

function truncate(s, max = 15000) {
  if (!s) return "";
  return s.length > max ? s.slice(0, max) + `\n…[tronqué, ${s.length} octets]` : s;
}

function formatResult(hostAlias, host, command, res) {
  if (!res.ok) {
    return `❌ Échec sur « ${hostAlias} » (${host.host})\nCommande : ${command}\nErreur : ${res.error}` +
      (res.stdout ? `\n--- stdout ---\n${truncate(res.stdout)}` : "") +
      (res.stderr ? `\n--- stderr ---\n${truncate(res.stderr)}` : "");
  }
  const status = res.code === 0 ? "✅" : `⚠️ (exit ${res.code})`;
  return `${status} « ${hostAlias} » (${host.host}) — exit=${res.code}\nCommande : ${command}` +
    `\n--- stdout ---\n${truncate(res.stdout) || "(vide)"}` +
    (res.stderr ? `\n--- stderr ---\n${truncate(res.stderr)}` : "");
}

function textResult(text) {
  return { content: [{ type: "text", text }] };
}

// ---------------------------------------------------------------------------
// Serveur MCP + outils
// ---------------------------------------------------------------------------

function buildServer(state) {
  const server = new McpServer({ name: "ssh-admin", version: "0.1.0" });

  // -- ssh_list_hosts : liste les hôtes configurés (sans aucun secret) --------
  server.tool(
    "ssh_list_hosts",
    "Liste les serveurs configurés (alias, hôte, utilisateur, environnement, type d'auth, mode lecture seule). N'expose aucun secret.",
    {},
    async () => {
      const { hosts } = state;
      const rows = Object.entries(hosts).map(([alias, h]) => ({
        alias,
        host: h.host,
        user: h.user,
        port: h.port || 22,
        environment: h.environment || "?",
        auth: h.auth?.type || "key",
        readOnly: !!h.readOnly,
      }));
      if (rows.length === 0)
        return textResult("Aucun hôte configuré dans hosts.json.");
      return textResult(
        "Hôtes configurés :\n" +
          rows
            .map(
              (r) =>
                `• ${r.alias} → ${r.user}@${r.host}:${r.port} | env=${r.environment} | auth=${r.auth}${r.readOnly ? " | LECTURE SEULE" : ""}`
            )
            .join("\n")
      );
    }
  );

  // -- ssh_check : vérification d'état, strictement en lecture ----------------
  server.tool(
    "ssh_check",
    "Vérifie la connectivité et l'état d'un serveur (lecture seule, sans risque) : identité, ressources, services en échec, ports en écoute.",
    { host: z.string().describe("Alias de l'hôte défini dans hosts.json") },
    async ({ host: alias }) => {
      const { hosts, guardrails } = state;
      const h = hosts[alias];
      if (!h)
        return textResult(
          `Hôte « ${alias} » inconnu. Hôtes : ${Object.keys(hosts).join(", ") || "(aucun)"}.`
        );
      const cmd =
        'echo "== Identité =="; hostname; id; uptime; ' +
        'echo "== Ressources =="; free -h 2>/dev/null; df -h 2>/dev/null | head -n 15; ' +
        'echo "== Services en échec =="; systemctl --failed --no-pager 2>/dev/null | head -n 20; ' +
        'echo "== Ports en écoute =="; ss -tulpn 2>/dev/null | head -n 25';
      audit({ tool: "ssh_check", host: alias });
      const res = await runSSH(h, cmd, guardrails.commandTimeoutMs);
      return textResult(formatResult(alias, h, "(bilan de santé)", res));
    }
  );

  // -- ssh_run : commande arbitraire, sous garde-fous -------------------------
  server.tool(
    "ssh_run",
    "Exécute une commande shell sur un serveur, sous garde-fous (commandes destructrices bloquées, mode lecture seule respecté, confirmation exigée pour la prod et les commandes sensibles). Utilise dryRun:true pour un test à blanc, confirm:true pour valider une commande sensible.",
    {
      host: z.string().describe("Alias de l'hôte défini dans hosts.json"),
      command: z.string().describe("Commande shell à exécuter sur le serveur distant"),
      confirm: z
        .boolean()
        .optional()
        .describe("Confirmation explicite requise pour la prod / les commandes sensibles"),
      dryRun: z
        .boolean()
        .optional()
        .describe("Si true, n'exécute rien : renvoie la commande qui serait lancée"),
    },
    async ({ host: alias, command, confirm, dryRun }) => {
      const { hosts, guardrails } = state;
      const verdict = evaluateGuardrails(alias, hosts, guardrails, command, {
        confirm,
        dryRun,
      });
      if (!verdict.ok) {
        audit({ tool: "ssh_run", host: alias, command, blocked: true, reason: verdict.reason });
        return textResult(
          (verdict.needsConfirm ? "" : "🚫 ") + verdict.reason
        );
      }
      if (dryRun) {
        return textResult(
          `🧪 DRY-RUN — rien exécuté.\nCible : ${verdict.host.user}@${verdict.host.host} (env=${verdict.host.environment || "?"})\nCommande : ${command}`
        );
      }
      audit({
        tool: "ssh_run",
        host: alias,
        command,
        confirm: !!confirm,
        prod: verdict.isProd,
        sensitive: verdict.sensitive,
      });
      const res = await runSSH(verdict.host, command, guardrails.commandTimeoutMs);
      return textResult(formatResult(alias, verdict.host, command, res));
    }
  );

  // -- ssh_install : installe un paquet via le gestionnaire détecté -----------
  server.tool(
    "ssh_install",
    "Installe un ou plusieurs paquets sur un serveur en détectant le gestionnaire (apt/dnf/yum/apk/pacman). Commande sensible : exige confirm:true (et systématiquement en prod).",
    {
      host: z.string().describe("Alias de l'hôte"),
      packages: z.array(z.string()).min(1).describe("Liste de paquets à installer"),
      confirm: z.boolean().optional().describe("Confirmation d'installation"),
      dryRun: z.boolean().optional(),
    },
    async ({ host: alias, packages, confirm, dryRun }) => {
      const { hosts, guardrails } = state;
      const pkgs = packages.map((p) => p.replace(/[^\w.+-]/g, "")).filter(Boolean);
      if (pkgs.length === 0) return textResult("🚫 Aucun paquet valide fourni.");
      // Détection du gestionnaire puis installation non interactive.
      const install =
        `if command -v apt-get >/dev/null; then sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ${pkgs.join(" ")}; ` +
        `elif command -v dnf >/dev/null; then sudo dnf install -y ${pkgs.join(" ")}; ` +
        `elif command -v yum >/dev/null; then sudo yum install -y ${pkgs.join(" ")}; ` +
        `elif command -v apk >/dev/null; then sudo apk add ${pkgs.join(" ")}; ` +
        `elif command -v pacman >/dev/null; then sudo pacman -S --noconfirm ${pkgs.join(" ")}; ` +
        `else echo "Aucun gestionnaire de paquets reconnu"; exit 1; fi`;
      const verdict = evaluateGuardrails(alias, hosts, guardrails, install, { confirm, dryRun });
      if (!verdict.ok) {
        audit({ tool: "ssh_install", host: alias, packages: pkgs, blocked: true });
        return textResult((verdict.needsConfirm ? "" : "🚫 ") + verdict.reason);
      }
      if (dryRun)
        return textResult(`🧪 DRY-RUN — installerait : ${pkgs.join(", ")} sur « ${alias} ».`);
      audit({ tool: "ssh_install", host: alias, packages: pkgs, confirm: !!confirm });
      const res = await runSSH(verdict.host, install, guardrails.commandTimeoutMs);
      return textResult(formatResult(alias, verdict.host, `install ${pkgs.join(" ")}`, res));
    }
  );

  // -- ssh_run_tests : lance une suite de tests dans un dossier ---------------
  server.tool(
    "ssh_run_tests",
    "Lance une commande de tests dans un répertoire du serveur (ex. 'npm test', 'pytest', 'make test'). Renvoie la sortie complète et le code de sortie.",
    {
      host: z.string().describe("Alias de l'hôte"),
      directory: z.string().describe("Répertoire de travail (chemin absolu de préférence)"),
      testCommand: z.string().describe("Commande de test à exécuter (ex. 'npm test')"),
      confirm: z.boolean().optional(),
      dryRun: z.boolean().optional(),
    },
    async ({ host: alias, directory, testCommand, confirm, dryRun }) => {
      const { hosts, guardrails } = state;
      // cd sécurisé : échoue si le dossier n'existe pas plutôt que de lancer ailleurs.
      const safeDir = directory.replace(/'/g, "'\\''");
      const cmd = `cd '${safeDir}' && ${testCommand}`;
      const verdict = evaluateGuardrails(alias, hosts, guardrails, cmd, { confirm, dryRun });
      if (!verdict.ok) {
        audit({ tool: "ssh_run_tests", host: alias, directory, testCommand, blocked: true });
        return textResult((verdict.needsConfirm ? "" : "🚫 ") + verdict.reason);
      }
      if (dryRun)
        return textResult(`🧪 DRY-RUN — lancerait « ${testCommand} » dans ${directory} sur « ${alias} ».`);
      audit({ tool: "ssh_run_tests", host: alias, directory, testCommand });
      const res = await runSSH(verdict.host, cmd, guardrails.commandTimeoutMs);
      return textResult(formatResult(alias, verdict.host, cmd, res));
    }
  );

  return server;
}

// ---------------------------------------------------------------------------
// Démarrage
// ---------------------------------------------------------------------------

async function main() {
  const config = loadConfig();

  if (process.argv.includes("--check-config")) {
    // Diagnostic hors MCP : valide la config et l'accessibilité des secrets/clés.
    const problems = [];
    for (const [alias, h] of Object.entries(config.hosts)) {
      if (!h.host || !h.user) problems.push(`${alias}: 'host' ou 'user' manquant`);
      const a = h.auth || {};
      if (a.type === "password") {
        if (!a.passwordEnv && !a.password)
          problems.push(`${alias}: auth password sans passwordEnv/password`);
        else if (a.passwordEnv && !process.env[a.passwordEnv])
          problems.push(`${alias}: variable d'env ${a.passwordEnv} non définie`);
      } else {
        const kp = expandHome(a.privateKeyPath);
        if (!kp || !existsSync(kp))
          problems.push(`${alias}: clé privée introuvable (${a.privateKeyPath})`);
      }
    }
    const nb = Object.keys(config.hosts).length;
    if (problems.length) {
      console.error(`Config chargée (${nb} hôte(s)) — problèmes :\n- ${problems.join("\n- ")}`);
      process.exit(1);
    }
    console.error(`✅ Config valide : ${nb} hôte(s), secrets/clés accessibles.`);
    process.exit(0);
  }

  const state = { hosts: config.hosts, guardrails: config.guardrails };
  const server = buildServer(state);
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error(
    `[ssh-admin] MCP prêt — ${Object.keys(config.hosts).length} hôte(s), config=${CONFIG_PATH}`
  );
}

main().catch((e) => {
  console.error(`[ssh-admin] Erreur fatale : ${e.message}`);
  process.exit(1);
});
