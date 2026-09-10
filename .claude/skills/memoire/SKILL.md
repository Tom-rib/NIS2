---
name: memoire
description: Mémoire de travail persistante. À utiliser pour sauvegarder l'état d'avancement d'une tâche afin de la reprendre dans une session future, ou pour relire ce contexte au démarrage. Déclencheurs typiques : « sauvegarde où on en est », « reprends le travail », « note ça pour plus tard », fin de session de travail.
---

# Mémoire de travail

Cette fonction permet à Claude de **garder le fil entre les sessions**. Le contexte d'une
session Claude Code est éphémère ; cette mémoire le rend persistant via des fichiers
versionnables dans `.claude/memory/`.

## Fichiers de mémoire

- **`.claude/memory/ETAT.md`** — l'instantané du *maintenant* : sur quoi on travaille,
  où on en est, quelle est la prochaine étape. Écrasé/mis à jour à chaque sauvegarde.
- **`.claude/memory/JOURNAL.md`** — l'historique append-only : une entrée datée par session
  ou par étape importante. On ajoute, on ne réécrit pas.
- **`.claude/memory/BACKLOG.md`** — le plan de travail (jalons, tâches, priorités, statuts).
  Géré par le skill `planification` ; à la sauvegarde, vérifie que les statuts sont à jour.
- **`.claude/memory/DECISIONS.md`** — append-only : une ligne par décision structurante
  (contexte → décision → raison). C'est ce qui évite de re-débattre les mêmes choix.
- **`.claude/memory/PREFERENCES.md`** — les manières de travailler de l'utilisateur,
  mémorisées **automatiquement** par le skill `preferences` (à distinguer : ce fichier
  décrit l'utilisateur, pas le projet).

> Au démarrage d'une session, le hook `.claude/scripts/session-start.sh` injecte automatiquement
> ces fichiers dans le contexte. Tu n'as donc pas besoin de les relire manuellement, sauf
> demande explicite de l'utilisateur (« reprends »).

## Sauvegarder le contexte

Quand l'utilisateur demande de sauvegarder (ou en fin de tâche importante) :

1. **Mets à jour `ETAT.md`** avec cette structure :
   ```markdown
   # État courant — <date>

   ## 🎯 Objectif
   <ce qu'on cherche à accomplir, en 1-2 phrases>

   ## ✅ Fait
   - <réalisations clés>

   ## 🚧 En cours
   - <ce qui est commencé mais pas fini>

   ## ⏭️ Prochaine étape
   - <la toute prochaine action concrète à faire>

   ## 📌 À savoir / décisions
   - <choix d'architecture, contraintes, pièges rencontrés, fichiers clés>
   ```

2. **Ajoute une ligne au `JOURNAL.md`** (append, ne pas écraser) :
   ```markdown
   ## <date> — <titre court de la session>
   <2-4 lignes : ce qui a été fait, décisions, point de reprise>
   ```

3. Confirme brièvement à l'utilisateur ce qui a été enregistré.

## Reprendre le travail

Quand l'utilisateur demande de reprendre :

1. Lis `ETAT.md` puis les dernières entrées de `JOURNAL.md`.
2. Résume en 3-4 lignes : objectif, ce qui était fait, et **la prochaine étape**.
3. Propose de reprendre à cette prochaine étape.

## Bonnes pratiques
- Sois **concret** : « la prochaine étape » doit être une action exécutable, pas un vœu.
- Note les **décisions et les pièges**, pas seulement les réussites — c'est ce qui fait
  gagner du temps à la reprise.
- Garde `ETAT.md` court (l'instantané). L'historique long va dans `JOURNAL.md`.
