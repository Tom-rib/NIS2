# CLAUDE.md — Projet NIS2 / HydroRégie

> Cas pratique de mise en conformité **NIS2** (directive UE 2022/2555) pour **HydroRégie**,
> régie des eaux desservant 450 000 habitants, qualifiée **entité essentielle**.
> Le sujet complet est dans `NIS2_sujet.md`.

## 🎯 Le projet

Quatre livrables attendus, déposés dans un dossier structuré sur GitHub :

| Bloc | Livrable | Points d'attention |
|---|---|---|
| 1 — Qualification | Note de qualification réglementaire | Secteur, taille, statut essentiel/important, obligations induites |
| 2 — Écarts | Analyse d'écart + feuille de route | Couverture des mesures de l'article 21, priorisation, plan daté et responsabilisé |
| 3 — Architecture | Schéma d'architecture réseau segmentée IT/OT | Zones, DMZ, niveaux de criticité, pare-feu/VLAN/VPN, continuité du service d'eau potable |
| 4 — Crise | Chronologie de crise + notifications rédigées | Alerte précoce **24 h**, notification **72 h**, rapport final **1 mois** |

Contraintes de départ : IT et OT **non cloisonnés** aujourd'hui ; courrier de l'autorité
nationale confirmant le statut d'entité essentielle.

Sources à privilégier : texte de la directive (UE) 2022/2555, ANSSI, ENISA, MonEspaceNIS.
**Toute affirmation réglementaire doit être adossée à un article ou à une source citée** —
pas d'approximation sur les seuils, les délais ou les sanctions.

## 🗂️ Organisation du dépôt

- La **racine ne contient que le rendu** : sujet, README, dossiers de livrables.
- Tout l'outillage Claude Code vit sous **`.claude/`** : `agents/`, `skills/`, `commands/`,
  `memory/`, `scripts/`, `mcp/`, `docs/` (guides d'utilisation de l'outillage).
- `.mcp.json` et ce fichier restent à la racine (Claude Code les y attend).

## 🎯 Philosophie

1. **Comprendre avant d'agir.** Demande ambiguë → questions (skill `reflexion`) plutôt que
   deviner. Sur un sujet réglementaire, une hypothèse implicite se paie cher.
2. **Déléguer au bon spécialiste.** Chaque domaine a son agent (`.claude/agents/`).
   L'agent `orchestrateur` coordonne.
3. **Sécurité par défaut.** Jamais de secret en clair, jamais de commande destructrice sans
   confirmation. L'agent `devsecops` veille.
4. **Garder la trace.** Le travail important se note dans `.claude/memory/JOURNAL.md`
   (skill `memoire`) ; les choix structurants dans `DECISIONS.md`.
5. **Apprendre l'utilisateur.** Ses manières de travailler se mémorisent automatiquement
   dans `.claude/memory/PREFERENCES.md` (skill `preferences`) et s'appliquent d'office.
6. **Honnêteté du rendu.** Ce qui n'est pas fait n'est pas présenté comme fait ; une
   hypothèse de travail est annoncée comme telle.

## 🧭 Cycle de vie

| Phase | Skill / commande | Ce qui en sort |
|---|---|---|
| 1. Cadrage | `reflexion` → `cahier-des-charges` (`/cahier-des-charges`) | Besoin formalisé, périmètre |
| 2. Planification | `planification` (`/planifier`) | Backlog priorisé dans `.claude/memory/BACKLOG.md` |
| 3. Production | `cycle-dev` (`/feature`) | Livrable rédigé, relu, documenté |
| 4. Livraison | `livraison` (`/livrer`) | Version, changelog, tag |
| 5. Suivi | `rapport-avancement` (`/rapport`) | Point d'avancement honnête |
| En cas de pépin | `incident` (`/incident`) | Stabilisation, hotfix, post-mortem |
| Reprise d'existant | `graphify` (`/graphify .`) puis `audit-existant` (`/audit`) | Cartographie, état des lieux |
| Ajout d'outillage | `verif-skills` (`/verifier`) puis `chercher-extensions` | Verdict sécurité, puis intégration |

