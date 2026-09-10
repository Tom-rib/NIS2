# Guide — Archify : des diagrammes d'architecture vérifiables

> **En un mot** : Archify transforme une petite spécification JSON typée en un diagramme
> HTML autonome, interactif et validé. C'est un **outil de restitution**, pas un outil
> d'économie de tokens — voir la section « Ce que ça ne fait pas ».

- **Source** : [tt-a1i/archify](https://github.com/tt-a1i/archify) — licence MIT
- **Version intégrée** : 2.17.0-dev.1 (commit `920543b`, 2026-09-07)
- **Emplacement** : `.claude/skills/archify/` (vendu dans le dépôt, ~2,5 Mo)
- **Commande** : `/archify`
- **Prérequis** : Node ≥ 18. **Aucune dépendance à installer.**

## Pourquoi il est là

Le dépôt savait déjà **comprendre** une codebase (`graphify` : graphe de connaissances
interrogeable) et **l'auditer** (`/audit`). Il ne savait pas la **montrer**. Archify comble
ce trou, et les deux s'enchaînent bien :

```
/graphify .          → cartographie réelle du dépôt (nœuds centraux, dépendances)
/graphify query "…"  → extrait le sous-graphe qui t'intéresse
/archify …           → transforme ce sous-graphe en diagramme livrable
```

⚠️ **Le maillon faible est la jonction.** Une arête `INFERRED` de graphify est une déduction
du modèle, pas une lecture du code. La dessiner dans un diagramme la transforme en fait
d'apparence officielle. Vérifie dans le code avant de tracer.

## Les cinq types

| Type | Pour quoi |
|---|---|
| `architecture` | Composants, services, frontières cloud/sécurité, infrastructure |
| `workflow` | Processus, portes d'approbation, appels d'outils, runbooks, CI/CD |
| `sequence` | Séquences d'appels d'API, allers-retours, cycles de vie de requête |
| `dataflow` | Pipelines de données, ETL/ELT, lignage |
| `lifecycle` | Machines à états, cycles de vie, états d'échec récupérables |

Il accepte aussi du **Mermaid collé** (`flowchart`, `sequenceDiagram`, `stateDiagram`) et le
convertit — pratique pour reprendre un diagramme existant sans repartir de zéro.

## Utilisation

```bash
/archify l'architecture de mon cluster k8s : ingress, 3 services, postgres, redis
```

Sous le capot, en deux commandes :

```bash
node .claude/skills/archify/bin/archify.mjs validate architecture candidat.json --quality showcase --json
node .claude/skills/archify/bin/archify.mjs deliver  architecture candidat.json sortie.html --quality showcase --json
```

`validate` en mode `showcase` fait passer **9 contrôles d'artefact** et exige 0 erreur et
0 avertissement de composition. Un reçu qui n'affiche que 4 contrôles est une validation
basique, pas une acceptation showcase — ne la présente pas comme telle.

Vérifié à l'installation sur un exemple fourni : `9/9 artifact checks; composition showcase:
pass`, HTML de 715 Ko produit, code de sortie 0.

## Ce que ça ne fait pas

- **Ça n'économise pas de tokens.** Le rendu est déterministe et hors modèle, donc la partie
  dessin ne coûte rien — mais produire le JSON IR coûte des tokens comme n'importe quelle
  génération. Ton vrai levier d'économie dans ce dépôt reste `graphify` : interroger un graphe
  plutôt que recharger des fichiers entiers en contexte.
- **Ça n'inspecte pas ton code tout seul.** Il faut lui fournir la topologie, à la main ou
  via graphify. Il ne devine pas ton architecture.

## Sécurité — ce qu'il faut savoir

Scanné avec SkillSpector (mode statique) le 2026-09-08. **Score brut : 74/100 HIGH.**
Les 5 findings HIGH ont été ouverts un par un : **tous faux positifs**, deux familles.

| Famille | Ce que le motif matche | Réalité |
|---|---|---|
| `P2` / `YR4` « instructions cachées » | la syntaxe de commentaire HTML `<!-- … -->` | Des commentaires de développeur : chargement de police, raccourcis clavier, exemples de flèches SVG |
| `RA2` « persistance de session » | la variable `relationshipList` | Un `<ul>` du panneau « lentille sémantique » manipulé en DOM. Ni cron, ni script de démarrage, ni fichier d'état |

Après baseline justifié : **13/100 LOW**, cohérent avec les 11/100 obtenus en scannant le
seul cœur exécutable (`SKILL.md` + `bin/` + `scripts/`).

**Audit manuel du HTML livré** (c'est lui qu'on partage, donc c'est lui qui compte) :

- `fetch` / `XMLHttpRequest` / `sendBeacon` / `WebSocket` / `import()` → **aucun**
- `eval` / `new Function` / `innerHTML =` → **aucun**
- `new Image()` ×3 → rastérisation SVG→canvas pour l'export PNG, pas de balise-espion
- hôtes externes → `www.w3.org` (espaces de noms SVG, jamais requêtés) et Google Fonts

### Deux résidus assumés, pas des faux positifs

1. **Le HTML généré appelle Google Fonts.** Quiconque **ouvre** un diagramme exporté est vu
   par Google. Repli prévu sur la pile monospace système si le réseau est coupé. À savoir
   avant de diffuser un diagramme hors de l'organisation. Pour un livrable sensible, coupe
   les deux `<link>` vers `fonts.googleapis.com` dans le HTML produit.
2. **Le skill ne déclare pas d'`allowed-tools`** (finding `LP3`, laissé visible exprès). On ne
   patche pas le `SKILL.md` amont pour ne pas casser les montées de version : le garde-fou est
   en aval, dans les permissions de `.claude/settings.json`.

### Le rappel de mise à jour

`SKILL.md` § « Update awareness » demande de lancer `scripts/check-update.mjs` après le premier
candidat — un rappel réseau automatique. À sa décharge, le skill est explicite : il annonce
qu'il ne télécharge ni n'installe rien, et que « le silence ne vaut pas consentement ».
Neutralisé quand même, par principe :

```json
"env": { "ARCHIFY_UPDATE_CHECK_DISABLED": "1" }
```

Pour vérifier les mises à jour, fais-le explicitement, à la main.

## Rejouer le scan

Le baseline **n'est pas chargé automatiquement** — il faut le passer explicitement :

```bash
skillspector scan .claude/skills/archify --no-llm --baseline .claude/skills/archify/.skillspector-baseline.yaml
```

Sans `--baseline`, tu retomberas sur 74/100 HIGH et tu croiras à une régression.

Il reste 14 findings MEDIUM `RA2` après baseline : même famille `relationshipList` déjà
vérifiée, à des numéros de ligne que les empreintes n'attrapent pas. Laissés visibles
volontairement — on ne muselle pas l'outil.
