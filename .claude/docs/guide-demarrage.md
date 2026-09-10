# Guide de démarrage — utiliser ce dépôt comme base

## 1. Cloner comme point de départ

```bash
git clone <ce-depot> mon-projet
cd mon-projet
rm -rf .git && git init        # repartir d'un historique vierge (optionnel)
```

## 2. (Optionnel) Configurer le conseil multi-IA

```bash
cp .env.example .env
# Renseigne les clés que tu possèdes (Anthropic, OpenAI, Gemini).
pip install anthropic openai google-genai   # selon les fournisseurs voulus
```

Le fichier `.env` est ignoré par git (voir `.gitignore`) — il ne sera jamais commité.

## 3. Démarrer un projet

Dans Claude Code :

```
/nouveau-projet une API de gestion de tâches avec authentification
```

Claude va :
1. te poser quelques questions de cadrage (stack, cible, périmètre du MVP),
2. proposer une architecture et demander ton feu vert,
3. échafauder la structure via les agents spécialisés (back, data, devops, tests…),
4. mettre en place lint + tests + CI + README,
5. enregistrer l'état dans la mémoire.

## 4. Travailler au quotidien

- **Déléguer** : « demande au `frontend-uiux` de créer la page de connexion ».
- **Réviser** : « fais relire le module d'auth par le `reviseur-code` ».
- **Déboguer** : « ce test échoue, lance le `debugger` ».
- **Sécuriser** : « audit de sécurité avec `devsecops` avant le déploiement ».
- **Décider** : `/conseil PostgreSQL ou MongoDB pour ce cas ?`
- **Apprendre** : « `formateur`, fais-moi un cours sur Kubernetes ».

## 5. Sauvegarder et reprendre

En fin de session :
```
/sauver-contexte
```
À la session suivante, la mémoire est rechargée automatiquement ; pour reprendre :
```
/reprendre
```

## 6. Adapter le modèle à tes besoins

- Ajoute/édite des agents, skills, commandes — voir `docs/guide-agents.md`.
- Ajuste les permissions et hooks dans `.claude/settings.json`.
- Mets à jour `CLAUDE.md` avec les conventions propres à ton projet.

## Rappels de sécurité
- Jamais de secret dans le code ou le dépôt : tout en variables d'environnement.
- `git push` sur `main` seulement sur demande explicite ; travaille sur des branches.
- Avant de livrer : lance les tests et le linter, et signale honnêtement les échecs.
