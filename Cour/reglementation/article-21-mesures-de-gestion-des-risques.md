# Article 21 — Mesures de gestion des risques en matière de cybersécurité

> 🎯 **En une phrase** : dix domaines minimum à couvrir, avec une approche **tous risques** et
> **proportionnée**. C'est **l'article le plus important de NIS2** pour un technicien.
> ⏱️ 12 minutes. **Cœur du bloc 2.**

---

## 1. Les quatre paragraphes de l'article

### Art. 21(1) — Le principe

Les entités prennent des mesures **techniques, opérationnelles et organisationnelles** appropriées
et proportionnées pour **gérer les risques** qui menacent la sécurité de leurs réseaux et systèmes
d'information, et pour **éliminer ou réduire les conséquences** que les incidents ont sur les
destinataires de leurs services et sur d'autres services.

Ces mesures **tiennent compte** :

| Critère de proportionnalité | Ce que ça implique |
|---|---|
| L'état des connaissances | On ne peut pas ignorer une menace publiquement documentée |
| Les normes européennes et internationales applicables | IEC 62443, ISO/IEC 27001… |
| Le **coût** de mise en œuvre | Une petite structure n'est pas tenue au même dispositif |
| Le **degré d'exposition** au risque | Un service vital est plus exposé |
| La **taille** de l'entité | — |
| La **probabilité** de survenance des incidents et leur **gravité**, y compris **leurs conséquences sociétales et économiques** | 💧 Pour l'eau potable : gravité **maximale** |

> 🔑 **La proportionnalité fonctionne dans les deux sens.** Pour une entité essentielle du secteur
> de l'eau, elle **augmente** le niveau attendu : le critère « conséquences sociétales » place la
> barre haut.

### Art. 21(2) — Les dix domaines

Les mesures sont fondées sur une approche **« tous risques »** (*all-hazards*) visant à protéger les
réseaux et systèmes d'information **et leur environnement physique** contre les incidents. Elles
comprennent **au moins** :

| # | Réf. | Domaine | Traduction opérationnelle |
|---|---|---|---|
| 1 | **(a)** | Politiques relatives à l'**analyse des risques** et à la sécurité des SI | Analyse de risques formalisée (EBIOS RM), **PSSI** validée par la direction, revue annuelle |
| 2 | **(b)** | **Gestion des incidents** | Procédure de détection, qualification, escalade, traitement ; **registre des incidents** ; astreinte 24/7 |
| 3 | **(c)** | **Continuité des activités**, telle que la gestion des **sauvegardes** et la **reprise des activités**, et **gestion des crises** | PCA/PRA **testés**, sauvegardes hors ligne (3-2-1), RTO/RPO définis, cellule de crise |
| 4 | **(d)** | **Sécurité de la chaîne d'approvisionnement**, y compris les aspects liés aux relations avec les **fournisseurs directs** ou prestataires de services | Clauses de sécurité contractuelles, évaluation des intégrateurs, gestion des accès prestataires |
| 5 | **(e)** | Sécurité de l'**acquisition, du développement et de la maintenance**, y compris la **gestion et la divulgation des vulnérabilités** | Veille CVE / avis CERT-FR, politique de correctifs, **mesures de contournement** quand on ne peut pas patcher un automate |
| 6 | **(f)** | Politiques et procédures pour **évaluer l'efficacité** des mesures | Audits, tests d'intrusion, indicateurs, revue de direction |
| 7 | **(g)** | Pratiques de base en matière de **cyberhygiène** et **formation** à la cybersécurité | Guide d'hygiène ANSSI, sensibilisation de tous les agents, campagnes d'hameçonnage simulé |
| 8 | **(h)** | Politiques et procédures relatives à l'utilisation de la **cryptographie** et, le cas échéant, du **chiffrement** | Chiffrement des sauvegardes, des postes nomades, des flux d'administration, gestion des clés |
| 9 | **(i)** | **Sécurité des ressources humaines**, politiques de **contrôle d'accès** et **gestion des actifs** | Procédures arrivée/départ, inventaire complet IT **et OT**, revue périodique des droits, moindre privilège |
| 10 | **(j)** | **Authentification à plusieurs facteurs** ou authentification continue, **communications vocales, vidéo et texte sécurisées** et systèmes de **communication d'urgence sécurisés** au sein de l'entité, le cas échéant | MFA sur VPN, messagerie et administration ; **moyen de communication de secours** hors domaine pour la cellule de crise |

### Art. 21(3) — La chaîne d'approvisionnement, précisée

Les entités prennent en compte les **vulnérabilités propres à chaque fournisseur direct** et
prestataire de services, ainsi que la **qualité globale des produits et des pratiques de
cybersécurité** de leurs fournisseurs, y compris **leurs procédures de développement sécurisé**.

