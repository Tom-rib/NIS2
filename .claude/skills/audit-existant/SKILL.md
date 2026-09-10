---
name: audit-existant
description: Audit et reprise d'un projet existant — cartographie du code, état des tests, dette technique, sécurité, plan de reprise. À utiliser quand on récupère une codebase qu'on ne connaît pas (projet client, legacy, open source) avant d'y toucher. Déclencheurs : « audite ce projet », « analyse cette codebase », « on reprend ce projet », « état des lieux ».
---

# Audit d'un projet existant

Une entreprise qui reprend le projet d'un client commence par un état des lieux, pas par
du code. Ce skill produit un rapport d'audit et un plan de reprise.

## Méthode

### 1. Cartographier (lecture seule)
Explore sans rien modifier :
- **Structure** : langages, frameworks, arborescence, points d'entrée.
- **Exécution** : comment ça se lance ? Y a-t-il un README fiable ? Essaie réellement
  d'installer et de lancer le projet — c'est le test le plus révélateur.
- **Tests & CI** : une suite existe-t-elle ? Passe-t-elle ? Couverture approximative ?
- **Dépendances** : versions obsolètes, dépendances abandonnées, vulnérabilités connues.
- **Données** : schéma de BDD, migrations, données sensibles.

Pour une codebase volumineuse, délègue l'exploration en parallèle : `devsecops` (secrets
en dur, failles évidentes), `qa-testing` (état des tests), `architecte-donnees` (schéma).

### 2. Évaluer
Note chaque axe en 🟢 / 🟡 / 🔴 avec une phrase de justification :
lisibilité, tests, sécurité, dépendances, documentation, facilité de déploiement.

### 3. Rédiger le rapport
Écris `docs/projet/AUDIT.md` :

```markdown
# Audit — <projet> — <date>

## Synthèse (à lire en 30 secondes)
<3-5 phrases : état général, risques majeurs, effort de reprise estimé.>

## Cartographie
<Stack, structure, comment ça se lance, ce qui fonctionne aujourd'hui.>

## Évaluation par axe
| Axe | État | Constat |
|---|---|---|
| Tests | 🟡 | … |

## Risques prioritaires
<Classés : ce qui peut faire mal en premier (sécu > perte de données > dette).>

## Plan de reprise recommandé
<Étapes ordonnées, gains rapides d'abord. Chiffrées en S/M/L.>
```

### 4. Enchaîner
Présente la synthèse à l'utilisateur, puis propose de transformer le plan de reprise en
backlog (skill `planification`). Les urgences de sécurité passent toujours en premier.

## Règles
- **Ne modifie rien pendant l'audit** — pas même un « petit fix évident ». L'audit
  observe, le plan corrige.
- Distingue les **faits** (« 0 test », « clé API commitée dans config.js ») des
  **opinions** (« je structurerais autrement »). Le rapport privilégie les faits.
- Si tu découvres un secret exposé ou une faille exploitable, signale-le à l'utilisateur
  immédiatement, sans attendre la fin du rapport.
