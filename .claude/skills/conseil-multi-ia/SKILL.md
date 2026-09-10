---
name: conseil-multi-ia
description: Convoque un « conseil » de plusieurs IA (Claude, GPT, Gemini) pour confronter leurs points de vue sur une question difficile et en tirer une synthèse. À utiliser pour une décision importante, un arbitrage technique, une revue d'idée, ou quand l'utilisateur veut « l'avis de plusieurs IA ». Déclencheurs : « demande à plusieurs IA », « conseil multi-IA », « confronte les avis ».
---

# Conseil multi-IA

Le but : obtenir une **réflexion commune** en interrogeant plusieurs modèles d'IA de
fournisseurs différents, puis synthétiser leurs réponses (accords, désaccords, angle mort).

## Deux modes

### Mode A — Multi-fournisseurs (Claude + GPT + Gemini)
Utilise le script `.claude/scripts/conseil_multi_ia.py`. Il interroge en parallèle chaque
fournisseur **dont la clé API est présente** dans l'environnement, et affiche chaque
réponse côte à côte. Les fournisseurs sans clé sont ignorés proprement.

```bash
python .claude/scripts/conseil_multi_ia.py "Faut-il choisir PostgreSQL ou MongoDB pour <contexte> ?"
```

Clés lues dans l'environnement (voir `.env.example`) :
- `ANTHROPIC_API_KEY` → Claude (`claude-opus-4-8`)
- `OPENAI_API_KEY` → GPT
- `GEMINI_API_KEY` → Gemini

Pré-requis : `pip install anthropic openai google-genai` (chaque paquet n'est requis que
pour le fournisseur correspondant). Si un paquet manque, ce fournisseur est sauté.

Après exécution, **lis les réponses et produis une synthèse** :
1. Points d'**accord** entre les modèles.
2. Points de **désaccord** et pourquoi.
3. Ce qu'un modèle a vu que les autres ont manqué.
4. Ta **recommandation** finale, justifiée.

### Mode B — Conseil interne (sans autres fournisseurs)
Si aucune autre clé n'est disponible, simule un conseil avec plusieurs **personas** via des
sous-agents ou plusieurs angles d'analyse, puis synthétise :
- Un **partisan** (pourquoi c'est une bonne idée),
- Un **sceptique** (risques, failles, cas limites),
- Un **pragmatique** (coût, effort, alternative plus simple).

Confronte les trois et conclus par une recommandation argumentée.

## Quand l'utiliser
- Décision d'architecture ou de stack à fort impact.
- Idée à challenger avant de s'engager.
- Sujet où tu veux réduire le risque d'angle mort d'un seul modèle.

## Posture
La valeur n'est pas dans la juxtaposition des avis, mais dans la **synthèse** : ce que la
confrontation révèle. Termine toujours par une recommandation claire, pas un simple résumé.
