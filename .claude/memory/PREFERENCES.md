# Préférences de travail — (s'enrichit automatiquement)

> Ce fichier mémorise **comment l'utilisateur aime travailler**. Il est chargé à chaque
> démarrage de session et mis à jour automatiquement par le skill `preferences` dès
> qu'une préférence est exprimée, qu'une façon de faire est corrigée, ou qu'un choix
> se répète. Une préférence = une puce, avec la date entre parenthèses.

## 💬 Communication
_Ex. : réponses courtes d'abord puis détail ; toujours en français ; tutoiement._
- Réponses et documentation en français, identifiants de code en anglais (défaut du dépôt).

## 🛠️ Stack & outils favoris
_Ex. : préfère PostgreSQL à MongoDB ; déploie sur un VPS OVH ; utilise pnpm._
- **Open source par défaut.** Privilégier systématiquement les briques sous licence
  approuvée OSI, et reléguer tout service payant ou propriétaire derrière un connecteur
  enfichable désactivé. Vérifier la licence réelle plutôt que la réputation : Redis,
  Vault, Terraform et Sentry sont passés en licences non OSI après leur adoption
  massive — prendre les forks communautaires (Valkey, OpenBao, OpenTofu, GlitchTip).
  Ne pas prétendre que tout est gratuit : nommer les exceptions incompressibles
  (modèles LLM frontier, encaissement) plutôt que les masquer. (2026-08-30)

## ✍️ Style de code
_Ex. : commentaires rares mais utiles ; pas de one-liners cryptiques ; tests d'abord._
- —

## 🔁 Workflow & process
_Ex. : veut valider l'architecture avant tout code ; commits petits et fréquents ;
préfère fusionner lui-même les PR._
- Sur les projets à soutenance (ex. Ansible) : il exécute lui-même les commandes dans
  le terminal pour pouvoir faire ses captures d'écran. Fournir des blocs à copier-coller
  prêts à l'emploi, ne pas lancer les playbooks via le MCP `ssh-admin` à sa place.
  (2026-07-21)
- Dans tout ce qui sera lu par un tiers (portfolio, CV, README) : privilégie l'honnêteté
  à l'esbroufe — niveaux de compétence assumés et adossés à une preuve, liste courte
  d'objectifs réels plutôt qu'un catalogue d'intentions (2026-07-22).
- Un projet = son propre dépôt. Ne jamais construire un projet à l'intérieur du dépôt
  template `Claude-skills-agents` : il se retrouve commité dedans et contamine toutes
  les copies suivantes (constaté avec Ansible_Projet puis le portfolio, 2026-07-22).
- Toute extension (skill, plugin, MCP) doit être **scannée avec SkillSpector avant
  installation** (`/verifier`), y compris celles que Claude propose lui-même. Corollaire
  posé le même jour : on ne se fie pas au score brut — les findings HIGH se lisent un par
  un, et les faux positifs se figent dans un baseline justifié par écrit (2026-08-30).
  Méthode corrigée le 2026-09-08 après vérification : le baseline **n'est pas auto-chargé**
  (`skillspector scan <cible> --baseline <fichier>`, sinon on croit à une régression), et
  les **règles glob écrites à la main n'ont aucun effet** — seules les empreintes générées
  par `skillspector baseline` mordent. Générer avec la CLI, puis préfixer le fichier de la
  justification manuelle. Pour supprimer le bruit à la source plutôt que le masquer :
  `SKILLSPECTOR_PROVIDER=claude_cli` fait tourner les analyseurs LLM sur la session Claude
  Code locale, sans clé API facturée.
- Un dépôt vanté comme « économiseur de tokens » s'évalue sur ce qu'il fait réellement, pas
  sur son argumentaire : dire franchement quand la prémisse est fausse plutôt que d'installer
  pour faire plaisir. Et une brique qui ferait transiter le code vers des tiers ne s'installe
  jamais sans arbitrage explicite, même demandée (constaté sur OmniRoute, 2026-09-08).
- Mais un nouveau dépôt doit **embarquer tout l'outillage** du template, pas seulement
  le contenu métier : agents, skills, commandes, mémoire, hook `session-start.sh`,
  `.mcp.json` et un `CLAUDE.md` propre au projet. Le projet doit être reprenable seul.
  Ranger cet outillage sous `.claude/` pour que la racine ne montre que le rendu
  (oubli constaté au démarrage du projet Terraform, 2026-07-28).

## 🚫 À ne pas faire
_Ex. : ne jamais toucher au dossier legacy/ ; pas d'emojis dans les commits._
- —
