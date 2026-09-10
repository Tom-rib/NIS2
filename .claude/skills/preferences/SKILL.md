---
name: preferences
description: Mémoire persistante des habitudes et préférences de travail de l'utilisateur, qui s'enregistre AUTOMATIQUEMENT — sans qu'il le demande. À activer dès que l'utilisateur exprime une préférence (« je préfère… », « utilise plutôt… », « toujours/jamais… »), corrige une façon de faire, refait le même choix plusieurs fois, ou demande « souviens-toi que… ». Aussi pour consulter ou nettoyer les préférences mémorisées.
---

# Préférences de travail (mémoire automatique)

Un bon collaborateur n'a pas besoin qu'on lui répète trois fois la même chose. Ce skill
capture les **manières de travailler** de l'utilisateur dans
`.claude/memory/PREFERENCES.md`, chargé automatiquement à chaque session.

## Ce qui déclenche un enregistrement (sans demande explicite)

Enregistre une préférence dès que tu observes :
1. **Une préférence exprimée** : « je préfère X », « utilise plutôt Y », « toujours Z »,
   « jamais W », « souviens-toi que… ».
2. **Une correction de ta façon de faire** : l'utilisateur reformule ta sortie, te fait
   refaire quelque chose autrement, ou te reprend sur la forme (ton, longueur, langue,
   style de code, workflow). La correction vaut préférence.
3. **Un choix répété** : le même arbitrage revient pour la 2e ou 3e fois (même stack,
   même hébergeur, même structure). Note-le pour ne plus reposer la question.

Ne demande pas la permission d'enregistrer : fais-le, puis signale-le en **une ligne**
en fin de réponse (« 📌 Noté dans tes préférences : … »). Si l'utilisateur conteste,
retire la ligne aussitôt.

## Comment enregistrer

1. Ouvre `.claude/memory/PREFERENCES.md` et ajoute la préférence **dans la bonne
   section** (Communication, Stack & outils, Style de code, Workflow, À ne pas faire).
2. Une préférence = **une puce courte, actionnable, datée** :
   `- Préfère PostgreSQL par défaut pour les nouvelles applis (2026-07-06)`
3. **Pas de doublon** : si une préférence proche existe, mets-la à jour (et à jour la
   date) plutôt que d'empiler. Si une nouvelle contredit une ancienne, la nouvelle
   **remplace** l'ancienne.
4. Reste factuel : note ce que l'utilisateur a montré ou dit, pas des suppositions.

## Ce qu'il ne faut PAS enregistrer
- Les choix **propres à un projet** (ils vont dans `DECISIONS.md` du projet).
- Les demandes ponctuelles (« pour cette fois, fais court ») — une occurrence n'est
  pas une habitude, sauf formulation en « toujours/jamais ».
- Tout secret, donnée personnelle sensible, ou détail d'infrastructure confidentiel.

## Utiliser les préférences
- Elles sont injectées au démarrage par `.claude/scripts/session-start.sh` : **applique-les
  d'office**, sans les rappeler à l'utilisateur.
- En cas de conflit entre une préférence mémorisée et une demande explicite du moment,
  la demande du moment gagne (et si elle se répète, elle devient la nouvelle préférence).

## Consulter / nettoyer
Sur demande (« montre mes préférences », « oublie ça ») : affiche le fichier par
sections, supprime ou corrige ce que l'utilisateur désigne.
