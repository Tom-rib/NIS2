# Guide des agents, skills et commandes

## Les 14 agents

| Agent | Quand l'appeler | Modèle |
|---|---|---|
| `orchestrateur` | Tâche complexe à découper et répartir | opus |
| `chef-de-projet` | Cadrage, backlog, priorités, rapports d'avancement | opus |
| `frontend-uiux` | Interface, UI/UX, accessibilité, responsive | sonnet |
| `backend-api` | API, serveur, auth, logique métier | sonnet |
| `architecte-donnees` | Schéma BDD, migrations, requêtes | sonnet |
| `devops-cloud` | CI/CD, Docker, Kubernetes, Terraform, clusters | sonnet |
| `devsecops` | Sécurité, secrets, durcissement, audit | opus |
| `sysadmin` | Serveurs Linux, services, réseau, scripts | sonnet |
| `admin-distant` | Connexion SSH, installation, vérification de serveurs/bases distants | sonnet |
| `qa-testing` | Stratégie et écriture de tests | sonnet |
| `reviseur-code` | Revue d'un diff/fichier | opus |
| `debugger` | Diagnostic d'un bug, stack trace | sonnet |
| `redacteur-docs` | README, guides, doc d'API | sonnet |
| `formateur` | Cours, fiches, quiz de révision | sonnet |

Claude choisit l'agent selon la `description` du fichier. Tu peux aussi le nommer
explicitement (« demande au `devsecops` de relire l'auth »).

## Les 14 skills

| Skill | Déclencheurs | Effet |
|---|---|---|
| `memoire` | « sauvegarde », « reprends » | Persiste/relit le contexte dans `.claude/memory/` |
| `preferences` | « je préfère… », corrections, choix répétés (auto) | Mémorise les manières de travailler dans `PREFERENCES.md` |
| `reflexion` | demande vague, « pose-moi des questions » | Questions de cadrage avant d'agir |
| `conseil-multi-ia` | « avis de plusieurs IA » | Interroge Claude+GPT+Gemini, synthétise |
| `nouveau-projet` | « démarre un projet » | Cadre, propose une archi, échafaude |
| `cahier-des-charges` | « rédige la spec », « cahier des charges » | User stories, critères d'acceptation, périmètre |
| `planification` | « planifie », « fais le backlog » | Backlog priorisé dans `.claude/memory/BACKLOG.md` |
| `cycle-dev` | « développe la fonctionnalité » | Branche → code → tests → revue → doc → commit |
| `livraison` | « fais une release », « livre » | Semver, checklist qualité, changelog, tag |
| `audit-existant` | « audite ce projet », « on reprend ce projet » | Rapport d'audit + plan de reprise |
| `incident` | « c'est cassé en prod », « urgence » | Stabiliser → hotfix → post-mortem |
| `rapport-avancement` | « fais le point », « où en est-on ? » | Rapport client : réalisé, risques, décisions |
| `ui-ux-pro-max` | conception UI, choix de style/palette/typo | Recherche dans une base design (voir `docs/guide-plugins.md`) |
| `chercher-extensions` | « trouve un MCP/skill/plugin pour… » | Cherche (mcp-compass, skills.sh, marketplaces), audite, intègre |

## Les commandes slash

| Commande | Effet |
|---|---|
| `/nouveau-projet [desc]` | Démarre un projet |
| `/cahier-des-charges [besoin]` | Formalise le besoin avant de développer |
| `/planifier [objectif]` | Construit ou réorganise le backlog |
| `/feature [tâche]` | Développe une fonctionnalité via le pipeline complet |
| `/livrer [version]` | Prépare et exécute une release |
| `/audit [cible]` | État des lieux d'une codebase existante |
| `/incident [problème]` | Gestion d'urgence (stabiliser, hotfix, post-mortem) |
| `/rapport` | Point d'avancement pour le client/manager |
| `/reflechir [sujet]` | Lance le questionnement de cadrage |
| `/conseil [question]` | Convoque le conseil multi-IA |
| `/sauver-contexte` | Sauvegarde l'état dans la mémoire |
| `/reprendre` | Relit la mémoire et reprend |
| `/preferences` | Affiche/nettoie les préférences de travail mémorisées |

## Ajouter / modifier

### Un agent
Crée `.claude/agents/<nom>.md` :
```markdown
---
name: mon-agent
description: Quand l'utiliser (c'est ce qui déclenche la délégation).
tools: Read, Write, Edit, Grep, Glob, Bash   # optionnel ; omis = tous
model: sonnet                                 # sonnet | opus | haiku | inherit
---
Prompt système de l'agent : son rôle, sa méthode, ses garde-fous.
```

### Un skill
Crée `.claude/skills/<nom>/SKILL.md` :
```markdown
---
name: mon-skill
description: Ce que fait le skill ET quand l'utiliser (déclencheurs explicites).
---
Instructions détaillées que Claude suivra quand le skill est activé.
```
Un skill peut référencer des scripts (ex. `scripts/...`) ou d'autres fichiers du dossier.

### Une commande
Crée `.claude/commands/<nom>.md` :
```markdown
---
description: Texte affiché dans la liste des commandes.
argument-hint: [ce qu'attend la commande]
---
Le prompt déclenché, avec $ARGUMENTS pour insérer ce que tape l'utilisateur.
```

## Conseils de rédaction
- La `description` d'un agent/skill est **décisive** : c'est elle qui détermine quand il
  est sélectionné. Sois explicite sur les déclencheurs.
- Garde chaque agent **focalisé** : un domaine, des garde-fous clairs.
- Préfère plusieurs agents nets à un agent fourre-tout.
