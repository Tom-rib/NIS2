# Mémoire de travail

Ce dossier contient la **mémoire persistante** de Claude entre les sessions (skill `memoire`).

- **`ETAT.md`** — instantané du travail courant (objectif, fait, en cours, prochaine étape).
  Mis à jour à chaque sauvegarde.
- **`JOURNAL.md`** — historique daté, en ajout seulement (append-only).
- **`BACKLOG.md`** — plan de travail : jalons, tâches, priorités, statuts
  (skill `planification`, commande `/planifier`).
- **`DECISIONS.md`** — journal append-only des décisions structurantes
  (contexte → décision → raison).
- **`PREFERENCES.md`** — manières de travailler de l'utilisateur, enregistrées
  automatiquement (skill `preferences`, commande `/preferences`). Décrit l'utilisateur,
  pas le projet : ce fichier se transporte d'un projet à l'autre.

Au démarrage d'une session, `.claude/scripts/session-start.sh` injecte ces fichiers dans le
contexte de Claude pour qu'il puisse reprendre le fil.

Pour mettre à jour : commande `/sauver-contexte`. Pour reprendre : `/reprendre`.

> Astuce : versionne `ETAT.md` et `JOURNAL.md` si tu veux partager l'avancement avec ton
> équipe. Les fichiers `session-*.md` (mémoire locale temporaire) sont, eux, ignorés par git.