### Art. 21(4) — La correction

Lorsqu'une entité constate qu'elle **ne respecte pas** les mesures prévues, elle prend **sans délai** toutes les mesures correctives nécessaires, appropriées et proportionnées.

> 💡 Autrement dit : **constater un écart et ne rien faire est un manquement en soi.** C'est
> exactement ce que produit une analyse d'écart… d'où l'importance d'y associer un plan daté.

---

## 2. 🔑 Les trois idées à retenir

1. **« Tous risques » (all-hazards)** : NIS2 ne parle pas que de piratage. Incendie, inondation,
   panne électrique, erreur humaine, défaillance d'un prestataire : tout ce qui menace la
   disponibilité entre dans le périmètre. L'article mentionne d'ailleurs explicitement
   **l'environnement physique**.
2. **« Au moins »** : les dix domaines sont un **minimum**, pas une liste à cocher qui épuiserait
   l'obligation.
3. **La proportionnalité n'est pas une excuse** : elle s'apprécie notamment au regard des
   **conséquences sociétales**. Pour l'eau potable, cela tire les exigences vers le haut.

---

## 3. 🏢 Chez HydroRégie — cotation de départ

Échelle de maturité : 0 = inexistant, 1 = initialisé, 2 = reproductible, 3 = défini, 4 = maîtrisé.

| # | Domaine | Constat | Niveau | Cible |
|---|---|---|---|---|
| a | Analyse de risques / PSSI | Aucune analyse formalisée, pas de PSSI | **0** | 3 |
| b | Gestion des incidents | Traitement au cas par cas, pas de registre | **1** | 4 |
| c | Continuité / sauvegardes | Sauvegardes sur NAS unique en ligne, PRA non testé | **1** | 4 |
| d | Chaîne d'approvisionnement | Aucune clause de sécurité avec les intégrateurs | **0** | 3 |
| e | Acquisition / vulnérabilités | Pas de veille CVE sur les automates | **1** | 3 |
| f | Évaluation de l'efficacité | Aucun audit, aucun indicateur | **0** | 3 |
| g | Cyberhygiène / formation | Sensibilisation ponctuelle à l'arrivée | **1** | 3 |
| h | Cryptographie | Pas de chiffrement des sauvegardes ni des flux d'admin | **1** | 3 |
| i | RH / accès / actifs | Inventaire OT incomplet, comptes partagés, pas de revue des droits | **1** | 4 |
| j | MFA / communications | Pas de MFA, TeamViewer en accès permanent, pas de moyen de crise | **0** | 4 |

**Maturité moyenne : 0,6 / 4.** 📕 Cotation d'audit initial — voir le détail dans
[`Documentation/job-2-analyse-ecart.md`](../../Documentation/job-2-analyse-ecart.md).

---

## 4. Ce que la segmentation IT/OT vient couvrir

Une seule mesure technique — la segmentation — répond partiellement à **cinq** des dix domaines :

| Domaine | En quoi la segmentation y contribue |
|---|---|
| (a) | Elle matérialise l'analyse de risques : les zones traduisent les niveaux de criticité |
| (b) | Elle **contient** l'incident : un poste bureautique compromis n'atteint pas les automates |
| (c) | Elle permet de continuer à distribuer l'eau pendant qu'on traite l'IT — **le cœur du bloc 4** |
| (e) | Elle compense l'impossibilité de corriger certains automates (défense en profondeur) |
| (i) | Elle impose un point de passage unique et tracé pour l'administration |

> 🎯 **C'est l'argument central du projet** : la segmentation n'est pas une lubie technique, c'est
> la mesure qui rend les autres tenables.

---

## 5. ⚠️ Les pièges

| Piège | Correction |
|---|---|
| Traiter l'article 21 comme une checklist de conformité | C'est une **obligation de moyens renforcée** : il faut démontrer la pertinence des choix au regard des risques |
| Oublier l'OT dans l'inventaire (i) | Les 350 automates **sont** des systèmes d'information au sens de l'art. 6 |
| Appliquer une politique de correctifs IT à l'OT | Un automate ne se redémarre pas librement : la réponse est le **contournement** (segmentation, filtrage), documenté |
| Négliger le point (j) sur les communications d'urgence | Le jour où l'AD est chiffré, la messagerie ne fonctionne plus |
| Croire qu'un pare-feu suffit | Neuf des dix domaines sont **organisationnels** |

---

## 🔗 Liens

⬅️ [Article 20](article-20-gouvernance.md) · ➡️ [Article 22 — Évaluations coordonnées](article-22-evaluations-coordonnees.md) ·
📎 [Cours technique — segmentation](../technique/03-vlan-et-segmentation.md) · 📎 [Bloc 2 — analyse d'écart](../../Documentation/job-2-analyse-ecart.md)
