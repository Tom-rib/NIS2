# Annexe C — Rapport final (1 mois)

> 📗 **Fondement** : article 23(4)(d) de la directive (UE) 2022/2555
> **Délai** : au plus tard **un mois après la transmission de la notification d'incident** (celle
> des 72 h) — 🔴 **pas** un mois après la découverte.
> **Contenu exigé** :
> (i) description détaillée de l'incident, y compris sa gravité et son impact ;
> (ii) type de menace ou **cause profonde** ayant probablement déclenché l'incident ;
> (iii) mesures d'atténuation **appliquées et en cours** ;
> (iv) le cas échéant, **impact transfrontalier**.

---

## RAPPORT FINAL D'INCIDENT

**Fondement juridique** : article 23(4)(d) de la directive (UE) 2022/2555
**Destinataire** : autorité nationale compétente / CSIRT national
**Émetteur** : HydroRégie — entité essentielle (annexe I, point 6)
**Référence interne** : `INC-2027-0316-001` — **rapport final**
**Se rapporte à** : alerte précoce du 16/03/2027 et notification d'incident du 18/03/2027
**Date d'envoi** : **jeudi 15 avril 2027**
**Délai** : **28 jours** après la notification du 18/03 ✅ *(échéance : 18/04/2027)*
**État de l'incident** : ✅ **Clos** — service intégralement rétabli le 26/03/2027

---

## 1. Synthèse

| Élément | Valeur |
|---|---|
| Type d'incident | Rançongiciel avec double extorsion (chiffrement + menace de divulgation) |
| Date de compromission initiale | 07/03/2027 vers 23 h 41 |
| Date de détection (T0) | 16/03/2027 à 04 h 12 |
| **Durée de présence non détectée** | **9 jours** |
| Date de rétablissement complet | 26/03/2027 |
| **Interruption de la distribution d'eau** | ✅ **AUCUNE** |
| Durée d'exploitation en mode dégradé | 6 jours (16/03 au 22/03) |
| Systèmes de gestion touchés | 2 contrôleurs de domaine, 3 serveurs de fichiers, 3 applications métier, 180 postes |
| **Système industriel** | ✅ **Non compromis** — vérification exhaustive des 350 automates |
| Personnes concernées | 240 000 abonnés (données), 450 000 habitants (service) |
| Rançon | ❌ **Non payée** |
| Coût total constaté 📕 | **1,18 M€** |

---

## 2. 📗 (i) Description détaillée de l'incident, gravité et impact

### 2.1 Déroulement complet

