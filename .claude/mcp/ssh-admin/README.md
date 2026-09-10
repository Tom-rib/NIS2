# MCP `ssh-admin` — administration de serveurs distants via SSH

Serveur MCP qui donne à Claude (dans VSCode / Claude Code) des **outils SSH cadrés** pour
installer des paquets, lancer des tests et vérifier l'état de tes serveurs — avec
authentification **par clé ou par mot de passe** et des **garde-fous** non contournables.

## 🧰 Outils exposés

| Outil | Rôle | Garde-fous |
|---|---|---|
| `ssh_list_hosts` | Liste les hôtes configurés (sans aucun secret) | — |
| `ssh_check` | Bilan de santé d'un serveur (identité, ressources, services, ports) | **Lecture seule** |
| `ssh_run` | Exécute une commande shell | Blocage destructeur, lecture seule, confirmation prod/sensible, dry-run |
| `ssh_install` | Installe des paquets (apt/dnf/yum/apk/pacman détecté) | Sensible → `confirm:true` |
| `ssh_run_tests` | Lance une commande de tests dans un dossier | Confirmation si sensible |

## 🚦 Garde-fous

- **Commandes destructrices bloquées** (`rm -rf /`, `mkfs`, `dd of=/dev/…`, fork bomb,
  `shutdown`…) — refusées **même avec confirmation**. La liste est *additive* : le
  `hosts.json` ne peut qu'en **ajouter**, jamais en retirer.
- **Allowlist d'hôtes** : seuls les alias définis dans `hosts.json` sont joignables. Pas
  d'IP arbitraire.
- **Mode lecture seule** par hôte (`"readOnly": true`) : seules les commandes de
  consultation passent (fail-closed). Idéal pour la prod.
- **Confirmation obligatoire** (`confirm: true`) avant toute commande **sensible**
  (install, `systemctl restart`, `rm`, firewall, `DROP`…) et **systématiquement en prod**.
- **Dry-run** (`dryRun: true`) : montre ce qui serait lancé sans rien exécuter.
- **Timeout** par commande (défaut 120 s).
- **Journal d'audit** append-only (`ssh-mcp-audit.log`, gitignoré) : chaque appel est tracé.

## 🔐 Secrets

`hosts.json` **n'est jamais commité** (gitignoré) et ne contient **aucun secret en clair** :

- **Clé** : `"auth": { "type": "key", "privateKeyPath": "~/.ssh/id_ed25519" }`
  (passphrase optionnelle via `"passphraseEnv": "MA_VAR"`).
- **Mot de passe** : `"auth": { "type": "password", "passwordEnv": "PROD_WEB_PASSWORD" }`
  → le mot de passe est lu dans la **variable d'environnement**, jamais dans le fichier.

## 🚀 Installation

```bash
cd mcp/ssh-admin
npm install
cp hosts.example.json hosts.json      # puis édite tes serveurs (gitignoré)

# Renseigne les secrets référencés (mots de passe / passphrases) :
export PROD_WEB_PASSWORD='...'
export STAGING_WEB_KEY_PASSPHRASE='...'

# Vérifie la config et l'accès aux clés/secrets sans rien lancer sur les serveurs :
node server.js --check-config
```

Le serveur est déclaré dans `.mcp.json` à la racine du dépôt : Claude Code / l'extension
VSCode le démarre automatiquement à l'ouverture du projet. Dans VSCode, ouvre la palette et
approuve le serveur MCP si l'IDE le demande.

## 🧭 Utilisation type (ce que Claude fait)

1. `ssh_list_hosts` puis `ssh_check host=staging-web` pour diagnostiquer sans risque.
2. `ssh_run … dryRun:true` pour valider la commande.
3. `ssh_install`/`ssh_run … confirm:true` pour agir après ton feu vert.
4. `ssh_run_tests host=staging-web directory=/srv/app testCommand="npm test"` pour vérifier.

Commence toujours sur **staging**, pas la prod.
