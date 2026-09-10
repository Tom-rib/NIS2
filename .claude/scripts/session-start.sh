#!/usr/bin/env bash
# Hook SessionStart : au démarrage d'une session Claude Code, charge la mémoire
# de travail (s'il y en a une) pour que Claude puisse reprendre le fil.
#
# La sortie de ce script est injectée dans le contexte de Claude.

set -euo pipefail

JOURNAL=".claude/memory/JOURNAL.md"
ETAT=".claude/memory/ETAT.md"
BACKLOG=".claude/memory/BACKLOG.md"
PREFERENCES=".claude/memory/PREFERENCES.md"

if [[ -f "$ETAT" ]] || [[ -f "$JOURNAL" ]]; then
  echo "## 🧠 Mémoire de travail rechargée"
  echo ""
  if [[ -f "$PREFERENCES" ]]; then
    echo "### Préférences de travail de l'utilisateur (.claude/memory/PREFERENCES.md)"
    echo ""
    echo "_Applique ces préférences d'office. Mets ce fichier à jour automatiquement"
    echo "dès qu'une préférence est exprimée ou qu'une façon de faire est corrigée"
    echo "(skill \`preferences\`)._"
    echo ""
    cat "$PREFERENCES"
    echo ""
  fi
  if [[ -f "$ETAT" ]]; then
    echo "### État courant (.claude/memory/ETAT.md)"
    echo ""
    cat "$ETAT"
    echo ""
  fi
  if [[ -f "$BACKLOG" ]]; then
    echo "### Backlog (.claude/memory/BACKLOG.md)"
    echo ""
    # Affiche le début du backlog (jalon en cours) pour rester concis.
    head -n 30 "$BACKLOG"
    echo ""
  fi
  if [[ -f "$JOURNAL" ]]; then
    echo "### Dernières entrées du journal"
    echo ""
    # Affiche les 40 dernières lignes du journal pour rester concis.
    tail -n 40 "$JOURNAL"
    echo ""
  fi
  echo "_Pour mettre à jour : skill \`memoire\` ou commande \`/sauver-contexte\`._"
else
  echo "## 🧠 Mémoire de travail vide"
  echo "Aucun contexte sauvegardé. Utilise \`/sauver-contexte\` pour en créer un."
fi