| Phase | Période | Description |
|---|---|---|
| **Compromission initiale** | 07/03 23 h 41 | Connexion frauduleuse au VPN avec les identifiants d'un prestataire de maintenance bureautique, obtenus par hameçonnage ciblé (courriel imitant un portail de gestion de tickets). Le compte disposait de droits d'administration du domaine et n'était pas protégé par une authentification multifacteur |
| **Reconnaissance** | 08/03 → 12/03 | Cartographie du réseau, identification des serveurs de fichiers, de l'annuaire et des sauvegardes. Utilisation d'outils d'administration légitimes (technique dite du « détournement d'outils intégrés ») |
| **Exfiltration** | 12/03 → 14/03 | Extraction d'environ **42 Go** de données depuis les serveurs de fichiers, dont des exports de la base abonnés |
| **Préparation** | 15/03 22 h 00 | Suppression des copies d'ombre, désactivation de l'antivirus par stratégie de groupe, déploiement de la charge utile |
| **Chiffrement** | 16/03 03 h 50 | Déclenchement simultané sur l'ensemble du domaine |
| **Détection** | 16/03 04 h 12 | Alarmes SCADA (perte de liaison avec l'historian) et indisponibilité des postes du siège |
| **Confinement** | 16/03 04 h 45 | Coupure physique gestion ↔ industriel — **33 minutes après la détection** |
| **Remédiation** | 17/03 → 26/03 | Reconstruction sur socle sain, restauration, vérifications |
| **Retour au mode nominal** | 23/03 | Reconnexion progressive du lien gestion ↔ industriel après vérification d'intégrité |

### 2.2 Gravité

| Critère de l'art. 23(3) | Évaluation finale |
|---|---|
| **(a) Perturbation opérationnelle grave** | ✅ Confirmée sur le système de gestion — 10 jours d'indisponibilité partielle |
| **(a) Pertes financières** | ✅ Confirmées — **1,18 M€** |
| **(b) Dommages à des tiers** | ✅ Confirmés — exfiltration de données de 240 000 abonnés, dont des coordonnées bancaires de prélèvement |
| **Continuité du service essentiel** | ✅ **Maintenue** — aucun usager privé d'eau, aucune non-conformité de qualité |

### 2.3 Impact détaillé

| Domaine | Impact | Durée |
|---|---|---|
| **Distribution d'eau potable** | ✅ **Aucune interruption** | — |
| **Qualité de l'eau** | ✅ Aucune non-conformité — 312 prélèvements réalisés, tous conformes | — |
| Supervision centralisée | Indisponible (isolement volontaire) | 6 jours |
| Facturation abonnés | Indisponible | 10 jours — 2 cycles de facturation décalés |
| Espace abonnés en ligne | Indisponible | 10 jours |
| Accueil téléphonique | Dégradé | 8 jours |
| Gestion de maintenance | Indisponible | 6 jours — 87 interventions reportées |
| Messagerie | Indisponible | 10 jours |
| **Données personnelles** | 240 000 abonnés — exfiltration confirmée | Permanent |
| Charge humaine | Astreinte renforcée : **1 240 heures** supplémentaires | 6 jours |

### 2.4 Coût constaté 📕

| Poste | Montant |
|---|---|
| Prestation de réponse à incident et investigation | 185 k€ |
| Reconstruction (matériel, licences, main-d'œuvre) | 310 k€ |
| Astreinte renforcée et heures supplémentaires | 95 k€ |
| Perte et décalage de recettes de facturation | 420 k€ |
| Communication de crise et information des abonnés | 45 k€ |
| Accompagnement juridique et notification RGPD | 65 k€ |
| Mesures correctives immédiates | 60 k€ |
| **TOTAL** | **1 180 k€** |

> 💡 À comparer aux **956 k€** du plan complet de mise en conformité sur 24 mois. **Un seul incident
> a coûté plus cher que la totalité du plan.**

---

## 3. 📗 (ii) Type de menace et cause profonde

### 3.1 Type de menace

> Rançongiciel opéré par un groupe criminel, selon un mode opératoire dit de **double extorsion** :
> exfiltration des données **puis** chiffrement, avec menace de divulgation publique. Motivation
> financière ; aucune indication d'un ciblage lié à la nature de service essentiel de l'entité.

### 3.2 🔴 Cause profonde

L'analyse identifie **une cause immédiate** et **quatre causes structurelles**.

| # | Cause | Nature | Écart correspondant |
|---|---|---|---|
| **C1** | **Compte de prestataire disposant de droits d'administration du domaine, sans authentification multifacteur** | 🔴 **Cause immédiate** | E-05, E-09 |
| C2 | **Absence de segmentation entre le système de gestion et le système industriel** — la propagation vers l'OT n'a été empêchée que par une intervention humaine en 33 minutes | Structurelle | E-01 |
| C3 | **Journalisation insuffisante** — 9 jours de présence non détectée ; certains journaux avaient déjà tourné lors de l'investigation | Structurelle | E-13 |
| C4 | **Absence d'exigences de sécurité contractuelles** vis-à-vis des prestataires | Structurelle | E-11 |
| C5 | **Absence de détection comportementale** — la latéralisation et la suppression des copies d'ombre n'ont déclenché aucune alerte | Structurelle | E-13, E-14 |

> 📗 Ces causes étaient **déjà identifiées** dans l'analyse d'écart du 10 septembre 2026 et
> inscrites au plan d'actions approuvé par la direction. L'incident est survenu pendant la phase de
> mise en œuvre du plan. Les mesures de la **phase 0** (sauvegardes hors ligne, procédure de
> notification, MFA sur les comptes d'administration, communication hors domaine), **déjà
> déployées**, ont permis de limiter l'impact et de restaurer sans payer de rançon.

---

## 4. 📗 (iii) Mesures d'atténuation appliquées et en cours

### 4.1 Mesures appliquées pendant l'incident

| # | Mesure | Date | Effet mesuré |
|---|---|---|---|
| 1 | Coupure physique gestion ↔ industriel | 16/03 04 h 45 | 🔴 **Propagation vers le procédé empêchée** |
| 2 | Isolement complet du système d'information | 16/03 06 h 00 | Arrêt de la propagation |
| 3 | Bascule en exploitation dégradée autonome | 16/03 04 h 45 | ✅ **Continuité de la distribution** |
| 4 | Restauration depuis sauvegarde hors ligne du 12/03 | 19/03 → 22/03 | **Rançon non payée** |
| 5 | Reconstruction sur socle sain | 17/03 → 26/03 | Aucune réinfection constatée |
| 6 | Réinitialisation générale des accès | 17/03 | Révocation des accès de l'attaquant |
| 7 | Vérification d'intégrité des 350 automates | 17/03 → 22/03 | ✅ Aucune modification détectée |
| 8 | Contrôles qualité renforcés | 16/03 → 26/03 | 312 prélèvements conformes |

### 4.2 Mesures correctives déjà mises en œuvre depuis l'incident

| # | Mesure | Date | Écart clos |
|---|---|---|---|
| 1 | **MFA généralisé à tous les comptes prestataires et à privilèges** | 30/03/2027 | E-05 (avancé de 3 mois) |
| 2 | **Suppression de tous les droits d'administration du domaine accordés à des prestataires** | 28/03/2027 | E-09 |
| 3 | Comptes prestataires **désactivés par défaut**, activation sur ticket avec expiration automatique | 05/04/2027 | E-03 |
| 4 | **Synchronisation horaire (NTP) déployée sur l'ensemble du parc** | 10/04/2027 | E-13 (partiel) |
| 5 | Passage des tests de restauration en cadence mensuelle | 01/04/2027 | E-04 |
| 6 | Deuxième copie hors ligne, sur un site distinct | 12/04/2027 | E-04 |

### 4.3 Mesures en cours

| # | Mesure | Échéance | Écart |
|---|---|---|---|
| 1 | 🔴 **Segmentation IT / OT** — projet accéléré de 3 mois par décision du comité de sécurité du 20/04/2027 | **31/12/2027** au lieu du 31/03/2028 | E-01 |
| 2 | Journalisation centralisée avec rétention de 12 mois | 31/12/2027 | E-13 |
| 3 | Détection comportementale sur le système de gestion | 30/09/2027 | E-13 |
| 4 | Sonde passive de détection sur le réseau industriel | 31/01/2028 | E-14 |
| 5 | Annexe sécurité contractuelle imposée à tous les prestataires | 30/06/2027 | E-11 |
| 6 | Campagne de sensibilisation renforcée, incluant les prestataires | 30/06/2027 | E-12 |
| 7 | Test d'intrusion externe | 30/09/2027 | E-17 |

---

## 5. 📗 (iv) Impact transfrontalier

> ❌ **Aucun impact transfrontalier.** HydroRégie exerce son activité exclusivement sur le territoire
> national, ne fournit aucun service dans un autre État membre et n'a aucune interconnexion
> opérationnelle avec un opérateur étranger. Aucun autre État membre n'a été affecté.

---

## 6. Enseignements et partage

### 6.1 Ce qui a fonctionné

1. La **procédure de coupure gestion ↔ industriel**, écrite et testée, appliquée en 33 minutes.
2. La **sauvegarde hors ligne**, déployée trois mois plus tôt : elle a rendu la rançon inutile.
3. Les **modèles de notification** préparés à froid : les trois échéances ont été tenues avec marge.
4. L'**autonomie locale des automates** : six jours d'exploitation sans supervision, sans coupure d'eau.
5. La **communication hors domaine** : la cellule de crise a pu se coordonner malgré la perte de la messagerie.

### 6.2 Ce qui doit changer

1. La **segmentation** ne peut plus attendre : elle transforme une coupure physique brutale en
   isolement logique maîtrisé.
2. La **journalisation** est le prérequis de la détection : 9 jours de présence non détectée sont
   inacceptables pour une entité essentielle.
3. Les **prestataires** doivent être traités comme une extension du périmètre, avec les mêmes
   exigences (art. 21(2)(d) et 21(3)).

### 6.3 Partage d'informations

> Conformément à l'esprit de l'article 29, HydroRégie a partagé les **indicateurs de compromission**
> et le **retour d'expérience anonymisé** avec le CSIRT national et la communauté sectorielle des
> exploitants d'eau, afin de permettre à d'autres opérateurs de rechercher les mêmes traces.

---

**Rédigé par** : `<nom>`, RSSI · **Validé par** : `<nom>`, Directeur général
**Approuvé par le comité de sécurité des systèmes d'information** le 20/04/2027 (art. 20(1))
**Transmis le** : 15/04/2027 · **Accusé de réception** : `AR-2027-0415-XXXX`

---

## 📋 Aide-mémoire de rédaction

| ✅ À faire | ❌ À éviter |
|---|---|
| Traiter **explicitement les quatre points** (i) à (iv) de l'art. 23(4)(d) | Rédiger un récit libre sans structure |
| Compter le mois **depuis la notification des 72 h** | Compter depuis la découverte |
| Nommer la **cause profonde**, pas seulement la cause immédiate | S'arrêter à « un utilisateur a cliqué » |
| Distinguer les mesures **appliquées** et **en cours** | Présenter comme fait ce qui est planifié |
| Chiffrer l'impact réel | Rester dans le qualitatif |
| Assumer les écarts connus avant l'incident | Prétendre que rien n'était identifié — le plan d'actions daté prouve le contraire, et **c'est un atout** (art. 32(7) : degré de coopération et mesures prises) |
| Si l'incident est encore en cours : envoyer un **rapport d'avancement** (art. 23(4)(e)) | Laisser passer l'échéance |

⬅️ [Annexe B](B-notification-72h.md) · ➡️ [Annexe D — Information des usagers](D-information-usagers.md)