## 🤖 Agents (`.claude/agents/`)

`orchestrateur`, `chef-de-projet`, `frontend-uiux`, `backend-api`, `architecte-donnees`,
`devops-cloud`, `devsecops`, `sysadmin`, `admin-distant`, `qa-testing`, `reviseur-code`,
`debugger`, `redacteur-docs`, `formateur`.

Sur ce projet, les plus utiles : **`devsecops`** (mesures de l'article 21, durcissement),
**`sysadmin`** et **`devops-cloud`** (segmentation IT/OT, pare-feu, VLAN, VPN),
**`chef-de-projet`** (feuille de route datée et responsabilisée), **`redacteur-docs`**
(notes, notifications, rapports), **`formateur`** (réviser NIS2 avant soutenance).

## 🧩 Skills (`.claude/skills/`)

`memoire`, `preferences`, `reflexion`, `conseil-multi-ia`, `nouveau-projet`,
`cahier-des-charges`, `planification`, `cycle-dev`, `livraison`, `audit-existant`,
`incident`, `rapport-avancement`, `ui-ux-pro-max`, `chercher-extensions`, `verif-skills`,
`graphify`, `archify`, `admin-mcp-ssh`.

**`archify`** est le bon outil pour le **bloc 3** : il rend une architecture en diagramme
HTML autonome et validé (zones, DMZ, flux IT/OT). Attention : le HTML produit charge ses
polices depuis Google Fonts — à savoir avant de le diffuser hors de l'organisation.

Réflexe sécurité : **rien ne s'installe sans scan**. Avant tout `npx skills add`,
`/plugin install`, ajout dans `.mcp.json` ou copie d'un `SKILL.md` trouvé en ligne, lance
`/verifier <URL ou chemin>`. Un skill est du texte exécuté avec les droits de l'utilisateur :
pas besoin de code pour être malveillant. Mais le score ne tranche pas seul — en mode
statique le scanner confond les négations et matche des mots-clés dans de simples fichiers
de données : ouvre chaque finding HIGH/CRITICAL avant de conclure.

## 🔁 Commandes (`.claude/commands/`)

`/nouveau-projet`, `/cahier-des-charges`, `/planifier`, `/feature`, `/livrer`, `/audit`,
`/incident`, `/rapport`, `/reflechir`, `/conseil`, `/sauver-contexte`, `/reprendre`,
`/preferences`, `/graphify`, `/archify`, `/verifier`.

## 🔌 Serveurs MCP (`.mcp.json`)

Douze serveurs préconfigurés (détails : `.claude/docs/guide-mcp.md`) : `context7`,
`playwright`, `sequential-thinking`, `mcp-compass`, `github`, `postgres`, `firecrawl`,
`brave-search`, `sentry`, `vercel`, `figma`, `ssh-admin`.

Pour ce projet : **`brave-search`** et **`firecrawl`** pour aller chercher les textes ANSSI
et ENISA à jour plutôt que citer de mémoire. Si un serveur n'est pas connecté (clé
manquante, app fermée), travaille sans lui et signale-le.

Le MCP `ssh-admin` attend ses dépendances : `cd .claude/mcp/ssh-admin && npm install`, puis
`cp hosts.example.json hosts.json` (le vrai `hosts.json` est gitignoré).

## 📌 Apprentissage automatique des préférences

Dès que l'utilisateur **exprime une préférence**, **corrige ta façon de faire**, ou **répète
un même choix**, enregistre-le immédiatement dans `.claude/memory/PREFERENCES.md`
(skill `preferences`), sans demander la permission — signale-le juste en une ligne.

## ✅ Conventions transverses

- **Langue** : livrables et documentation en français ; identifiants de code en anglais.
- **Commits** : messages clairs à l'impératif (`Ajoute…`, `Corrige…`, `Refactore…`).
- **Branches** : ne jamais pousser sur `main` sans demande explicite.
- **Secrets** : variables d'environnement uniquement ; voir `.env.example`, jamais `.env`.
- **Citations** : toute règle NIS2 avancée est rattachée à son article ou à sa source.
