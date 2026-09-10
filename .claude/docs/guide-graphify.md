# Guide Graphify — cartographier un projet en graphe de connaissances

**Graphify** ([Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)) est un
skill Claude Code externe qui transforme **n'importe quel dossier** — code, Markdown, PDF,
captures d'écran, schémas — en un **graphe de connaissances interrogeable**.

Intérêt concret pour ce dépôt : au lieu de découvrir une codebase à coups de `grep` et de
charger des fichiers entiers en contexte, on lit une **carte** du projet (nœuds centraux,
dépendances réelles, communautés de fichiers) puis on interroge le graphe.

## Ce que ça produit

Une exécution crée un dossier `graphify-out/` (déjà ignoré par `.gitignore`) :

| Fichier | Contenu |
|---|---|
| `GRAPH_REPORT.md` | Le rapport à lire en premier : « god nodes », connexions inattendues, questions suggérées |
| `graph.html` | Graphe interactif (clic sur un nœud, recherche, filtre par communauté) |
| `graph.json` | Le graphe persistant — interrogeable des semaines plus tard sans re-scanner |
| `obsidian/`, `wiki/` | Vault Obsidian et articles Markdown navigables par un agent |
| `cache/` | Cache SHA256 : une relance ne retraite que les fichiers modifiés |

## Installation

**Prérequis** : Python >= 3.10 (tu as 3.14) et Claude Code.

Le paquet PyPI s'appelle `graphifyy` (double `y`) — le nom `graphify` est en cours de
récupération par les auteurs. La commande, elle, reste `graphify`.

### 1. Le CLI (une fois par machine)

```bash
pip install --user graphifyy
```

> **Windows** — si `graphify` n'est pas reconnu ensuite, ajoute le dossier des scripts
> Python au `PATH` : `%APPDATA%\Python\Python314\Scripts`.

### 2. Le skill, en mode projet

Depuis la racine du dépôt :

```bash
graphify install --project
```

Le mode `--project` est exactement ce qu'il nous faut : tout reste **dans le dépôt**,
donc l'outillage suit chaque projet dérivé du template (convention maison). Sans
`--project`, l'installation écrit dans `~/.claude/` et dans ton `CLAUDE.md` personnel.

Relance Claude Code pour que `/graphify` soit détecté.

## Ce que l'installation modifie (vérifié dans le code du paquet)

`graphify install --project` touche trois choses :

| Cible | Contenu |
|---|---|
| `.claude/skills/graphify/SKILL.md` | Le skill lui-même |
| `.claude/CLAUDE.md` | Ligne d'enregistrement du skill |
| `CLAUDE.md` (racine) | Une section `## graphify` est **ajoutée à la fin** — vérifié à l'installation, contrairement à ce que laisse croire la doc amont |
| `.claude/skills/graphify/references/` | Fiches de référence chargées à la demande par le skill |
| `.claude/settings.json` | Deux hooks `PreToolUse`, matchers `Bash|Grep` et `Read|Glob` |

Sur le chemin de l'exécutable dans les hooks : l'installeur grave un **chemin absolu** s'il
arrive à résoudre `graphify` (via `PATH`, puis via le dossier de `sys.executable`), sinon il
retombe sur la commande nue `graphify`. Un chemin absolu Windows dans un `settings.json`
versionné casse WSL et fuite ton nom d'utilisateur : pour un usage multi-environnement,
**installe avec `python -m graphify install --project`** — la résolution échoue alors et tu
obtiens la forme portable. À vérifier après coup dans `.claude/settings.json`.

Les **hooks** méritent une explication, c'est le point le moins évident :

- **Par défaut (non strict)** : quand un graphe à jour existe, le hook ajoute un
  `additionalContext` qui suggère à l'agent d'interroger le graphe plutôt que de lire
  les fichiers bruts. Il **sort toujours en code 0** — il ne bloque jamais un outil.
- **Avec `--strict`** (opt-in) : il bloque la *première* lecture brute de chaque session
  tant qu'aucun `graphify query` n'a tourné, via le champ JSON `permissionDecision`
  (jamais via le code de sortie), puis retombe en simple suggestion.
- `GRAPHIFY_HOOK_STRICT` force le mode à l'exécution sans réinstaller.

