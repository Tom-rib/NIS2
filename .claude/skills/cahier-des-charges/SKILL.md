---
name: cahier-des-charges
description: Rédige un cahier des charges / une spécification fonctionnelle avant de développer. À utiliser au démarrage d'un projet ou d'une fonctionnalité importante pour formaliser le besoin, les user stories, les critères d'acceptation et le périmètre. Déclencheurs : « cahier des charges », « spécifie », « rédige la spec », « formalise le besoin ».
---

# Cahier des charges

Dans une vraie entreprise de développement, on n'écrit pas une ligne de code sans un
besoin formalisé. Ce skill produit un document court mais engageant : ce qu'on construit,
pour qui, et comment on saura que c'est réussi.

## Quand l'utiliser
- Au démarrage d'un projet (juste après le cadrage du skill `reflexion`).
- Avant une fonctionnalité majeure ou structurante.
- Quand le client/utilisateur et l'équipe ne semblent pas alignés sur le besoin.

## Méthode

1. **Collecte** : si le besoin n'est pas clair, active d'abord le skill `reflexion`
   pour poser les questions décisives. Ne rédige jamais une spec sur des suppositions.

2. **Rédige** le document dans `docs/projet/CAHIER-DES-CHARGES.md` avec cette structure :

   ```markdown
   # Cahier des charges — <nom du projet>

   _Version : <n> — <date> — Statut : brouillon | validé_

   ## 1. Contexte & problème
   <Le problème qu'on résout, en langage client. Pas de technique ici.>

   ## 2. Objectifs & critères de succès
   <2-4 objectifs mesurables : « réussi » ressemble à quoi ?>

   ## 3. Utilisateurs & personas
   <Qui utilise le produit, dans quel contexte.>

   ## 4. Fonctionnalités (user stories)
   | ID | En tant que… | Je veux… | Afin de… | Priorité |
   |---|---|---|---|---|
   | US-01 | … | … | … | Must / Should / Could |

   ## 5. Critères d'acceptation
   <Par user story « Must » : conditions vérifiables de type Étant donné / Quand / Alors.>

   ## 6. Hors périmètre
   <Ce qu'on ne fait explicitement PAS dans cette version.>

   ## 7. Contraintes
   <Stack imposée, délais, budget, conformité (RGPD…), existant à respecter.>

   ## 8. Exigences non fonctionnelles
   <Performance, sécurité, accessibilité, disponibilité — seulement ce qui est réellement exigé.>
   ```

3. **Fais valider** : présente un résumé à l'utilisateur et demande la validation
   (ou les corrections) avant de passer à la planification.

4. **Enchaîne** : une fois validé, propose le skill `planification` pour transformer
   les user stories en backlog priorisé.

## Principes
- **Court et vérifiable** : chaque exigence doit pouvoir être testée. « L'app doit être
  rapide » est interdit ; « la page liste répond en < 500 ms pour 1000 éléments » est bon.
- Les priorités suivent **MoSCoW** (Must / Should / Could / Won't).
- La section « Hors périmètre » est **obligatoire** : c'est elle qui évite les dérives.
- Le document vit : mets à jour la version et le statut à chaque évolution validée.
