# Article 6 — Définitions

> 🎯 **En une phrase** : l'article 6 contient 41 définitions ; une dizaine seulement compte
> vraiment, mais elles **conditionnent tout le reste**.
> ⏱️ 5 minutes.

---

## Les définitions qui changent quelque chose

| Terme | Définition (reformulée) | Pourquoi c'est important |
|---|---|---|
| **Réseau et système d'information** | Un réseau de communications électroniques, un dispositif ou un ensemble de dispositifs qui traitent des données numériques automatiquement, **ainsi que les données** qu'ils traitent | 🔑 **Assez large pour inclure les automates et le SCADA.** C'est le fondement juridique du bloc 3 |
| **Sécurité des réseaux et des systèmes d'information** | Leur capacité à résister, à un niveau de confiance donné, à des événements compromettant la **disponibilité**, l'**authenticité**, l'**intégrité** ou la **confidentialité** | La **disponibilité est citée en premier** — c'est cohérent avec un enjeu OT |
| **Incident** | Un événement compromettant la disponibilité, l'authenticité, l'intégrité ou la confidentialité de données **ou** des services | Un incident n'est pas forcément une attaque : une panne compte |
| **Incident évité** *(near miss)* | Un événement qui **aurait pu** compromettre… mais dont la survenance a été **empêchée** | Peut faire l'objet d'une notification **volontaire** (art. 30) |
| **Traitement d'incident** | Toute action visant à **prévenir, détecter, analyser, contenir** un incident ou à y **répondre** et à assurer le rétablissement | Le périmètre attendu d'une procédure d'incident (art. 21(2)(b)) |
| **Cybermenace** | Toute circonstance, événement ou action susceptible de nuire, perturber ou avoir un impact négatif | — |
| **Cybermenace importante** | Cybermenace dont les caractéristiques techniques laissent supposer un **impact grave** | Déclenche l'obligation d'informer les destinataires (art. 23(2)) |
| **Risque** | La **perte potentielle** résultant d'un incident, exprimée comme une combinaison de son **ampleur** et de sa **probabilité** | La base de l'analyse de risques (art. 21(2)(a)) |
| **Vulnérabilité** | Une faiblesse, susceptibilité ou faille pouvant être exploitée par une cybermenace | Art. 21(2)(e) et art. 12 |
| **Entité** | Une personne physique ou morale créée et reconnue comme telle en vertu du droit national | ✅ **Inclut une régie publique** |
| **Représentant** | Personne établie dans l'Union désignée pour agir pour le compte d'une entité non établie dans l'Union | Art. 26 |
| **Norme** | Une norme au sens du règlement (UE) n° 1025/2012 | Art. 25 |

---

## 🔑 À retenir

Trois définitions à savoir citer :

1. **« Réseau et système d'information »** est **volontairement large** : il couvre les systèmes
   industriels. On ne peut donc pas prétendre que le SCADA ou les automates seraient hors périmètre
   NIS2.
2. **« Sécurité »** cite **la disponibilité en premier** — ce qui légitime le raisonnement OT
   (Disponibilité > Intégrité > Confidentialité).
3. **« Incident »** n'exige **aucune malveillance**. Une défaillance technique qui rend le SCADA
   indisponible est un incident au sens de la directive.

---

## 🏢 Chez HydroRégie

| Élément du SI | Couvert par la définition ? |
|---|---|
| Postes bureautiques, AD, messagerie | ✅ Oui |
| ERP de facturation, portail abonnés | ✅ Oui |
| Superviseur SCADA, historian | ✅ Oui |
| Automates, RTU, capteurs communicants | ✅ Oui — ce sont des dispositifs traitant des données numériques |
| Compteurs communicants (télérelève) | ✅ Oui |
| Une vanne purement manuelle | ❌ Non (aucun traitement de données) |

➡️ **Conclusion pour le bloc 1** : le périmètre NIS2 d'HydroRégie couvre **l'IT et l'OT**, sans
possibilité d'exclure l'industriel. C'est précisément ce qui rend la segmentation obligatoire.

---

## ⚠️ Le piège

Traiter la notion d'« incident » comme synonyme de « cyberattaque ». Le registre des incidents doit
donc aussi consigner les pannes, les erreurs de manipulation et les défaillances de prestataires.

---

⬅️ [Article 5](article-05-harmonisation-minimale.md) · ➡️ [Articles 7 à 13 — Dispositif national](articles-07-a-13-dispositif-national.md)
