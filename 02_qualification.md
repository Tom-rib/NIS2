# 02 — Qualification & cadre réglementaire

> 🎯 **Objectifs de cette fiche**
> 1. Comprendre ce qu'est NIS2 et d'où elle vient.
> 2. Savoir dérouler **la méthode en 4 questions** pour qualifier n'importe quelle entité.
> 3. Connaître la différence entre entité **essentielle** et entité **importante**.
> 4. Savoir quelles obligations découlent du statut.
>
> ⏱️ Lecture : 15 minutes.
> 📗 Toutes les règles de cette fiche sont rattachées à leur article.

---

## 1. NIS2, c'est quoi exactement ?

**NIS** = *Network and Information Security*. C'est une **directive européenne**, c'est-à-dire un
texte que chaque État membre doit **transposer** dans son droit national.

| | NIS1 (2016/1148) | NIS2 (UE) 2022/2555 |
|---|---|---|
| Entités concernées en France | ~500 « opérateurs de services essentiels » | ~15 000 entités (source ANSSI) |
| Secteurs | 6 | 18 |
| Qui décide qui est concerné | L'État désigne, entité par entité | **L'entité s'auto-qualifie** selon secteur + taille (art. 2) |
| Dirigeants | Peu impliqués | **Responsabilité directe** (art. 20) |
| Sanctions | Faibles | Jusqu'à **10 M€ ou 2 % du CA mondial** (art. 34) |

> 📗 NIS2 abroge NIS1 à compter du **18 octobre 2024** (art. 44) et s'applique depuis cette même
> date (art. 41). La date limite de transposition était le **17 octobre 2024**.

### ⚠️ L'état de la transposition en France (vérifié le 10/09/2026)

