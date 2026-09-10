---
name: admin-mcp-ssh
description: Administrer des serveurs distants via le serveur MCP `ssh-admin` (outils ssh_list_hosts, ssh_check, ssh_run, ssh_install, ssh_run_tests). À utiliser quand l'utilisateur veut que Claude installe des paquets, lance des tests ou vérifie l'état de SES serveurs via SSH, avec garde-fous. Déclencheurs : « installe X sur mon serveur », « lance les tests sur staging », « vérifie l'état du serveur », « déploie sur la prod ».
---

# Administration distante via MCP `ssh-admin`

Ce skill explique **comment piloter proprement** le serveur MCP `ssh-admin`
(voir `.claude/mcp/ssh-admin/`). Ce MCP fournit les *outils* ; ce skill fournit la *méthode*.

> ⚠️ Prérequis : le MCP doit être installé et configuré
> (`cd .claude/mcp/ssh-admin && npm install`, `cp hosts.example.json hosts.json`, secrets en
> variables d'environnement). Si `ssh_list_hosts` renvoie « aucun hôte », arrête-toi et
> guide l'utilisateur pour la configuration au lieu de deviner.

## 🧭 Méthode (toujours dans cet ordre)

1. **Cadrer la cible.** Appelle `ssh_list_hosts`. Identifie l'alias et l'**environnement**
   (dev / staging / **prod**). En cas de doute sur la bonne machine, demande confirmation.
2. **Diagnostiquer avant d'agir.** `ssh_check host=<alias>` (lecture seule, sans risque)
   pour voir l'état réel avant toute modification.
3. **Tester à blanc.** Pour toute commande qui modifie quelque chose, lance-la d'abord avec
   `dryRun:true` et **montre à l'utilisateur** ce qui serait exécuté.
4. **Agir après feu vert.** N'ajoute `confirm:true` que lorsque l'utilisateur a validé.
   `confirm:true` est **obligatoire** en prod et pour les commandes sensibles.
5. **Vérifier après.** Reste sur `ssh_check` ou une commande de lecture pour confirmer que
   le service tourne et que rien d'autre n'est cassé. `ssh_run_tests` pour valider le code.

## 🚦 Respecter les garde-fous (ne pas les contourner)

- Si un outil renvoie **« Confirmation requise »**, ne relance PAS `confirm:true` de ta
  propre initiative : **remonte le message à l'utilisateur** et attends son accord.
- Si un outil renvoie **« Commande bloquée »** (motif destructeur), n'essaie pas de
  reformuler pour passer outre. Explique le risque et propose une alternative sûre.
- Sur un hôte **lecture seule**, ne tente pas d'action modifiante : c'est voulu.
- Ne mets jamais de secret (mot de passe, clé) dans un argument d'outil : l'auth est gérée
  par la config du MCP (variables d'env / chemin de clé).

## 💡 Recettes courantes

- **Installer un paquet** : `ssh_install host=staging-web packages=["nginx"]`
  → d'abord `dryRun:true`, puis `confirm:true` après validation.
- **Lancer les tests** :
  `ssh_run_tests host=staging-web directory=/srv/app testCommand="npm test"`.
- **Redémarrer un service** (sensible) : `ssh_run host=… command="sudo systemctl restart app"`
  → l'outil exigera `confirm:true`. Confirme la cible avant.
- **Consulter des logs** : `ssh_run host=… command="journalctl -u app -n 100 --no-pager"`
  (lecture seule — passe même sur un hôte readOnly).

## 🤝 Articulation avec le reste du dépôt

- L'agent **`admin-distant`** couvre l'approche SSH « brute » via `Bash` : utilise-le quand
  le MCP n'est pas configuré ou pour des besoins ponctuels hors catalogue.
- Pour la **sécurité** (pare-feu, durcissement, secrets), collabore avec **`devsecops`**.
- Pour des **migrations/BDD lourdes**, délègue à **`architecte-donnees`**.
- Rends compte **fidèlement** : ne déclare « OK » que ce que la sortie réelle confirme.
