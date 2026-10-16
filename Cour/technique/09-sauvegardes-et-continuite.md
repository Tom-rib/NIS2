# 09 — Sauvegardes et continuité

> 🎯 **Objectif** : garantir que **l'eau continue de couler** même quand tout l'informatique est
> arrêté, et pouvoir tout reconstruire.
> ⏱️ 7 minutes. **La mesure qui sauve, art. 21(2)(c).**

---

## 1. Les deux questions à se poser

| Question | Notion | Chez HydroRégie 📕 |
|---|---|---|
| Combien de temps puis-je rester sans ce système ? | **RTO** (*Recovery Time Objective*) | SCADA : **4 h** · ERP : 72 h · Portail abonnés : 5 jours |
| Combien de données puis-je me permettre de perdre ? | **RPO** (*Recovery Point Objective*) | Historian : **1 h** · Programmes automates : **0** (versionnés) · ERP : 24 h |

> 💡 Le RTO et le RPO ne se décident **pas** par la DSI : ce sont des **choix de direction**
> (art. 20(1)), car ils déterminent le budget.

## 2. La règle 3-2-1 (et sa version durcie)

```
3 copies des donnees
2 supports de nature differente
1 copie HORS SITE et HORS LIGNE     <-- la seule qui resiste a un rancongiciel
```

Version durcie, dite **3-2-1-1-0** :

| Chiffre | Exigence |
|---|---|
| **3** | copies |
| **2** | supports différents |
| **1** | hors site |
| **1** | **hors ligne ou immuable** (WORM) |
| **0** | **erreur au dernier test de restauration** |

> 🔴 **Le test qui disqualifie une sauvegarde** : « depuis mon compte d'administrateur du domaine,
> puis-je supprimer les sauvegardes ? » Si la réponse est oui, un rançongiciel le peut aussi.
> 📕 C'est exactement la situation d'HydroRégie aujourd'hui : NAS unique, sur le même réseau,
> accessible avec les identifiants du domaine.

## 3. Ce qu'il faut sauvegarder en OT (souvent oublié)

| Élément | Pourquoi c'est vital | Fréquence |
|---|---|---|
| **Programmes automates** (fichiers source) | Sans eux, un automate remplacé est une boîte vide. Un intégrateur peut mettre **des semaines** à reconstituer une logique de traitement | À chaque modification, versionné |
| **Configuration du SCADA** (synoptiques, alarmes, variables) | Reconstruire 200 vues à la main est irréaliste | Hebdomadaire + à chaque modification |
| **Base historian** | Traçabilité réglementaire de la qualité de l'eau | Quotidienne |
| **Configurations réseau** (commutateurs, pare-feu, VPN) | Redémarrer la segmentation après sinistre | À chaque changement, versionné |
| **Recettes / consignes de traitement** | Dosages, seuils, courbes de régulation | À chaque modification |
| **Documentation à jour** (schémas, plans d'adressage, contacts) | En crise, on n'a pas le temps de chercher | Mensuelle, **+ copie papier** |

> 🔑 **Le piège classique** : sauvegarder scrupuleusement l'ERP et oublier les programmes automates,
> qui vivent sur le disque dur du poste d'ingénierie… lui aussi chiffré par le rançongiciel.

## 4. Les modes de continuité du service d'eau

C'est **le cœur de l'argumentaire** du projet : montrer que l'eau coule même si l'informatique tombe.

| Mode | Déclencheur | Ce qui fonctionne | Ce qu'on perd | Durée tenable 📕 |
|---|---|---|---|---|
| **Nominal** | — | Télégestion complète, optimisation énergétique | — | — |
| **Dégradé — autonomie locale** | SCADA indisponible ou isolé volontairement | Les **automates régulent seuls** : niveau, pression, chloration asservie au débit. IHM locales sur site | Vision centralisée, optimisation, alarmes à distance | **Plusieurs jours** |
| **Manuel** | Automate HS ou site inaccessible | Manœuvres humaines des vannes, dosage contrôlé par **prélèvements** | Réactivité, précision ; forte charge en personnel | **Quelques jours**, avec renfort |
| **Crise majeure** | Perte de production | Interconnexions avec les réseaux voisins, citernes, distribution d'eau embouteillée | Le service normal | Selon les stocks |

### 🔴 L'exigence d'architecture qui en découle

> **Les automates doivent embarquer une logique de repli autonome et ne jamais dépendre du SCADA
> pour maintenir le service.**

C'est une exigence à écrire **dans les cahiers des charges des intégrateurs** (art. 21(2)(d)) et à
**tester** (art. 21(2)(f)) : on coupe volontairement le lien SCADA ↔ automate en fenêtre planifiée,
et on vérifie que la régulation se poursuit.

## 5. Le plan de reprise, étape par étape

```
0. DECIDER      : la cellule de crise declare le sinistre (qui ? sur quel critere ?)
1. ISOLER       : couper les liens pour stopper la propagation, PRESERVER LES PREUVES
                  (images disque AVANT reinstallation)
2. EVALUER      : quoi est touche, quoi est sain, les sauvegardes sont-elles intactes ?
3. RECONSTRUIRE : environnement d'accueil SAIN (jamais restaurer sur un socle compromis)
4. RESTAURER    : par ordre de priorite  ->  1) OT  2) sauvegardes  3) AD  4) metier  5) confort
5. VERIFIER     : integrite des donnees, coherence des consignes de traitement
6. REMETTRE     : progressivement, sous surveillance renforcee
7. CAPITALISER  : retour d'experience, mise a jour des procedures
```

> ⚠️ **L'étape 1 est celle qu'on rate** : réinstaller immédiatement détruit les preuves, empêche de
> comprendre le point d'entrée… et donc de le refermer. On réinfecte alors le système reconstruit.

## 6. Le test de restauration

📗 Sans test, l'article 21(2)(c) n'est pas satisfait — et l'article 21(2)(f) impose d'évaluer
l'efficacité.

| Test | Fréquence 📕 | Critère de réussite |
|---|---|---|
| Restauration d'un fichier isolé | Mensuelle | < 30 min |
| Restauration d'un serveur complet en bac à sable | Trimestrielle | < RTO |
| Restauration de la configuration SCADA | Semestrielle | Démarrage effectif et supervision opérationnelle |
| Rechargement d'un programme automate sur un équipement de rechange | Annuelle | Automate fonctionnel |
| **Bascule en mode dégradé** en conditions réelles | **Annuelle** | Distribution d'eau **maintenue** |
| Exercice de crise complet | Annuelle | Voir [10 — Gestion de crise](10-gestion-de-crise-cyber.md) |

## ✅ Vérification

- [ ] Que signifient RTO et RPO, et qui les décide ?
- [ ] Que veut dire le « 0 » de la règle 3-2-1-1-0 ?
- [ ] Cite trois éléments OT à sauvegarder qu'on oublie souvent.
- [ ] Pourquoi ne faut-il pas réinstaller immédiatement après une attaque ?

---

⬅️ [08 — Détection](08-detection-et-journalisation.md) · ➡️ [10 — Gestion de crise cyber](10-gestion-de-crise-cyber.md)
