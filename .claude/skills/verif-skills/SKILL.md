---
name: verif-skills
description: Scanne un skill, un plugin, un serveur MCP ou un dépôt avec SkillSpector (NVIDIA) avant de l'installer — prompt injection, exfiltration de données, escalade de privilèges, risques chaîne d'appro. À utiliser AVANT toute installation d'extension, et pour auditer périodiquement les skills déjà en place. Déclencheurs : « vérifie ce skill », « c'est safe ? », « scanne ce dépôt », « avant d'installer », « audit sécurité des skills ».
---

# Vérification de sécurité des skills (SkillSpector)

Un skill, c'est du texte que Claude exécute avec les droits de l'utilisateur. Un
`SKILL.md` malveillant n'a pas besoin de code : quelques phrases suffisent à faire
exfiltrer un `.env` ou contourner une confirmation. SkillSpector (NVIDIA, Apache-2.0)
scanne ce texte et le code qui l'accompagne **avant** l'installation.

## Commandes

```bash
skillspector scan <chemin|URL|zip> --no-llm            # analyse statique, hors ligne
skillspector scan <cible> --no-llm --format json --output rapport.json
skillspector scan <cible> --no-llm --format markdown --output rapport.md
skillspector baseline <cible> -o .skillspector-baseline.yaml   # fige les faux positifs
skillspector scan <cible> --baseline .skillspector-baseline.yaml
```

La cible peut être un dossier (`.claude/skills/mon-skill/`), un fichier `SKILL.md`,
une **URL de dépôt GitHub** (scan avant clonage — c'est le cas d'usage principal) ou
un `.zip`.

## Lire le résultat

| Score | Sévérité | Verdict SkillSpector |
|---|---|---|
| 0–20 | LOW | SAFE |
| 21–50 | MEDIUM | CAUTION |
| 51–80 | HIGH | DO_NOT_INSTALL |
| 81–100 | CRITICAL | DO_NOT_INSTALL |

Barème : CRITICAL +50, HIGH +25, MEDIUM +10, LOW +5, ×1,3 si le skill embarque des
scripts exécutables. En JSON, tout est dans `risk_assessment` et `issues[]`.

## Règle d'usage — le score ne décide pas à ta place

En mode `--no-llm` l'analyse est **statique** (regex, AST, YARA) : elle ne comprend pas
le sens des phrases et produit de vrais faux positifs. Constaté sur ce dépôt : le skill
`graphify` sort à 63/100 « DO_NOT_INSTALL » à cause de la phrase *« ne jamais lancer la
visualisation sans prévenir l'utilisateur »* — le motif « Anti-Refusal » a matché
« sans prévenir » en ignorant la négation.

Donc, systématiquement :
1. Lance le scan.
2. **Ouvre chaque finding HIGH/CRITICAL** (`code_snippet`, `explanation`) et juge le
   contexte réel.
3. Rends un verdict en une ligne : ce que ça fait, ce que ça touche, ce qui sort de la
   machine — puis demande l'accord de l'utilisateur.
4. Les faux positifs confirmés vont dans un `baseline`, jamais dans un `--no-verify`
   mental. Ce qui est mis en baseline doit être justifié par écrit.

Ne jamais bloquer une installation sur le seul score, ni la valider sur le seul score.

## Quand l'utiliser
- **Obligatoire** avant tout `npx skills add`, `/plugin install`, ajout dans `.mcp.json`
  ou copie d'un `SKILL.md` trouvé en ligne (voir skill `chercher-extensions`, étape 3).
- Après mise à jour d'un skill tiers (le contenu change sans que le nom bouge).
- En audit périodique : scanner l'ensemble de `.claude/skills/`.

## Analyse sémantique (optionnelle)
Sans clé API, les trois analyseurs LLM sont sautés — c'est le mode par défaut ici, et
il est gratuit et hors ligne. Pour activer la couche sémantique (celle qui écarte les
faux positifs ci-dessus) :

```bash
export SKILLSPECTOR_PROVIDER=anthropic
export ANTHROPIC_API_KEY=...    # facturé à l'usage, hors abonnement
```

Un Ollama local fait aussi l'affaire (`SKILLSPECTOR_PROVIDER=openai`,
`OPENAI_BASE_URL=http://localhost:11434/v1`). Détails : `.claude/docs/guide-skillspector.md`.

## Limites à connaître
- Le scan porte sur le **contenu du skill**, pas sur les dépendances qu'il installe
  ensuite : un `SKILL.md` propre peut appeler un paquet npm/PyPI vérolé. La vérification
  de la chaîne d'appro reste manuelle (cf. audit de `graphify` dans le JOURNAL).
- Un dépôt scanné puis cloné plus tard a pu changer entre-temps : scanner le commit
  qu'on installe réellement.
- Statut du projet amont : `Development Status :: 3 - Alpha`. Utile, pas infaillible.
