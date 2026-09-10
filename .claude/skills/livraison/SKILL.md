---
name: livraison
description: Prépare et exécute une livraison (release) professionnelle — version sémantique, changelog, vérifications pré-livraison, tag. À utiliser quand une version doit être publiée ou déployée. Déclencheurs : « livre », « fais une release », « publie la version », « prépare le déploiement ».
---

# Livraison (release)

Une entreprise sérieuse ne livre pas « ce qu'il y a sur la branche » : elle livre une
version identifiée, vérifiée et documentée. Ce skill déroule la checklist de livraison.

## Méthode

### 1. Décider la version (semver)
- **MAJOR** (2.0.0) : rupture de compatibilité.
- **MINOR** (1.3.0) : nouvelles fonctionnalités compatibles.
- **PATCH** (1.2.4) : corrections uniquement.
- Regarde le changelog « Unreleased » et les commits depuis le dernier tag pour trancher.
  Propose la version à l'utilisateur avec la justification.

### 2. Vérifier (bloquant)
Avant tout tag ou déploiement, dans l'ordre :
1. Suite de tests complète **verte**.
2. Linter/format sans erreur.
3. Pas de secret, de `TODO` critique ou de code de debug dans le diff de la release.
4. Passe rapide `devsecops` si la release touche auth, dépendances ou exposition réseau.
5. La doc utilisateur/API reflète les changements livrés.

Un point rouge = on corrige ou on repousse. Signale-le honnêtement, ne « force » jamais.

### 3. Documenter
- Mets à jour `CHANGELOG.md` (format Keep a Changelog) : bascule « Unreleased » vers
  la nouvelle version datée, sections Added / Changed / Fixed / Removed / Security.
- Mets à jour le numéro de version là où le projet le déclare (package.json,
  pyproject.toml, etc.).

### 4. Livrer
- Commit de release : `Release v<X.Y.Z>` puis tag annoté `v<X.Y.Z>`.
- **Demande confirmation avant** : push du tag, fusion dans `main`, déploiement.
  Ce sont des actions visibles de l'extérieur.
- Pour le déploiement lui-même, délègue à `devops-cloud` (ou `admin-distant` pour un
  serveur géré en SSH).

### 5. Après la livraison
- Vérifie que la version déployée répond (healthcheck, page d'accueil, endpoint clé).
- Note la release dans `.claude/memory/JOURNAL.md` : version, contenu marquant, où c'est
  déployé.
- Ouvre une nouvelle section « Unreleased » dans le changelog.

## Règles
- Jamais de livraison le vendredi soir sans demande explicite 😉 — plus sérieusement :
  jamais de livraison sans possibilité de retour arrière identifiée (tag précédent,
  rollback du déploiement).
- Une release = un état **reproductible** : tout est commité et tagué, rien d'ambiant.
- En cas de problème juste après livraison, bascule sur le skill `incident`.
