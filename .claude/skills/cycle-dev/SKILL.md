---
name: cycle-dev
description: Workflow complet de développement d'une fonctionnalité, comme dans une équipe professionnelle — branche, implémentation, tests, revue de code, documentation, commit propre. À utiliser dès qu'on développe une fonctionnalité ou un correctif non trivial. Déclencheurs : « développe la fonctionnalité », « implémente », « ajoute la feature », « corrige le bug » (après diagnostic).
---

# Cycle de développement d'une fonctionnalité

Dans une vraie équipe, une fonctionnalité ne se résume pas à « écrire le code » : elle
suit un pipeline qui garantit la qualité à chaque étape. Ce skill déroule ce pipeline.

## Le pipeline

### 1. Préparer
- Identifie la tâche dans le backlog (`.claude/memory/BACKLOG.md`) si elle existe ;
  sinon, reformule l'objectif et les critères d'acceptation en 2-3 lignes.
- Crée une branche dédiée : `feature/<courte-description>` ou `fix/<courte-description>`
  (identifiants en anglais). Jamais de travail direct sur `main`.
- Passe la tâche « en cours » dans le backlog.

### 2. Implémenter
- Délègue au(x) spécialiste(s) : `backend-api`, `frontend-uiux`, `architecte-donnees`…
  Pour une fonctionnalité pluridisciplinaire, passe par l'`orchestrateur`.
- Commits atomiques au fil de l'eau, messages à l'impératif (`Ajoute…`, `Corrige…`).

### 3. Tester
- `qa-testing` écrit ou complète les tests couvrant les critères d'acceptation
  (cas nominal + cas d'erreur significatifs).
- Lance **toute** la suite de tests et le linter, pas seulement les nouveaux tests.
- Un test qui échoue = on corrige avant d'avancer. Jamais de test désactivé pour « passer ».

### 4. Relire
- `reviseur-code` relit le diff complet de la branche : bugs, lisibilité, simplification.
- Si l'authentification, les entrées utilisateur, les secrets ou les permissions sont
  touchés : revue `devsecops` en plus.
- Applique les corrections retenues ; note dans la réponse ce qui a été volontairement
  écarté et pourquoi.

### 5. Documenter
- `redacteur-docs` met à jour ce qui est impacté : README, doc d'API, changelog
  (section « Unreleased »).
- Une décision d'architecture prise en route ? Consigne-la dans
  `.claude/memory/DECISIONS.md` (une ligne suffit : contexte → décision → raison).

### 6. Livrer la branche
- Vérifie une dernière fois : tests verts, linter propre, diff relu.
- Pousse la branche. **Ne crée une PR et ne fusionne dans `main` que si l'utilisateur
  le demande.**
- Passe la tâche « fait » dans le backlog et mets à jour `ETAT.md` (skill `memoire`).

## Compte-rendu final
Termine toujours par un résumé court : ce qui a été fait, comment c'est testé,
ce qui a été relu/corrigé, et ce qui reste éventuellement à décider.

## Règles
- Les étapes 3 et 4 ne sont **pas optionnelles**, même pour un « petit » changement.
- Si l'implémentation révèle que la tâche était mal découpée ou plus grosse que prévu,
  arrête-toi et repasse par `planification` plutôt que de t'enfoncer.
- Échec honnête : si les tests ne passent pas à la fin, livre l'état réel et le
  diagnostic, jamais un « c'est bon » de façade.
