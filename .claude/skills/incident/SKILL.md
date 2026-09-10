---
name: incident
description: Gestion d'incident et hotfix — stabiliser d'abord, corriger proprement ensuite, puis post-mortem. À utiliser quand quelque chose est cassé en production ou bloque l'utilisateur maintenant : panne, régression livrée, faille découverte, service down. Déclencheurs : « c'est cassé en prod », « urgence », « hotfix », « le site est down », « incident ».
---

# Gestion d'incident

Quand la production brûle, une équipe pro suit un ordre strict : **stabiliser → corriger
→ comprendre**. Pas l'inverse. Ce skill impose cet ordre.

## Phase 1 — Stabiliser (minutes)
Objectif : faire cesser l'impact, pas trouver le coupable.
1. **Évalue l'impact** : qui/quoi est touché, depuis quand, est-ce que ça empire ?
2. **Cherche le retour arrière le plus rapide** : rollback vers le dernier tag/déploiement
   sain, désactivation de la fonctionnalité fautive, redémarrage du service
   (`admin-distant`/`sysadmin` pour un serveur, `devops-cloud` pour un déploiement).
3. **Demande confirmation** avant toute action sur la production, mais présente-la comme
   une recommandation prête à exécuter, pas une liste d'options.
4. Note l'heure et les actions au fil de l'eau (ça servira au post-mortem).

## Phase 2 — Corriger (heures)
Une fois l'impact stoppé :
1. `debugger` établit la cause racine (pas juste le symptôme).
2. Correctif minimal sur une branche `fix/…`, via le skill `cycle-dev` en version
   accélérée : le correctif + un test qui **reproduit le bug** et prouve la correction.
   Le test anti-régression n'est pas négociable, même en urgence.
3. Livraison du correctif via le skill `livraison` (version PATCH).

## Phase 3 — Comprendre (post-mortem, sans blâme)
Rédige `docs/projet/postmortems/<date>-<titre-court>.md` :

```markdown
# Post-mortem — <titre> — <date>

## Impact
<Qui, quoi, combien de temps.>

## Chronologie
<Heure par heure : détection, actions, résolution.>

## Cause racine
<La vraie cause, pas « erreur humaine » — qu'est-ce qui a permis à l'erreur d'atteindre la prod ?>

## Ce qui a bien / mal fonctionné
<Détection rapide ? Rollback disponible ? Tests aveugles sur ce cas ?>

## Actions préventives
| Action | Type | Priorité |
|---|---|---|
| <ex. test E2E sur le parcours de paiement> | test / monitoring / process | Must |
```

Ajoute les actions préventives au backlog (`planification`) et une entrée au
`JOURNAL.md`.

## Règles
- **Pendant la phase 1, aucun refactoring, aucun « pendant qu'on y est ».** Le
  périmètre d'un hotfix est le strict minimum.
- Communique l'état à chaque bascule de phase : impact → stabilisé → corrigé → compris.
- Un incident sans post-mortem est un incident qui reviendra.
