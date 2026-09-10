# État courant — NIS2 / HydroRégie

## 🎯 Objectif
Produire les 4 livrables de mise en conformité NIS2 pour HydroRégie (régie des eaux,
450 000 habitants, entité essentielle) : qualification réglementaire, analyse d'écart +
feuille de route, architecture réseau segmentée IT/OT, gestion de crise et notifications.
Rendu attendu : dépôt GitHub structuré, exploitable aussi comme cours de révision.

## ✅ Fait (2026-09-10)
- Dépôt initialisé avec le sujet (`NIS2_sujet.md`, `NIS2_sujet.pdf`).
- Outillage Claude Code installé sous `.claude/`.
- **Les 4 livrables sont rédigés** dans `Documentation/` (job-1 à job-4).
- **5 annexes** rédigées : alerte 24 h, notification 72 h, rapport final 1 mois,
  information des usagers, notification CNIL — + registre des écarts en CSV.
- **Cours réglementaire** : 26 fiches dans `Cour/reglementation/`, une par article ou
  groupe d'articles, + quiz de révision de 25 questions.
- **Cours technique** : 10 fiches dans `Cour/technique/` (IT vs OT, Purdue, VLAN, pare-feu,
  DMZ, VPN/bastion, protocoles industriels, détection, sauvegardes, crise).
- **5 fiches pédagogiques racine** : 01_preparation → 05_annexes.
- **Scripts** : VLAN, nftables, WireGuard, OPNsense, test de segmentation, inventaire passif,
  sauvegarde 3-2-1-1-0.
- **Schémas Mermaid** (avant / après / flux de notification) dans `schemas/`.
- **`Documentation.md`** (~2 700 lignes) et **`Documentation.docx`** générés.
- 230 liens internes vérifiés, 0 cassé.

## 🚧 En cours
- —

## ⏭️ Prochaine étape
- **Présentation orale sur Canva** (demandée par l'utilisateur, à faire ensuite).
  Point de départ : le résumé « Le projet en une page » de `Documentation.md`.

## 📌 À savoir / décisions
- 🔴 **La loi française de transposition n'est pas promulguée** (vérifié le 2026-09-10 :
  Sénat 11-12/03/2025, commission spéciale AN 10/09/2025, décrets à venir). Tout le rendu
  s'appuie sur **le texte de la directive**, jamais sur un droit français inexistant.
- Convention de marquage utilisée partout : 📗 texte de la directive · 📙 source officielle ·
  📕 hypothèse de travail construite pour le cas d'école.
- Chiffres HydroRégie retenus (hypothèses) : 380 salariés, 72 M€ de CA, 95 M€ de bilan,
  240 000 abonnés, ~350 automates, 62 communes, ~1 200 km de réseau.
- Architecture : 9 zones, 2 pare-feu en cascade, DMZ industrielle, OPC UA seul protocole
  franchissant une frontière de zone, WireGuard pour les sites distants.
- Scénario de crise daté du 16/03/2027 (après la phase 0 du plan, avant la segmentation) :
  choix délibéré pour montrer ce que les mesures peu coûteuses ont sauvé et ce que la
  segmentation aurait évité.
- Délais réglementaires : alerte précoce 24 h, notification 72 h, **rapport final 1 mois à
  compter de la notification des 72 h** (pas de la découverte).
- `Documentation.md` et `Documentation.docx` sont **générés** par
  `scripts/documentation/` — ne jamais les éditer à la main.
