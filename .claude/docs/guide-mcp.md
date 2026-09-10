# Guide MCP — connecter Claude Code au monde extérieur

Les serveurs **MCP** (Model Context Protocol) donnent à Claude des outils supplémentaires :
lire la doc à jour d'une bibliothèque, piloter un navigateur, interroger la base, gérer
les PRs GitHub… Ce dépôt en préconfigure **12** dans **`.mcp.json`** (à la racine,
versionné) ; ils sont approuvés automatiquement via `enableAllProjectMcpServers` dans
`.claude/settings.json`.

> Un serveur dont le prérequis manque (clé absente, app fermée) apparaît simplement en
> erreur dans `/mcp` — c'est normal et sans impact sur les autres. Configure uniquement
> ceux dont tu as besoin.

## Les 12 serveurs préconfigurés

### ✅ Sans configuration (marchent tout de suite)

| Serveur | À quoi ça sert | Agents principaux |
|---|---|---|
| `context7` | Documentation **à jour** de milliers de bibliothèques — fini le code écrit de mémoire sur une API dépassée | `backend-api`, `frontend-uiux`, `devops-cloud` |
| `playwright` | Piloter un vrai navigateur : vérifier une UI, tester un parcours, captures d'écran (Node ≥ 18) | `frontend-uiux`, `qa-testing` |
| `sequential-thinking` | Raisonnement pas à pas structuré pour les problèmes complexes (architecture, débogage retors) | tous |
| `mcp-compass` | **Découverte de serveurs MCP** en langage naturel — trouve le bon serveur pour un besoin (skill `chercher-extensions`) | tous |

### 🔑 Avec une clé API (variable d'environnement du shell)

| Serveur | À quoi ça sert | Variable | Où obtenir la clé |
|---|---|---|---|
| `github` | PRs, issues, revues, CI | `GITHUB_PERSONAL_ACCESS_TOKEN` | github.com/settings/tokens |
| `postgres` | Interroger la base du projet : schéma, requêtes (lecture) | `DATABASE_URL` | chaîne de connexion du projet |
| `firecrawl` | Scraper/crawler des sites web en Markdown propre (veille, extraction de contenu) | `FIRECRAWL_API_KEY` | firecrawl.dev |
| `brave-search` | Recherche web indépendante (complément de la recherche intégrée) | `BRAVE_API_KEY` | brave.com/search/api |

### 🔐 Avec authentification OAuth (lancer `/mcp` puis « Authenticate »)

| Serveur | À quoi ça sert | Agents principaux |
|---|---|---|
| `sentry` | Erreurs et crashs en production : stack traces réelles, fréquence, régressions | `debugger`, `incident` |
| `vercel` | Déploiements, logs, domaines des projets Vercel | `devops-cloud` |

### 🖥️ Avec une application locale

| Serveur | À quoi ça sert | Prérequis |
|---|---|---|
| `figma` | Lire les maquettes : composants, styles, variables — pour coder fidèle au design | App desktop Figma ouverte + serveur MCP Dev Mode activé (Préférences) |
| `ssh-admin` | Administrer tes serveurs via SSH avec garde-fous (blocage destructif, allowlist d'hôtes, journal d'audit) — skill `admin-mcp-ssh`, agent `admin-distant` | Créer `mcp/ssh-admin/hosts.json` depuis `hosts.example.json` (voir `mcp/ssh-admin/README.md`) |

## Configurer les clés

Les serveurs MCP lisent l'environnement du **shell**, pas le fichier `.env` :

```bash
# ~/.bashrc ou ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="github_pat_…"
export DATABASE_URL="postgresql://user:pass@localhost:5432/mabase"
export FIRECRAWL_API_KEY="fc-…"
export BRAVE_API_KEY="BSA…"
```

Puis relance Claude Code et vérifie avec `/mcp` que les serveurs voulus sont connectés.
(`.env.example` liste les mêmes variables pour mémoire.)

## Commandes utiles

```bash
/mcp                      # état des serveurs, outils exposés, authentification OAuth
claude mcp list           # liste les serveurs configurés
claude mcp add <nom> …    # ajoute un serveur (portée user ou project)
```

## Ajouter un serveur selon le projet

Le skill `chercher-extensions` automatise la démarche : demande « trouve un MCP
pour <besoin> » et Claude interroge `mcp-compass`, audite le candidat et l'intègre.
Manuellement : entrée dans `.mcp.json` (versionné, partagé avec l'équipe) ou
`claude mcp add`. Selon le contexte : **GitLab**, **Stripe** (paiements),
**Supabase**, **Notion**, **Slack**…
Catalogues : registre officiel https://registry.modelcontextprotocol.io et
https://github.com/modelcontextprotocol/servers

## Sécurité

- **Jamais de secret dans `.mcp.json`** (il est versionné) : référence des variables
  d'environnement avec `${VAR}`.
- N'ajoute que des serveurs dont tu comprends ce qu'ils exposent : un serveur MCP
  donne de vrais outils à Claude (écriture, API externes…).
- Les permissions de `.claude/settings.json` s'appliquent aussi aux outils MCP :
  `context7`, `playwright`, `sequential-thinking`, `brave-search` et `mcp-compass`
  sont pré-autorisés (lecture/local) ; les serveurs qui **agissent** (github,
  postgres, sentry, vercel, firecrawl, figma) demandent confirmation.
- `postgres` : utilise un utilisateur en **lecture seule** pour `DATABASE_URL` quand
  c'est possible, surtout vers une base partagée.
