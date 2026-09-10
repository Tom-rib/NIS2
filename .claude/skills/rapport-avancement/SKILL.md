---
name: rapport-avancement
description: Produit un rapport d'avancement clair et honnête, comme pour un client ou un manager — réalisé, en cours, risques, prochaines étapes, décisions attendues. À utiliser en fin de session de travail, avant une démo, ou quand l'utilisateur demande « où en est-on ? ». Déclencheurs : « fais le point », « rapport d'avancement », « où en est le projet », « prépare la démo ».
---

# Rapport d'avancement

Un client ne lit pas les commits : il veut savoir où en est son projet, ce qui le menace,
et ce qu'on attend de lui. Ce skill produit ce compte-rendu.

## Méthode

1. **Rassemble les faits** : backlog (`.claude/memory/BACKLOG.md`), état
   (`ETAT.md`), journal (`JOURNAL.md`), historique git récent (`git log`), état des
   tests. Ne te fie pas à ta seule mémoire de session.

2. **Rédige le rapport** — directement dans la conversation par défaut, ou dans
   `docs/projet/rapports/<date>.md` si l'utilisateur veut un livrable :

   ```markdown
   # Point d'avancement — <projet> — <date>

   ## 🟢 En une phrase
   <L'état du projet, compréhensible par un non-technicien.>

   ## ✅ Réalisé depuis le dernier point
   <Livrables démontrables, formulés côté utilisateur : « la connexion fonctionne »,
   pas « refactoring du middleware d'auth ».>

   ## 🚧 En cours
   <Ce qui est commencé, et à quel stade.>

   ## ⚠️ Risques & points d'attention
   <Ce qui pourrait retarder ou coûter. Chaque risque avec sa parade envisagée.>

   ## ⏭️ Prochaines étapes
   <Les 2-4 prochaines actions concrètes, dans l'ordre.>

   ## ❓ Décisions attendues
   <Ce que le client doit trancher pour ne pas bloquer l'équipe. Vide = le dire.>
   ```

3. **Si une démo est demandée** : vérifie que le projet se lance réellement, prépare le
   scénario (3-5 étapes qui montrent la valeur), et signale ce qu'il ne faut PAS montrer
   (parties instables).

## Règles
- **Honnêteté avant tout** : un retard annoncé tôt est un problème géré ; un retard
  masqué est une crise. Ne « verdit » jamais un point qui est orange.
- Langage client : parle en fonctionnalités et en risques, pas en jargon technique.
  Le détail technique va en annexe si nécessaire.
- Chiffres réels : « 34 tests, tous verts », « 8 tâches sur 12 du jalon », pas « ça
  avance bien ».
- Termine la session par une mise à jour de la mémoire (skill `memoire`) pour que le
  prochain rapport soit facile à produire.
