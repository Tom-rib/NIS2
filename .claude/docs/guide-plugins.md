# Guide plugins & skills externes — analysés avant intégration

Règle de la maison : **on n'ajoute rien sans avoir lu le code** (scripts, hooks,
appels réseau) et **on n'ajoute pas ce qui fait doublon** avec l'existant.
Ce guide consigne les analyses faites et les verdicts.

## ✅ Intégré : `ui-ux-pro-max` (skill embarqué)

**Quoi** : base de connaissances design interrogeable — 50+ styles UI, 161 palettes,
57 accords typographiques, 99 guidelines UX, 25 types de graphiques, 10 stacks.
Copié dans `.claude/skills/ui-ux-pro-max/` ; l'agent `frontend-uiux` la consulte
avant toute décision de design.

**Analyse de risque (v2.6.2, licence MIT)** : ✅ **sain**
- Scripts Python en bibliothèque standard uniquement (csv, json, re) : recherche
  locale dans des CSV. **Aucun appel réseau, aucun subprocess, aucun eval.**
- Le dépôt d'origine contient d'autres skills (design-system, ui-styling…) dont
  certains scripts téléchargent des images (Pexels) ou lancent `npx shadcn` :
  **volontairement non embarqués** pour garder le modèle sans effet de bord.

**Usage** :
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "saas dashboard" --design-system -p "Mon Projet"
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
```

## 🟡 Disponible mais non activé : `claude-mem` (plugin)

**Quoi** : mémoire persistante automatique — compresse les transcripts en
« observations » dans une base SQLite locale, worker en arrière-plan, viewer web,
~20 skills embarqués. Marketplace déjà déclarée dans `settings.json` ; pour l'essayer :
`/plugin install claude-mem@thedotmack`.

**Analyse de risque (v13.10.2, Apache-2.0)** : 🟡 **légitime mais lourd**
- Projet sérieux (SECURITY.md, maintenance active), pas de code malveillant détecté.
- MAIS : hooks sur chaque prompt + worker Node persistant lancé à chaque session ;
  **télémétrie PostHog activée par défaut** (anonyme et filtrée — OS, version,
  compteurs — pas le contenu ; désactivable : `claude-mem telemetry off`) ;
  peut router la compression vers des LLM tiers (DeepSeek, OpenRouter…) **si**
  on le configure ainsi.

**Pourquoi non activé : doublon.** Ce dépôt a déjà une mémoire (`memoire` +
`preferences` : ETAT, JOURNAL, BACKLOG, DECISIONS, PREFERENCES) — versionnée dans
git, partageable en équipe, lisible. claude-mem est une mémoire **personnelle,
locale et automatique** : les deux injecteraient chacune leur contexte à chaque
session. Choisis : garde la mémoire du dépôt (défaut), ou installe claude-mem et
désactive le hook `session-start.sh` pour éviter la double injection.

## 🟡 Disponible mais non activé : `superpowers` (plugin)

**Quoi** : bibliothèque de skills réputée (brainstorming, plans, TDD, débogage
cause-racine…). Marketplace déclarée ; pour l'essayer :
`/plugin install superpowers@superpowers-marketplace`.

**Pourquoi non activé : doublon partiel.** Ses workflows (brainstorm → plan →
implémentation TDD) recouvrent `reflexion`, `planification` et `cycle-dev` — deux
doctrines concurrentes qui se déclencheraient en même temps. À tester si tu veux
comparer, mais pas les deux en même temps sur un vrai projet.

## ❌ Écartés : doublons avérés

| Demandé | Pourquoi écarté |
|---|---|
| `code-review` (plugin) | Claude Code embarque déjà `/code-review`, et le dépôt a l'agent `reviseur-code` + l'étape revue de `cycle-dev` |
| `security-review` (plugin) | `/security-review` intégré + agent `devsecops` |
| `frontend-design` (plugin) | Rôle couvert par `ui-ux-pro-max` (embarqué) + agent `frontend-uiux` |
| « stack » | Couvert : `ui-ux-pro-max` inclut les guidelines par stack (`data/stacks/`, option `--stack` de la recherche) |

## Méthode pour évaluer un skill/plugin externe

1. **Cloner et lire** : `SKILL.md`, `hooks.json`, scripts. Chercher réseau
   (`requests`, `fetch`, URLs), exécution (`subprocess`, `os.system`, `eval`),
   accès hors projet (`~/`, chemins absolus), télémétrie.
2. **Se méfier particulièrement des hooks** : ils s'exécutent automatiquement,
   sans confirmation, à chaque session/prompt.
3. **Vérifier le doublon** : qu'apporte-t-il que les agents/skills/MCP existants
   ne font pas ?
4. **Consigner le verdict ici**, puis intégrer (skill copié ou plugin activé)
   seulement si sain et non redondant.
