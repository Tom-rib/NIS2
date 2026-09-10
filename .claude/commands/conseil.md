---
description: Convoque le conseil multi-IA (Claude + GPT + Gemini) sur une question, puis synthétise.
argument-hint: [la question à soumettre au conseil]
---

Active le skill `conseil-multi-ia` sur la question ci-dessous.

Si des clés API d'autres fournisseurs sont disponibles, lance
`python .claude/scripts/conseil_multi_ia.py "$ARGUMENTS"` puis produis la synthèse.
Sinon, utilise le mode B (conseil interne par personas) et synthétise.

Question : $ARGUMENTS
