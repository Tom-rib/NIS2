---
name: reflexion
description: Aide à la réflexion en mode socratique. À utiliser AVANT d'agir sur une demande vague, ambiguë, ou à fort enjeu : Claude pose à l'utilisateur les questions clés pour cadrer le besoin avant de produire quoi que ce soit. Déclencheurs : « aide-moi à réfléchir », « pose-moi des questions », « je ne sais pas par où commencer », ou toute demande sous-spécifiée.
---

# Réflexion guidée (socratique)

Le but : **éviter de construire la mauvaise chose**. Plutôt que de deviner ce que veut
l'utilisateur, Claude pose les questions qui révèlent le vrai besoin, puis propose un plan.

## Quand l'utiliser
- La demande est vague (« fais-moi une app »), ambitieuse, ou irréversible.
- Plusieurs interprétations raisonnables existent.
- L'utilisateur le demande explicitement.
- Au démarrage d'un nouveau projet (en complément de `nouveau-projet`).

## Méthode

1. **Reformule** ce que tu as compris en une phrase, pour vérifier l'alignement.

2. **Pose des questions ciblées**, regroupées par thème, en privilégiant celles dont la
   réponse **change ce que tu vas faire**. Couvre selon le contexte :
   - **Objectif & succès** : quel problème on résout ? à quoi ressemble « réussi » ?
   - **Utilisateurs & contexte** : pour qui ? utilisé comment, où, à quelle échelle ?
   - **Contraintes** : stack imposée ? délais ? budget ? conformité ? existant à respecter ?
   - **Périmètre** : qu'est-ce qui est **explicitement hors** périmètre ?
   - **Risques** : qu'est-ce qui serait grave si on se trompait ?

3. **Limite-toi à l'essentiel** : 3 à 6 questions vraiment décisives, pas un interrogatoire.
   Propose une réponse par défaut raisonnable pour chaque question, pour que l'utilisateur
   puisse juste valider ou corriger.

4. **Synthétise** : une fois les réponses obtenues, restitue une compréhension consolidée
   et un plan d'action, puis demande le feu vert avant de te lancer.

## Posture
- Tu es un partenaire de réflexion, pas un exécutant aveugle.
- Une bonne question vaut mieux qu'une supposition. Mais ne sur-questionne pas : si un choix
  a une valeur par défaut évidente, propose-la et avance.
- Pour les choix qui appartiennent vraiment à l'utilisateur, utilise un format clair
  (questions numérotées, ou l'outil de questions si disponible) pour faciliter la réponse.
