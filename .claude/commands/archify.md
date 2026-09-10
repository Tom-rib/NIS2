---
description: Génère un diagramme d'architecture, de workflow, de séquence, de flux de données ou de cycle de vie, en HTML autonome interrogeable.
---

Utilise le skill `archify` (`.claude/skills/archify/SKILL.md`) pour produire un diagramme
validé à partir de : $ARGUMENTS

## Marche à suivre

1. **Choisis le type** parmi `architecture`, `workflow`, `sequence`, `dataflow`, `lifecycle`.
   Si la demande est ambiguë, demande — un mauvais type se voit tout de suite au rendu.

2. **Si le diagramme doit refléter du code réel**, ne lis pas les fichiers à l'aveugle :
   - `graphify-out/graph.json` existe → interroge le graphe (`/graphify query "..."`)
     pour obtenir les nœuds centraux et les dépendances réelles, puis convertis en JSON IR.
   - sinon → lance `/graphify .` d'abord, ou travaille à partir de la description de l'utilisateur.
   ⚠️ Une arête `INFERRED` du graphe n'est pas un fait : vérifie dans le code avant de la
   dessiner comme une dépendance réelle. Un diagramme faux est pire qu'une absence de diagramme.

3. **Écris le candidat JSON** avant d'inspecter quoi que ce soit d'autre. Au plus 12 nœuds
   principaux, un chemin principal clair, `meta.quality_profile: "showcase"`.

4. **Valide, puis livre** (depuis `.claude/skills/archify/`) :

   ```bash
   node .claude/skills/archify/bin/archify.mjs validate <type> <candidat.json> --quality showcase --json
   node .claude/skills/archify/bin/archify.mjs deliver  <type> <candidat.json> <sortie.html> --quality showcase --json
   ```

   Une sortie non nulle n'est jamais un succès. En cas d'échec, corrige uniquement le
   `subject` diagnostiqué et relance. Si deux tours consécutifs n'améliorent pas le compte
   d'erreurs, arrête et signale honnêtement ce qui reste.

5. **Range la sortie** dans `docs/diagrammes/` (crée le dossier au besoin), pas à la racine.

## À savoir

- Le skill est **vendu dans le dépôt** (`.claude/skills/archify/`), sans dépendance runtime :
  `bin/archify.mjs` n'importe que des modules `node:` natifs. Rien à installer, Node ≥ 18 suffit.
- Le HTML généré **charge ses polices depuis Google Fonts**. Quiconque ouvre le diagramme est
  donc vu par Google, avec repli sur la police système si le réseau est coupé. À savoir avant
  de diffuser un diagramme hors de l'organisation.
- Le rappel automatique de mise à jour (SKILL.md § « Update awareness ») est neutralisé par
  `ARCHIFY_UPDATE_CHECK_DISABLED=1` dans `.claude/settings.json`. Pour vérifier les mises à
  jour, fais-le explicitement, à la main.
