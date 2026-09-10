# Annexe B — Notification d'incident (72 h)

> 📗 **Fondement** : article 23(4)(b) de la directive (UE) 2022/2555
> **Délai** : sans retard injustifié et **dans les 72 heures** après avoir eu connaissance de
> l'incident important.
> **Contenu exigé** : mettre à jour l'alerte précoce, fournir une **évaluation initiale** de
> l'incident (gravité, impact) et, **lorsqu'ils sont disponibles**, les **indicateurs de
> compromission**.

---

## NOTIFICATION D'INCIDENT

**Fondement juridique** : article 23(4)(b) de la directive (UE) 2022/2555
**Destinataire** : autorité nationale compétente / CSIRT national
**Émetteur** : HydroRégie — entité essentielle (annexe I, point 6)
**Référence interne** : `INC-2027-0316-001` — **mise à jour n° 1**
**Se rapporte à** : alerte précoce du 16/03/2027 à 14 h 30 (accusé `AR-2027-0316-1430`)
**Date et heure d'envoi** : **jeudi 18 mars 2027, 17 h 00**
**Délai écoulé depuis T0** : **60 h 48** ✅ *(échéance : 19/03/2027 à 04 h 12)*

---

### 1. Rappel des éléments de l'alerte précoce

| Champ | Valeur | Évolution |
|---|---|---|
| T0 — connaissance de l'incident | 16/03/2027 à 04 h 12 | Inchangé |
| Type | Rançongiciel sur le système d'information de gestion | Confirmé |
| Actes illicites ou malveillants | Oui | **Confirmé** — plainte déposée le 17/03/2027 |
| Impact transfrontalier | Non | Confirmé |
| Incident en cours | Oui | ⚠️ **Toujours en cours** — reconstruction engagée |

### 2. Évaluation initiale de la gravité

| Critère | Évaluation |
|---|---|
| **Perturbation opérationnelle** | **Grave** sur le système de gestion : facturation, relation abonnés, maintenance et messagerie indisponibles depuis 3 jours |
| **Continuité du service essentiel** | ✅ **Maintenue** — distribution d'eau potable non interrompue, aucun usager privé d'eau |
| **Qualité de l'eau** | ✅ Conforme — 46 prélèvements réalisés depuis le 16/03, tous conformes |
| **Système industriel** | ✅ **Non compromis** — vérification d'intégrité en cours, aucune modification de programme ou de consigne détectée à ce jour |
| **Données à caractère personnel** | ⚠️ **Affectées** — 240 000 abonnés (identité, adresse, coordonnées bancaires de prélèvement, historique de consommation). Notification à l'autorité de protection des données transmise le 18/03/2027 |
| **Pertes financières estimées** | 📕 Entre 800 k€ et 1,4 M€ (remédiation, astreinte renforcée, décalage de facturation) — estimation provisoire |
| **Nombre de personnes concernées** | 450 000 habitants (service), 240 000 abonnés (données) |
| **Durée d'indisponibilité** | 3 jours à ce jour ; rétablissement complet estimé au 26/03/2027 |

> 📗 **Qualification retenue au titre de l'art. 23(3)** : incident important au titre du critère (a)
> — perturbation opérationnelle grave et pertes financières — **et** du critère (b) — dommages
> susceptibles d'affecter des tiers (abonnés).

### 3. Description technique de l'incident

#### 3.1 Chronologie établie à ce stade

| Date / heure | Événement |
|---|---|
| 07/03/2027 ~23 h 41 | **Première connexion** frauduleuse identifiée, via le compte d'un prestataire de maintenance bureautique |
| 07/03 → 15/03 | Phase de reconnaissance et de latéralisation (9 jours) — élévation de privilèges sur le domaine |
| 15/03/2027 ~22 h 00 | Suppression des copies d'ombre (*shadow copies*) et préparation du chiffrement |
| 16/03/2027 ~03 h 50 | **Déclenchement du chiffrement** |
| **16/03/2027 04 h 12** | 🔴 **T0 — détection** par l'astreinte exploitation |
| 16/03/2027 04 h 45 | Coupure physique de la liaison gestion ↔ industriel |
| 16/03/2027 06 h 15 | Sauvegardes hors ligne vérifiées intactes |
| 17/03/2027 | Point d'entrée identifié ; début de la reconstruction sur socle sain |
| 18/03/2027 | Restauration de l'annuaire en cours ; vérification d'intégrité du système industriel engagée |

#### 3.2 Vecteur initial

> Compromission du compte d'un **prestataire de maintenance bureautique**, à la suite d'un
> hameçonnage ciblé. Ce compte disposait de **droits d'administration du domaine**, ce qui a permis
> une latéralisation rapide. L'accès n'était **pas protégé par une authentification multifacteur**
> à la date de la compromission — la généralisation du MFA aux comptes de prestataires était
> planifiée pour le 30 juin 2027 dans notre feuille de route de mise en conformité.

#### 3.3 Systèmes affectés

| Système | État | Restauration |
|---|---|---|
| Contrôleurs de domaine (2) | Chiffrés | Reconstruction sur socle neuf, en cours |
| Serveurs de fichiers (3) | Chiffrés | Restauration depuis bande du 12/03 |
| Application de facturation | Chiffrée | Restauration prévue le 20/03 |
| Gestion de maintenance (GMAO) | Chiffrée | Restauration prévue le 22/03 |
| Messagerie | Indisponible | Rétablissement prévu le 26/03 |
| Postes de travail (≈ 180 sur 420) | Chiffrés | Réinstallation par lots |
| **Superviseur SCADA** | ✅ **Sain** | Isolé volontairement |
| **Automates et RTU (≈ 350)** | ✅ **Sains** | Vérification d'intégrité en cours |
| Historian | ✅ Sain | — |