📙 **La loi française n'est pas encore promulguée.** Le projet de loi « résilience des
infrastructures critiques et renforcement de la cybersécurité » a été adopté par le Sénat les
11 et 12 mars 2025, puis voté en commission spéciale à l'Assemblée nationale le 10 septembre 2025.
Les décrets et arrêtés suivront la promulgation.
*Source : [FAQ MonEspaceNIS2 — avancement de la transposition](https://aide.monespacenis2.cyber.gouv.fr/fr/article/avancement-de-la-transposition-de-la-directive-nis-2-1b3j1da/)*

**Conséquence pratique pour le projet** : on raisonne sur **le texte de la directive**, et on
signale explicitement ce qui dépendra des textes français (seuils précis d'incident significatif,
modalités d'enregistrement, calendrier de mise en œuvre). Un rendu qui citerait « la loi NIS2
française » serait factuellement faux à la date de rédaction.

---

## 2. La méthode en 4 questions

C'est **la** compétence du bloc 1. Elle marche pour n'importe quelle entreprise.

```
Q1. Mon secteur est-il listé en annexe I ou II ?
        | non -> hors champ (sauf designation, art. 2(2))
        v oui
Q2. Quelle est ma taille (recommandation 2003/361/CE) ?
        | < moyenne -> hors champ (sauf cas particuliers art. 2(2))
        v moyenne ou grande
Q3. Annexe I + grande entreprise ?
        | oui -> ENTITE ESSENTIELLE (art. 3(1)(a))
        | non -> ENTITE IMPORTANTE (art. 3(2))
        v
Q4. Un cas particulier me remonte-t-il en essentielle ?
     (art. 2(2), art. 3(1)(b) a (g) : DNS, TLD, telecoms, administration,
      entite critique au titre de la directive REC 2022/2557, designation nationale)
```

### Q1 — Le secteur (annexes I et II)

📗 **Annexe I — « Secteurs hautement critiques »** (11 secteurs) : énergie, transports, banque,
infrastructures des marchés financiers, santé, **eau potable**, eaux usées, infrastructure
numérique, gestion des services TIC (interentreprises), administration publique, espace.

📗 **Annexe II — « Autres secteurs critiques »** (7 secteurs) : services postaux et d'expédition,
gestion des déchets, fabrication/production/distribution de produits chimiques, production et
distribution de denrées alimentaires, fabrication (dispositifs médicaux, informatique,
électronique, machines, véhicules), fournisseurs numériques (places de marché, moteurs de
recherche, réseaux sociaux), recherche.

> 🔎 **HydroRégie** relève de l'**annexe I, point 6 — « Eau potable »**, qui vise les fournisseurs
> et distributeurs d'eau destinée à la consommation humaine au sens de la directive (UE) 2020/2184.

### Q2 — La taille (recommandation 2003/361/CE)

| Catégorie | Effectif | ET / OU financier |
|---|---|---|
| Micro | < 10 | CA ≤ 2 M€ **et** bilan ≤ 2 M€ |
| Petite | < 50 | CA ≤ 10 M€ **et** bilan ≤ 10 M€ |
| **Moyenne** | < 250 | CA ≤ 50 M€ **ou** bilan ≤ 43 M€ |
| **Grande** | ≥ 250 | **ou** CA > 50 M€ **et** bilan > 43 M€ |

> ⚠️ **Le piège classique** : le critère d'effectif est **autonome**. 250 salariés suffisent, même
> avec un petit chiffre d'affaires. À l'inverse, sous 250 salariés, il faut **les deux** critères
> financiers dépassés (CA **et** bilan) pour basculer en « grande entreprise ».

### Q3 — Le croisement secteur × taille

| | Annexe I (hautement critique) | Annexe II (autre secteur critique) |
|---|---|---|
| **Grande entreprise** | 🔴 **Entité essentielle** (art. 3(1)(a)) | 🟠 Entité importante (art. 3(2)) |
| **Moyenne entreprise** | 🟠 Entité importante (art. 3(2)) | 🟠 Entité importante (art. 3(2)) |
| Petite / micro | Hors champ (sauf art. 2(2)) | Hors champ (sauf art. 2(2)) |

### Q4 — Les cas particuliers

📗 Sont **essentielles quelle que soit leur taille** (art. 3(1)) : fournisseurs de services DNS,
registres de noms de domaine de premier niveau, prestataires de services de confiance qualifiés,
entités identifiées comme **entités critiques** au titre de la directive (UE) 2022/2557 (REC),
certaines administrations centrales, et toute entité **désignée** par l'État membre.

📗 Sont dans le champ **indépendamment de la taille** (art. 2(2)) notamment : l'entité qui est
**le seul prestataire** dans un État membre d'un service essentiel au maintien d'activités
sociétales ou économiques critiques, ou celle dont la perturbation du service **pourrait avoir un
impact important sur la sécurité publique, la sûreté publique ou la santé publique**.

> 💡 Retiens ce raisonnement : même si HydroRégie était une petite structure, l'article 2(2)
> permettrait de la faire entrer dans le champ, car couper l'eau de 450 000 personnes est
> évidemment un impact de santé publique.

---

## 3. Essentielle ou importante : quelle différence concrète ?

Les **obligations de fond sont les mêmes** (art. 20, 21, 23). Ce qui change, c'est **le contrôle**
et **la sanction**.

| | Entité essentielle | Entité importante |
|---|---|---|
| Mesures art. 21 | ✅ Identiques | ✅ Identiques |
| Notification art. 23 | ✅ Identique (24 h / 72 h / 1 mois) | ✅ Identique |
| Supervision | **Ex ante et ex post** (art. 32) : audits, inspections sur site, scans de sécurité **sans incident préalable** | **Ex post uniquement** (art. 33) : contrôle seulement s'il y a des éléments laissant penser à un manquement |
| Amende administrative maximale | **≥ 10 000 000 €** ou **2 %** du CA mondial annuel, le montant le plus élevé (art. 34(4)) | **≥ 7 000 000 €** ou **1,4 %** du CA mondial annuel, le montant le plus élevé (art. 34(5)) |
| Sanction sur les dirigeants | Interdiction temporaire d'exercer des fonctions dirigeantes possible (art. 32(5)(b)) | Non prévue |
| Suspension d'agrément | Possible (art. 32(5)(a)) | Non prévue |

> 📗 « Le montant le plus élevé » : pour une entité à 72 M€ de CA, 2 % = 1,44 M€, donc c'est le
> plancher de **10 M€** qui s'applique comme maximum encouru. Le statut essentiel coûte cher.

---

## 4. Les obligations qui découlent du statut

| Obligation | Article | En clair |
|---|---|---|
| **Gouvernance** | art. 20 | La direction **approuve** les mesures, **supervise** leur mise en œuvre, peut être **tenue responsable**, et **suit une formation** cyber |
| **Mesures de gestion des risques** | art. 21 | 10 domaines minimum (voir fiche 03), approche **tous risques**, proportionnée |
| **Notification des incidents** | art. 23 | Alerte précoce **24 h**, notification **72 h**, rapport final **1 mois** |
| **Enregistrement** | art. 3(4) | Fournir à l'autorité : nom, adresse, secteur, coordonnées, plages d'adresses IP — en France via **MonEspaceNIS2** |
| **Information des destinataires** | art. 23(1) et (2) | Prévenir les usagers quand l'incident ou la menace les affecte |
| **Chaîne d'approvisionnement** | art. 21(2)(d) et 21(3) | Tenir compte des vulnérabilités de **chaque fournisseur direct** |

📙 **Enregistrement en France** : l'ANSSI a ouvert un **pré-enregistrement volontaire** sur la
plateforme **MonEspaceNIS2** le 24 novembre 2025. Il ne remplace pas l'enregistrement obligatoire,
qui deviendra exigible avec les textes de transposition.
*Source : [MesServicesCyber — NIS 2](https://messervices.cyber.gouv.fr/nis2)*

---

## 5. Le raisonnement appliqué à HydroRégie

| Étape | Constat | Fondement |
|---|---|---|
| Q1 Secteur | Distribution d'eau destinée à la consommation humaine | **Annexe I, point 6** |
| Q2 Taille | 380 salariés (≥ 250) → **grande entreprise** | Recommandation 2003/361/CE, art. 2 de l'annexe |
| Q3 Croisement | Annexe I + grande entreprise | **Art. 3(1)(a)** |
| Q4 Cas particulier | Seul distributeur sur son territoire, impact santé publique — confirme le statut | Art. 2(2)(b) et (c) |
| **Conclusion** | 🔴 **ENTITÉ ESSENTIELLE** | Cohérent avec le courrier de l'autorité nationale |

> 📕 Le critère d'effectif suffit à lui seul (380 ≥ 250). Les critères financiers
> (72 M€ de CA **et** 95 M€ de bilan, tous deux au-dessus des seuils de 50 M€ / 43 M€)
> confirment la qualification par une seconde voie. La qualification est donc **robuste**.

---

## ✅ Vérification de fin de fiche

- [ ] Une entreprise de 300 salariés dans la gestion des déchets (annexe II) : essentielle ou importante ?
      <details><summary>Réponse</summary>**Importante**. L'annexe II ne donne jamais le statut essentiel par la taille (art. 3(1)(a) ne vise que l'annexe I).</details>
- [ ] Une entreprise de 120 salariés, 60 M€ de CA, 20 M€ de bilan, secteur énergie : dans le champ ?
      <details><summary>Réponse</summary>Oui, **entité importante** : sous 250 salariés il faut CA > 50 M€ **et** bilan > 43 M€ pour être « grande ». Ici le bilan est trop faible → moyenne entreprise → annexe I + moyenne = importante.</details>
- [ ] Quelle est l'amende maximale encourue par une entité essentielle ?
- [ ] Sur quel article s'appuie l'obligation de formation des dirigeants ?

---

⬅️ [01 — Préparation](01_preparation.md) · ➡️ **Suite** : [03 — Mise en conformité & architecture](03_mise_en_conformite.md)
