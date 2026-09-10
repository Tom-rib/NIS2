# Journal de travail

> Historique en ajout seulement. Une entrée par session ou étape importante.
> Rempli par le skill `memoire` (`/sauver-contexte`).

## 2026-09-10 — Initialisation du dépôt NIS2
Outillage complet copié depuis le template `Claude-skills-agents` et rangé sous `.claude/`
(agents, skills, commandes, mémoire, scripts, MCP ssh-admin, guides). Chemins réécrits en
conséquence dans `settings.json`, `.mcp.json`, `.gitignore` et les skills.
Point de reprise : cadrer les 4 blocs du cas HydroRégie (`/reflechir`, puis `/planifier`).

## 2026-09-10 — Rendu complet des 4 blocs + cours + document unique
Construction de l'intégralité du dépôt de rendu, pensé comme un mini-cours réutilisable.

**Produit**
- `Documentation/` : job-1 (qualification), job-2 (analyse d'écart + feuille de route 24 mois),
  job-3 (architecture segmentée IT/OT), job-4 (chronologie de crise), + 5 annexes de
  notifications rédigées et un registre des écarts CSV.
- `Cour/reglementation/` : 26 fiches, une par article ou groupe d'articles + quiz de 25 questions.
- `Cour/technique/` : 10 fiches (IT vs OT, Purdue, VLAN, pare-feu, DMZ, VPN/bastion,
  protocoles industriels, détection, sauvegardes, gestion de crise).
- Fiches racine 01 à 05, `scripts/` (VLAN, nftables, WireGuard, OPNsense, tests, inventaire
  passif, sauvegarde), `schemas/` (Mermaid avant/après/notification).
- `Documentation.md` (~2 700 lignes) et `Documentation.docx`, générés par
  `scripts/documentation/` (python-docx ; pandoc absent de la machine).

**Vérifications faites**
- Numérotation des articles 36 à 45 vérifiée en ligne (erreur initiale corrigée :
  art. 40 = Réexamen, 41 = Transposition, 42 = eIDAS, 43 = 2018/1972, 44 = Abrogation).
- Énumérations des art. 21(2) et 23(4) recoupées avec une source externe.
- État de la transposition française vérifié auprès de la FAQ MonEspaceNIS2 : **non achevée**.
- 230 liens internes contrôlés automatiquement, 0 cassé.

**Point de reprise** : la présentation orale sur Canva.