Ces hooks sont écrits dans le `.claude/settings.json` **versionné** du dépôt : ils
partiront donc dans le commit et s'appliqueront à toute personne qui clone. C'est
voulu ici (c'est le but du template), mais à savoir.

## Quel modèle fait l'extraction

Le code est parsé **en local** (AST tree-sitter), sans LLM et sans aucune clé. Un corpus
purement code — le `/graphify .` habituel sur un dépôt — ne fait donc appel à aucun modèle.
Seuls les docs, PDF et images déclenchent une extraction sémantique.

Deux chemins, à ne pas confondre :

- **Via le skill `/graphify` dans Claude Code** (ton cas) : si `GEMINI_API_KEY` ou
  `GOOGLE_API_KEY` est défini, Gemini fait l'extraction sémantique ; sinon **c'est la
  session Claude en cours qui joue ce rôle**, via des sous-agents. Le skill précise
  explicitement qu'aucune autre clé n'est lue — ni `ANTHROPIC_API_KEY`, ni
  `OPENAI_API_KEY` — et qu'il ne faut jamais bloquer en réclamant une clé.
- **En CLI nu** (`graphify extract . --backend X`, hors agent) : là seulement,
  `detect_backend` choisit selon les clés présentes dans l'environnement, dans l'ordre
  gemini → kimi → claude → openai → deepseek → azure → bedrock → ollama (ollama en
  dernier pour ne jamais court-circuiter silencieusement une clé payante).

Conséquence pratique : tu n'as **aucune clé à configurer**. Sur du code pur, rien ne sort
de ta machine ; sur des docs, le contenu passe par ta session Claude existante.

## Usage courant

```bash
/graphify .                       # cartographie le dossier courant
/graphify ./src --mode deep       # extraction plus agressive des relations déduites
/graphify . --update              # incrémental : ne retraite que ce qui a changé
```

```bash
/graphify query "qu'est-ce qui relie l'authentification au cache ?"
/graphify path "UserService" "Database"      # chemin entre deux composants
/graphify explain "OrchestrateurAgent"       # contexte d'un nœud
```

Options utiles :

- `--watch` — reconstruit le graphe à chaque sauvegarde de fichier de code (sans LLM).
- `--wiki` — génère un wiki Markdown qu'un agent peut parcourir à la lecture.
- `--svg` / `--graphml` / `--neo4j` — exports (Notion, Gephi/yEd, Neo4j).
- `--mcp` — démarre un serveur MCP stdio : le graphe devient un outil pour les agents.
- `graphify hook install` — hook git `post-commit` qui régénère le graphe à chaque commit.

## Comment ça s'articule avec le cycle de vie du dépôt

| Phase | Ce que graphify apporte |
|---|---|
| `/audit` (reprise d'existant) | Passe `/graphify .` **avant** l'audit : le rapport donne l'architecture réelle en une passe |
| `/feature` | `/graphify query` pour trouver les points d'impact avant de coder |
| `/incident` | `/graphify path "A" "B"` pour remonter une chaîne de dépendances suspecte |
| `/planifier` | Les « god nodes » signalent les zones à fort couplage, donc à découper en priorité |

## Précautions

- **Arêtes `INFERRED`** — chaque relation est étiquetée `EXTRACTED` (lue dans le code),
  `INFERRED` (déduite par le modèle) ou `AMBIGUOUS`. Une arête `INFERRED` est une
  hypothèse : la vérifier dans le code avant de fonder une décision dessus.
- **Confidentialité** — le code est analysé **localement** (AST tree-sitter). En revanche
  les docs, PDF et images passent par Claude. Ne lance pas graphify sur un dossier
  contenant des secrets ou des données clients sans y réfléchir.
- **Coût** — un run sur un gros corpus de docs/images consomme des tokens. Sur du code
  pur, l'extraction est locale et gratuite.
- **Sorties non versionnées** — `graphify-out/` est dans `.gitignore` : c'est régénérable.
  Si un `GRAPH_REPORT.md` mérite d'être partagé, copie-le dans `docs/`.

## Désinstaller

```bash
graphify uninstall --project
```

```bash
pip uninstall graphifyy
```

`uninstall --project` retire le skill, la ligne dans `.claude/CLAUDE.md` et les hooks de
`.claude/settings.json`. Les sorties (`graphify-out/`) se suppriment à la main.
