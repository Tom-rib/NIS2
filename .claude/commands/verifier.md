---
description: Scanne un skill, plugin, MCP ou dépôt avec SkillSpector avant installation.
argument-hint: [chemin, URL de dépôt ou .zip — vide = tous les skills du projet]
---

Vérifie la sécurité de la cible avec le skill `verif-skills`.

Cible : $ARGUMENTS

Sans argument, scanne chaque dossier de `.claude/skills/` et rends un tableau
`skill | score | sévérité | verdict`.

Rappel : le score ne décide pas seul. Ouvre chaque finding HIGH/CRITICAL, juge le
contexte réel (l'analyse statique confond les négations), puis conclus en une ligne
par cible. N'installe rien sans l'accord explicite de l'utilisateur.
