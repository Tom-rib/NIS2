---
name: planification
description: Transforme un besoin en plan de travail — backlog priorisé, découpage en lots/sprints, estimations et jalons. À utiliser après le cadrage/cahier des charges, ou pour réorganiser le travail restant d'un projet en cours. Déclencheurs : « planifie », « fais le backlog », « découpe en sprints », « organise le travail », « roadmap ».
---

# Planification & backlog

Ce skill joue le rôle du chef de projet : il découpe le travail, le priorise et le rend
suivable dans le temps. Le backlog vit dans `.claude/memory/BACKLOG.md` (chargé au
démarrage de session avec le reste de la mémoire).

## Méthode

1. **Pars du besoin** : cahier des charges (`docs/projet/CAHIER-DES-CHARGES.md`) s'il
   existe, sinon fais un cadrage rapide (skill `reflexion`).

2. **Découpe en tâches livrables** : chaque tâche doit produire quelque chose de
   démontrable (une page qui s'affiche, un endpoint qui répond, un déploiement qui passe).
   Évite les tâches « techniques » invisibles sauf si elles débloquent le reste.

3. **Priorise et ordonne** :
   - Priorité MoSCoW héritée des user stories.
   - Dépendances explicites (la BDD avant l'API, l'API avant l'UI…).
   - Le **chemin critique vers un premier livrable qui tourne** passe en premier.

4. **Estime grossièrement** en tailles (S < 1 h de travail agent, M = quelques heures,
   L = une session entière, XL = à redécouper — un XL n'entre jamais tel quel au backlog).

5. **Écris le backlog** dans `.claude/memory/BACKLOG.md` :

   ```markdown
   # Backlog — <projet>

   _Mis à jour : <date>_

   ## 🎯 Jalon en cours : <nom du jalon / sprint>
   <Objectif du jalon en une phrase.>

   | ID | Tâche | Agent pressenti | Taille | Priorité | Statut |
   |---|---|---|---|---|---|
   | T-01 | … | backend-api | M | Must | à faire / en cours / fait / bloqué |

   ## ⏭️ Jalons suivants
   - <Jalon 2> : <contenu en 1-2 lignes>

   ## 🧊 Plus tard / idées
   - <tout ce qui est noté mais non planifié>
   ```

6. **Tiens-le à jour** : à chaque tâche terminée ou décision qui change le plan,
   mets à jour le statut. Le backlog est la source de vérité du « qu'est-ce qu'on fait
   ensuite » ; `ETAT.md` reste l'instantané de la session.

## Règles
- **Jalons courts** : un jalon = quelques jours de travail max, avec un livrable
  démontrable à la fin. Pas de tunnel de trois semaines.
- **Ne planifie pas au-delà de 2 jalons** en détail : le reste va dans « Plus tard ».
- Si l'utilisateur impose une deadline, pars de la deadline et propose ce qui **rentre**,
  plutôt que d'empiler des tâches et de dépasser.
- Signale les risques (dépendance externe, inconnue technique) directement sur la tâche.
- Pour exécuter le backlog, délègue à l'`orchestrateur` jalon par jalon.
