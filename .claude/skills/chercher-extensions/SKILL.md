---
name: chercher-extensions
description: Trouve et ajoute des capacités au projet — serveurs MCP, skills, plugins. À utiliser quand il manque un outil pour la tâche en cours, ou quand l'utilisateur demande d'étendre la stack. Déclencheurs : « trouve un MCP/skill/plugin pour… », « il nous faudrait un outil qui… », « ajoute une capacité », « étends la stack », « existe-t-il un serveur MCP pour… ».
---

# Chercher & ajouter des extensions (MCP, skills, plugins)

Ce skill fait de Claude son propre « responsable outillage » : quand une capacité
manque, il sait où chercher, comment évaluer, et comment intégrer proprement.

## 1. Identifier le besoin
Formule le besoin en une phrase (« interroger l'API Stripe », « générer des PDF »,
« mémoire sémantique »). Vérifie d'abord que l'existant ne couvre pas déjà le besoin :
agents, 13+ skills, serveurs MCP de `.mcp.json`, outils intégrés. **Pas de doublon.**

## 2. Chercher au bon endroit

### Serveurs MCP → outil `mcp-compass` (préconfiguré)
Interroge `recommend-mcp-servers` en langage naturel ; il renvoie des serveurs
candidats avec leur dépôt GitHub. Compléments : le registre officiel
(registry.modelcontextprotocol.io), le catalogue
github.com/modelcontextprotocol/servers, et une recherche web classique.

### Skills → CLI `skills.sh` (écosystème ouvert, 18+ agents compatibles)
```bash
npx skills find "<mots-clés>"     # cherche dans l'annuaire skills.sh
npx skills add <owner/repo>        # installe un skill (après audit !)
```

### Plugins Claude Code → marketplaces
```bash
/plugin marketplace add <owner/repo>   # déclare une source
/plugin install <nom>@<marketplace>    # installe
```
Marketplaces déjà déclarées dans `settings.json` : `thedotmack` (claude-mem),
`superpowers-marketplace`. Voir les verdicts existants dans `.claude/docs/guide-plugins.md`.

## 3. Auditer AVANT d'ajouter (obligatoire)
Applique la méthode de `.claude/docs/guide-plugins.md` :
0. **Scan automatique d'abord** — skill `verif-skills` :
   ```bash
   skillspector scan <URL du dépôt ou chemin> --no-llm
   ```
   Il détecte prompt injection, exfiltration, escalade de privilèges et agentivité
   excessive dans le `SKILL.md` lui-même. Le score oriente, il ne tranche pas :
   ouvre chaque finding HIGH/CRITICAL avant de conclure.
1. Clone/inspecte le code : cherche réseau (`fetch`, URLs), exécution
   (`subprocess`, `exec`), accès hors projet, télémétrie, hooks automatiques.
2. Résume le verdict à l'utilisateur : ce que ça fait, ce que ça touche, ce qui
   sort de la machine. **Demande son accord avant d'installer.**
3. Consigne le verdict dans `.claude/docs/guide-plugins.md` (intégré / disponible / écarté).

## 4. Intégrer proprement
- **MCP** : entrée dans `.mcp.json` (secrets via `${VAR}`, jamais en clair) +
  ligne dans `.claude/docs/guide-mcp.md` + pré-autorisation dans `settings.json`
  seulement si lecture seule.
- **Skill** : copie dans `.claude/skills/<nom>/` + tableau de `CLAUDE.md` +
  `.claude/docs/guide-agents.md`.
- **Plugin** : marketplace dans `extraKnownMarketplaces` ; activation via
  `enabledPlugins` seulement si non redondant.
- Branche le ou les **agents** concernés (une ligne « Outils MCP » dans leur fiche).
- Mets à jour la mémoire (`DECISIONS.md` : pourquoi cet outil a été ajouté).

## Règles
- Un outil qui fait doublon n'entre pas, même s'il est populaire.
- Préférer : officiel > maintenu et audité > obscur. En cas d'égalité, le plus simple.
- Ce qui écrit, dépense ou touche la prod ne se pré-autorise jamais dans
  `settings.json` — confirmation à chaque usage.
