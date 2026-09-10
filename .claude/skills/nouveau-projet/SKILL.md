---
name: nouveau-projet
description: Échafaude rapidement un nouveau projet à partir de ce dépôt de base. À utiliser quand l'utilisateur démarre quelque chose de neuf (application, API, projet DevOps, cluster, script, bibliothèque…). Cadre le besoin, propose une architecture, crée la structure et configure les outils. Déclencheurs : « démarre un projet », « nouveau projet », « initialise … ».
---

# Démarrer un nouveau projet

Cette fonction transforme ce dépôt de base en point de départ d'un projet concret, le plus
vite possible mais sans sauter le cadrage.

## Étape 1 — Cadrer (ne pas sauter)
Active d'abord la réflexion (skill `reflexion`). Avant d'écrire le moindre fichier, clarifie :
- **Type de projet** : appli web, API/back, CLI, bibliothèque, projet DevOps/infra, cluster,
  data/ML, autre ?
- **Stack** : imposée ou libre ? Si libre, propose un défaut raisonnable et justifie-le.
- **Cible & échelle** : pour qui, déployé où, quelle volumétrie attendue ?
- **Contraintes** : délais, conformité, existant à respecter.
- **Périmètre du MVP** : le strict nécessaire pour une première version qui tourne.

Propose une valeur par défaut pour chaque point ; l'utilisateur valide ou corrige.

Pour un projet client ou conséquent, formalise le résultat du cadrage avec le skill
`cahier-des-charges` (user stories, critères d'acceptation, hors-périmètre), puis
transforme-le en backlog avec le skill `planification`. Pour un petit projet perso,
un cadrage oral suffit — ne bureaucratise pas.

## Étape 2 — Proposer une architecture
Présente brièvement :
- l'arborescence cible,
- les composants principaux et leurs responsabilités,
- les choix techniques clés (et pourquoi),
- ce qui est volontairement reporté.

Demande le feu vert avant de générer.

## Étape 3 — Échafauder
Délègue à l'`orchestrateur` qui répartit entre les spécialistes selon le type de projet :
- structure de code + config de base,
- `frontend-uiux` / `backend-api` / `architecte-donnees` selon les besoins,
- `devops-cloud` pour Docker/CI/déploiement, `devsecops` pour le durcissement initial,
- `qa-testing` pour mettre en place le harnais de test,
- `redacteur-docs` pour un README de démarrage.

Mets en place dès le départ :
- un fichier d'outillage (lint/format) et une commande de test qui passe,
- un `.gitignore` adapté + `.env.example` (jamais de `.env`),
- un pipeline CI minimal (lint + test),
- un premier commit propre.

## Étape 4 — Mémoriser
Enregistre l'objectif et la prochaine étape via le skill `memoire` (`ETAT.md` + `JOURNAL.md`),
et le plan de travail dans `BACKLOG.md` si un backlog a été créé, pour pouvoir reprendre
facilement.

## Étape 5 — La suite du cycle de vie
Une fois le projet échafaudé, le travail courant suit les skills dédiés :
`cycle-dev` pour chaque fonctionnalité, `livraison` pour publier une version,
`rapport-avancement` pour faire le point, `incident` si quelque chose casse.

## Principes
- **MVP d'abord** : la chose la plus simple qui tourne, puis on itère.
- Pas de sur-ingénierie : pas d'abstraction pour des besoins hypothétiques.
- Sécurité dès le départ : secrets en variables d'env, dépendances à jour.
- Laisse le projet dans un état **exécutable et testé** à la fin du bootstrap.