#### 3.4 📗 Indicateurs de compromission *(art. 23(4)(b) — « lorsqu'ils sont disponibles »)*

| Type | Valeur | Commentaire |
|---|---|---|
| Famille de rançongiciel | `<famille identifiée avec l'appui du CSIRT>` | Identifiée le 16/03 à 22 h 00 |
| Empreintes des exécutables | `<SHA-256 des binaires>` | Extraits des images disque |
| Adresses IP de commande et contrôle | `<adresses>` | Bloquées en périmétrie |
| Comptes compromis | `<identifiants>` | Désactivés, mots de passe réinitialisés |
| Extension des fichiers chiffrés | `<extension>` | — |
| Nom de la note de rançon | `<nom du fichier>` | — |
| Persistance observée | Tâches planifiées + service Windows | Supprimées |
| Outils légitimes détournés | Outils d'administration à distance et d'archivage | — |

> 💡 Les indicateurs sont transmis **au format demandé par le CSIRT** et partagés au titre de
> l'article 29 (partage d'informations) afin d'aider les autres opérateurs du secteur.

### 4. Mesures d'atténuation appliquées

| # | Mesure | Date | Effet |
|---|---|---|---|
| 1 | Coupure gestion ↔ industriel | 16/03 04 h 45 | 🔴 **A empêché toute propagation vers le procédé** |
| 2 | Isolement du système d'information | 16/03 06 h 00 | Arrêt de la propagation interne |
| 3 | Mise hors ligne des sauvegardes restantes | 16/03 06 h 15 | Préservation de la capacité de reprise |
| 4 | Blocage des adresses de commande et contrôle | 16/03 20 h 00 | Coupure du canal de pilotage |
| 5 | Réinitialisation de l'ensemble des mots de passe | 17/03 | Révocation des accès de l'attaquant |
| 6 | Désactivation des comptes prestataires | 16/03 08 h 00 | Fermeture du vecteur initial |
| 7 | Reconstruction sur socle sain | 17/03 → | Évite la réinfection |
| 8 | Exploitation en mode dégradé autonome | 16/03 04 h 45 → | ✅ **Continuité de la distribution d'eau** |
| 9 | Contrôles qualité renforcés (prélèvements toutes les 4 h) | 16/03 → | Sécurité sanitaire |

### 5. Mesures en cours

- Vérification d'intégrité de l'ensemble des automates et du superviseur, par l'intégrateur
- Reconstruction de l'annuaire et restauration des applications métier
- Recherche des indicateurs de compromission sur l'ensemble du parc
- Analyse des journaux disponibles pour préciser le périmètre de l'exfiltration éventuelle

### 6. Impact transfrontalier

> ❌ Aucun. Activité exclusivement nationale, aucun service fourni dans un autre État membre,
> aucune interconnexion avec un opérateur étranger.

### 7. Information des tiers

| Destinataire | Fondement | Date |
|---|---|---|
| Usagers et abonnés | **Art. 23(1)** — incident affectant la fourniture des services | 16/03 à 15 h 00, puis mises à jour quotidiennes |
| Autorité de protection des données (CNIL) | Art. 33 RGPD | 18/03 à 17 h 30 |
| Autorité organisatrice, préfecture, agence régionale de santé | Obligations sectorielles | 16/03 à 10 h 00 |
| Dépôt de plainte | — | 17/03 |
| Assureur | Contrat | 16/03 |

### 8. Suite prévue

> Un **rapport final** sera transmis au titre de l'article 23(4)(d), **au plus tard un mois après la
> présente notification**, soit le **18 avril 2027**. Il comprendra la description détaillée de
> l'incident, le type de menace et la cause profonde, les mesures d'atténuation appliquées et en
> cours, et l'absence d'impact transfrontalier.
>
> Si l'incident était encore en cours à cette date, un **rapport d'avancement** serait transmis au
> titre de l'article 23(4)(e), suivi du rapport final dans le mois suivant le traitement de
> l'incident.

---

**Rédigé par** : `<nom>`, RSSI · **Validé par** : `<nom>`, Directeur général
**Transmis le** : 18/03/2027 à 17 h 00 · **Accusé de réception** : `AR-2027-0318-1700`

---

## 📋 Aide-mémoire de rédaction

| ✅ À faire | ❌ À éviter |
|---|---|
| **Mettre à jour** l'alerte précoce, ne pas la réécrire de zéro | Repartir d'une page blanche |
| Donner une **évaluation initiale** — c'est le mot du texte, une estimation suffit | Attendre des chiffres définitifs |
| Fournir les indicateurs **disponibles** | Retarder l'envoi pour attendre l'analyse complète |
| Dire clairement si le **service essentiel** est maintenu | Ne parler que du système d'information |
| Assumer les écarts (ici : MFA prestataires non encore déployé) | Masquer une faiblesse — l'autorité la découvrira, et la transparence est un facteur d'atténuation (art. 32(7)) |
| Annoncer l'échéance du rapport final | Laisser la suite dans le flou |

⬅️ [Annexe A](A-alerte-precoce-24h.md) · ➡️ [Annexe C — Rapport final](C-rapport-final-1-mois.md)
