# Bloc 4 — Chronologie de gestion de crise et notifications réglementaires

> **Objet** : dérouler une crise cyber de bout en bout chez HydroRégie et produire les notifications
> exigées par l'article 23 de la directive (UE) 2022/2555.
> **Date** : 10 septembre 2026 · **Version** : 1.0
> **Classification** : Diffusion restreinte

---

## ⚠️ Nature de ce document

📕 **Le scénario ci-dessous est fictif.** Il est construit pour ce cas d'école et sert de base à
l'exercice de crise annuel (action A-34 de la feuille de route). Les notifications rédigées en
annexe sont des **modèles remplis avec les données du scénario** : elles montrent le format,
le niveau de détail et le respect des délais.

**Positionnement dans le plan** : le scénario est daté de **mars 2027**, c'est-à-dire **après la
phase 0** (procédure de notification, MFA, sauvegardes hors ligne, bastion — réalisés fin 2026)
mais **avant la segmentation IT/OT** (achevée en mars 2028). C'est volontaire : cela permet de
montrer ce que les mesures déjà en place ont sauvé, **et** ce que la segmentation aurait évité.

---

## 1. Le scénario

| Élément | Valeur |
|---|---|
| **Date** | Mardi **16 mars 2027** |
| **T0 (connaissance de l'incident)** | **04 h 12** |
| **Type** | Rançongiciel sur le système d'information de gestion, avec tentative de propagation vers l'OT |
| **Vecteur initial** | Compte d'un prestataire de maintenance bureautique, compromis par hameçonnage ciblé, utilisé 9 jours plus tôt pour un premier accès |
| **Périmètre touché** | Active Directory, serveurs de fichiers, ERP de facturation, GMAO, messagerie |
| **Périmètre menacé** | Superviseur SCADA (réseau non encore segmenté) |
| **Impact sur la distribution d'eau** | ⚠️ **Aucune interruption** — bascule en mode dégradé autonome |
| **Usagers concernés** | 240 000 abonnés (facturation), 450 000 habitants (service) |

---

## 2. La chronologie détaillée

### 🔴 Phase 1 — Détection (T0 à T+30 min)

| Heure | Acteur | Fait | Décision / action |
|---|---|---|---|
| **04 h 12** | Astreinte exploitation | Alarmes multiples sur le SCADA : perte de liaison avec l'historian. Les postes bureautiques du siège sont inaccessibles | 🔴 **T0 — ouverture de la main courante**, horodatée |
| 04 h 15 | Astreinte | Constat visuel : messages de rançon sur deux serveurs | Appel immédiat au responsable d'astreinte DSI |
| 04 h 22 | Responsable DSI | Confirme : chiffrement en cours sur le serveur de fichiers et l'ERP | Appel du RSSI |
| 04 h 30 | RSSI | Prend la main. Vérifie l'état du SCADA : **encore opérationnel** | Décision : **couper immédiatement le lien IT ↔ OT** |

> 🔑 **La décision de 04 h 30 est la plus importante de toute la crise.** Le réseau n'étant pas
> encore segmenté, la coupure est **physique** : débranchement du lien montant du commutateur
> desservant la zone de supervision, selon la procédure préétablie.

### 🟠 Phase 2 — Qualification et confinement (T+30 min à T+3 h)

| Heure | Acteur | Fait | Décision / action |
|---|---|---|---|
| **04 h 45** | DSI + exploitation | **Lien IT ↔ OT physiquement coupé** | ✅ **Les automates passent en autonomie locale. La distribution d'eau n'est pas interrompue** |
| 05 h 00 | RSSI | Applique la grille de qualification (art. 23(3)) | 🔴 **Incident qualifié IMPORTANT** — perturbation opérationnelle grave + données de 240 000 abonnés potentiellement affectées |
| 05 h 10 | RSSI | Appelle le directeur général | **Activation de la cellule de crise** |
| 05 h 30 | Cellule de crise | Réunion physique en salle de crise. Communication par la messagerie **hors domaine** et l'annuaire papier | Répartition des rôles, désignation du secrétaire de crise |
| 06 h 00 | DSI | Isolement complet : coupure de l'accès Internet, arrêt des serveurs non chiffrés, déconnexion du site de sauvegarde | Confinement |
| 06 h 15 | DSI | **Vérification des sauvegardes hors ligne** : la bande du vendredi 12 mars est intacte, sortie du robot | ✅ **La restauration est possible** |
| 06 h 30 | RSSI | Appel au **CERT-FR** (art. 11) pour assistance technique | Prise en charge, conseils de préservation des preuves |
| 07 h 00 | RSSI + DSI | **Images disque** des trois serveurs les plus touchés, **avant toute réinstallation** | ✅ Préservation des preuves |
| 07 h 30 | Exploitation | Déploiement de l'astreinte renforcée sur les 2 usines et 4 sites sensibles | Mode dégradé stabilisé |

### 🟡 Phase 3 — Escalade et notification (T+3 h à T+24 h)

| Heure | Acteur | Fait | Décision / action |
|---|---|---|---|
| 08 h 00 | Cellule de crise | Premier point de situation formel | Décision : notification à l'autorité **dans la journée**, sans attendre l'échéance |
| 08 h 30 | DPO | Confirme que des données personnelles d'abonnés sont concernées | 🔴 **Double notification : ANSSI + CNIL** |
| 09 h 00 | Communication | Rédaction du message aux usagers et du message aux agents | Validation par le DG |
| 10 h 00 | Direction générale | Information de l'autorité organisatrice et de la préfecture | — |
| 11 h 00 | Juridique | Préparation du **dépôt de plainte** | Plainte déposée le 17/03 |
| 11 h 30 | Cellule | Déclaration à l'assureur cyber | — |
| **14 h 30** | **RSSI → DG → envoi** | 🔴 **ALERTE PRÉCOCE transmise à l'autorité** (art. 23(4)(a)) | ✅ **T0 + 10 h 18 — délai de 24 h respecté avec 13 h 42 de marge** |
| 15 h 00 | Communication | Message publié sur le site institutionnel et les réseaux sociaux (art. 23(1)) | Information des usagers |
| 16 h 00 | CERT-FR | Retour dans les 24 h prévu par l'art. 23(5) : orientations techniques, indicateurs de compromission à rechercher | Assistance |
| 18 h 00 | Cellule | Point de situation. **Organisation de la relève** : deux équipes en alternance 12 h | Éviter l'épuisement |
| 22 h 00 | DSI | Souche du rançongiciel identifiée avec l'aide du CERT-FR | Recherche du point d'entrée |

### 🟢 Phase 4 — Remédiation (J+1 à J+10)

| Date | Fait marquant |
|---|---|
| **Mercredi 17/03** | Point d'entrée identifié : compte prestataire compromis, première connexion le 07/03 à 23 h 41. Dépôt de plainte. Début de la reconstruction d'un environnement d'accueil **sain** (nouveaux serveurs, nouvel Active Directory) |
| **Jeudi 18/03 — 17 h 00** | 🔴 **NOTIFICATION D'INCIDENT transmise à l'autorité** (art. 23(4)(b)) — **T0 + 60 h 48, délai de 72 h respecté**. Notification CNIL transmise en parallèle (art. 33 RGPD) |
| **Vendredi 19/03** | Restauration de l'Active Directory sur socle neuf. Réinitialisation de **tous** les mots de passe. MFA vérifié sur l'ensemble des comptes |
| **Samedi 20/03** | Restauration de l'ERP de facturation. Perte constatée : **14 heures** de données de gestion (RPO respecté : 24 h) |
| **Lundi 22/03** | Vérification d'intégrité des automates et du SCADA par l'intégrateur : **aucune modification de programme ni de consigne détectée** ✅ |
| **Mardi 23/03** | Reconnexion **progressive** du lien IT ↔ OT, sous surveillance renforcée. Retour au mode nominal |
| **Vendredi 26/03** | Rétablissement de la messagerie et du portail abonnés. Fin de la cellule de crise |
| **Mardi 30/03** | Retour d'expérience à chaud avec l'ensemble des participants |

### 📄 Phase 5 — Clôture

| Date | Action |
|---|---|
| **Jeudi 15/04/2027** | 🔴 **RAPPORT FINAL transmis à l'autorité** (art. 23(4)(d)) — **28 jours après la notification du 18/03, délai d'un mois respecté** |
| 20/04/2027 | Présentation du retour d'expérience et du plan d'amélioration au COSSI (art. 20(1)) |
| 30/04/2027 | Mise à jour de l'analyse de risques et de la PSSI (art. 21(4)) |

---

## 3. La frise des délais réglementaires

```
MAR 16/03      MER 17/03      JEU 18/03            JEU 15/04       DIM 18/04
04h12          04h12          04h12   17h00        (envoi)         (echeance)
  |              |              |       |             |               |
  T0             |              |       |             |               |
  |<-- 10h18 --> |              |       |             |               |
  |   ALERTE     |              |       |             |               |
  |   PRECOCE    |              |       |             |               |
  |   14h30 OK   |              |       |             |               |
  |              ECHEANCE 24h   |       |             |               |
  |                             ECHEANCE 72h          |               |
  |<-------- 60h48 ------------------>  |             |               |
  |                          NOTIFICATION 72h         |               |
  |                          18/03 17h00 OK           |               |
  |                                     |<-- 28 j --> |               |
  |                                     |    RAPPORT FINAL 15/04 OK   |
  |                                     |                             |
  |                                     +--- 1 mois apres la NOTIF ---+
```

> 🔴 **Le point que tout le monde rate** : le mois du rapport final court à compter de la
> **notification des 72 h** (18/03), **pas** de T0 (16/03). Échéance : 18/04/2027. Envoyé le 15/04.

---

## 4. Les notifications rédigées

Les trois notifications réglementaires, remplies avec les données du scénario, sont en annexe :

| Document | Article | Échéance | Envoyé | Fichier |
|---|---|---|---|---|
| **Alerte précoce** | 23(4)(a) | 17/03 04 h 12 | **16/03 14 h 30** ✅ | [A-alerte-precoce-24h.md](annexes/A-alerte-precoce-24h.md) |
| **Notification d'incident** | 23(4)(b) | 19/03 04 h 12 | **18/03 17 h 00** ✅ | [B-notification-72h.md](annexes/B-notification-72h.md) |
| **Rapport final** | 23(4)(d) | 18/04 | **15/04** ✅ | [C-rapport-final-1-mois.md](annexes/C-rapport-final-1-mois.md) |
| Information des usagers | 23(1) | Sans retard injustifié | 16/03 15 h 00 | [D-information-usagers.md](annexes/D-information-usagers.md) |
| Notification CNIL | art. 33 RGPD | 19/03 | 18/03 17 h 30 | [E-notification-cnil.md](annexes/E-notification-cnil.md) |

---

## 5. L'organisation de crise

### 5.1 Les deux cellules

```
        +--------------------------------------+
        |        CELLULE DE CRISE              |   DECIDE - ARBITRE - COMMUNIQUE
        |  Directeur general (directeur crise) |   Se reunit toutes les 2 h
        |  DSI - RSSI                          |
        |  Responsable exploitation            |
        |  Communication - Juridique - DPO     |
        |  SECRETAIRE DE CRISE (main courante) |
        +------------------+-------------------+
                           | points de situation
        +------------------v-------------------+
        |        CELLULE TECHNIQUE             |   ANALYSE - CONTIENT - RESTAURE
        |  Administrateurs IT et OT            |   Point toutes les heures
        |  Prestataire de reponse a incident   |
        |  Integrateur automatismes            |
        |  CERT-FR (appui)                     |
        +--------------------------------------+
```

### 5.2 Qui fait quoi

| Rôle | Titulaire | Responsabilité | Ne fait pas |
|---|---|---|---|
| **Directeur de crise** | Directeur général | Décide, arbitre, engage l'entité, valide les notifications | Ne fait pas de technique |
| **RSSI** | RSSI | Qualifie l'incident, rédige les notifications, relation CERT-FR | Ne décide pas seul de notifier |
| **DSI** | DSI | Pilote la cellule technique, confinement, restauration | — |
| **Exploitation** | Responsable exploitation | 🔴 **Garantit la continuité de la distribution d'eau** | — |
| **Communication** | Chargé de communication | Usagers, presse, élus, agents | N'improvise pas |
| **DPO** | DPO | Volet RGPD, notification CNIL | — |
| **Juridique** | Service juridique | Plainte, assurance, contrats | — |
| **Secrétaire de crise** | Assistant de direction | **Main courante horodatée** | Ne participe pas aux décisions |

> 🔑 **Le secrétaire de crise est le poste le plus sous-estimé.** Sans main courante, le rapport
> final de l'article 23(4)(d) est impossible à écrire un mois plus tard, et le respect des délais
> est indémontrable.

### 5.3 Extrait de la main courante

| Heure | Source | Fait constaté | Décision | Qui |
|---|---|---|---|---|
| 04:12 | Astreinte exploitation | Alarmes SCADA multiples ; postes du siège inaccessibles | Ouverture main courante — **T0** | Astreinte |
| 04:15 | Astreinte | Messages de rançon sur SRV-FIC-01 et SRV-ERP-02 | Appel DSI | Astreinte |
| 04:30 | RSSI | SCADA opérationnel, pas de trace de compromission OT | **Couper le lien IT/OT** | RSSI |
| 04:45 | DSI | Lien coupé (débranchement SW-CORE-02 port 24) | Automates en autonomie locale | DSI |
| 05:00 | RSSI | Grille de qualification appliquée | **Incident important** — notification requise | RSSI |
| 06:15 | DSI | Bande de sauvegarde du 12/03 intacte, hors ligne | Restauration possible | DSI |
| 14:30 | RSSI | Alerte précoce transmise, accusé n° AR-2027-0316-1430 | — | DG |

> Règle : **on n'efface jamais**. Une correction est une nouvelle ligne.

---

## 6. La grille de qualification appliquée

📗 Art. 23(3) : un incident est important s'il **a causé ou est susceptible de causer** une
perturbation opérationnelle grave ou des pertes financières, **ou** s'il **a affecté ou est
susceptible d'affecter** des tiers en causant des dommages considérables.

| Question | Réponse le 16/03 à 05 h 00 | Conclusion |
|---|---|---|
| La distribution ou la qualité de l'eau est-elle affectée, ou **susceptible** de l'être ? | Pas affectée, mais **susceptible** de l'être (propagation vers l'OT non exclue à cet instant) | ✅ Critère (a) |
| Le SCADA ou des automates sont-ils indisponibles ou suspectés compromis ? | SCADA préservé, mais suspicion non levée | ✅ Critère (a) |
| Un service à l'usager est-il interrompu plus de 4 h ? | Oui — facturation, portail abonnés, accueil téléphonique | ✅ Critère (a) |
| Des données personnelles d'abonnés sont-elles concernées ? | Oui — 240 000 abonnés | ✅ Critère (b) + RGPD |
| L'incident est-il d'origine malveillante ? | Oui — rançongiciel avéré | ✅ |
| Pertes financières estimées | > seuil défini par la direction | ✅ Critère (a) |

> ✅ **Décision : incident important.** Notification requise au titre de l'article 23.
> ⏱️ Qualification prononcée à **T0 + 48 minutes**.

> 💡 **La règle qui doit figurer dans la procédure** : *en cas de doute, on notifie.*
> L'article 30 autorise la notification volontaire ; le coût d'une notification de trop est nul,
> celui d'une notification manquante est un manquement à l'article 23.

---

## 7. Les décisions difficiles, et comment elles ont été tranchées

| Décision | Prise à | Par | Motif | Difficulté |
|---|---|---|---|---|
| **Couper le lien IT ↔ OT** | 04 h 30 | RSSI + exploitation | Suspicion de propagation | Perte de la télégestion — assumée : **la sûreté prime** |
| Notifier avant d'avoir tout compris | 08 h 00 | DG sur proposition du RSSI | Art. 23(4)(a) n'exige pas de comprendre | Réticence naturelle à « déclarer sans savoir » |
| **Ne pas payer la rançon** | 09 h 00 | DG | Décision de principe actée **avant** la crise | Pression du délai de reconstruction |
| Reconstruire sur socle neuf plutôt que restaurer en place | 17/03 | DSI + CERT-FR | Le socle existant est suspect | Rallonge le délai de 3 jours |
| Communiquer publiquement dès J0 | 15 h 00 | DG + communication | Les usagers constatent déjà les pannes | Crainte de l'effet médiatique |
| Ne pas reconnecter l'OT avant vérification d'intégrité | 22/03 | Exploitation | Risque de réinfection | 6 jours en mode dégradé, charge humaine importante |

> 🔑 **Toutes ces décisions étaient tranchées à l'avance**, par écrit, dans la procédure validée en
> COSSI. En crise, on n'invente pas : on applique ce qu'on a décidé au calme.

---

## 8. Ce qui a bien fonctionné, et ce qui a manqué

### ✅ Ce qui a sauvé la situation

| Élément | Mesure | Origine |
|---|---|---|
| **La coupure du lien IT/OT en 33 minutes** | Procédure écrite et testée | Art. 21(2)(c) |
| **La sauvegarde hors ligne intacte** | Bande sortie du robot chaque vendredi | Action **A-06** (phase 0) |
| **Les programmes automates versionnés** | Dépôt Git hors domaine | Action **A-07** (phase 0) |
| **Les modèles de notification prêts** | Rédigés au calme, disponibles sur papier | Action **A-04** (phase 0) |
| **La messagerie hors domaine** | Comptes créés et testés à froid | Action **A-09** (phase 0) |
| **Le MFA sur les comptes d'administration** | A limité la propagation | Action **A-05** (phase 0) |
| **L'autonomie locale des automates** | Régulation maintenue sans SCADA | Conception historique |

> 🎯 **Six des sept éléments proviennent de la phase 0 du plan** — celle qui coûte 95 k€ sur un
> budget total de 956 k€. C'est l'argument le plus fort de la feuille de route.

### ❌ Ce qui a manqué

| Manque | Conséquence | Action corrective | Écart |
|---|---|---|---|
| **Réseau non segmenté** | La coupure a dû être **physique et brutale**, avec perte totale de la télégestion pendant 6 jours. Avec la segmentation, l'isolement aurait été logique, immédiat et partiel | Accélérer la phase 2 | E-01 |
| **Journalisation insuffisante** | 9 jours pour identifier le point d'entrée ; certains journaux avaient tourné | Journalisation centralisée 12 mois | E-13 |
| **Horloges désynchronisées** | 20 minutes d'écart entre équipements : la chronologie a dû être reconstruite manuellement | NTP généralisé | E-13 |
| **Inventaire OT incomplet** | 3 automates découverts pendant la vérification d'intégrité, non répertoriés | Inventaire exhaustif | E-08 |
| **Compte prestataire trop privilégié** | Le vecteur initial disposait de droits d'administration du domaine | Moindre privilège, comptes séparés | E-09 |
| **Pas de détection OT** | Impossible de prouver l'absence de compromission autrement que par audit manuel | Sonde passive | E-14 |

### Le plan d'amélioration issu du retour d'expérience

| # | Action | Responsable | Échéance |
|---|---|---|---|
| REX-1 | Avancer de 3 mois le jalon de segmentation (A-22 à A-27) | DSI | Décision COSSI du 20/04 |
| REX-2 | Déployer le NTP sur l'intégralité du parc **sans attendre** le reste du projet de journalisation | DSI | 30/05/2027 |
| REX-3 | Revue immédiate des comptes prestataires à privilèges | DSI | 30/04/2027 |
| REX-4 | Ajouter au scénario d'exercice une variante « le RSSI est indisponible » | RSSI | Exercice 2028 |
| REX-5 | Formaliser la relève : nul ne reste en cellule plus de 12 h | DG | 30/05/2027 |
| REX-6 | Doubler la fréquence des tests de restauration (trimestriel → mensuel) | DSI | 30/04/2027 |

---

## 9. Ce que la segmentation aurait changé

| Moment | Sans segmentation (réel) | Avec segmentation (cible mars 2028) |
|---|---|---|
| 04 h 12 | Propagation possible vers l'OT à tout instant | ⛔ Bloquée par la règle **D-01** dès le départ |
| 04 h 30 | Décision de couper physiquement | Isolement **logique** en une commande, ou déjà effectif |
| 04 h 45 | **Perte totale de la télégestion** pendant 6 jours | Télégestion **conservée** : seuls les flux IT ↔ DMZ sont coupés |
| 06 h 15 | Sauvegardes sauvées grâce à la bande hors ligne | Sauvegardes **également protégées par D-06** |
| 22/03 | Vérification manuelle de 350 automates, 4 jours | Sonde passive + inventaire de référence : quelques heures |
| Coût | Astreinte renforcée 6 jours, ≈ 45 k€ 📕 + facturation décalée | Réduit de l'ordre de 80 % |

> 🎯 **La conclusion à présenter au COSSI** : *l'incident a été survécu grâce à la phase 0. Il aurait
> été contenu grâce à la phase 2. La segmentation ne se justifie pas par la conformité, elle se
> justifie par les six jours de télégestion perdus.*

---

## 10. Le mémo de crise (à afficher en salle de crise)

```
+--------------------------------------------------------------+
|  INCIDENT CYBER - LES 8 PREMIERS REFLEXES                    |
+--------------------------------------------------------------+
| 1. NOTER L'HEURE. C'est T0. Ouvrir la main courante.          |
| 2. NE PAS ETEINDRE les machines touchees (preuves en memoire).|
| 3. ISOLER : couper le lien IT/OT AVANT toute analyse.         |
| 4. VERIFIER que l'eau coule : mode degrade, astreinte.        |
| 5. APPELER : DSI -> RSSI -> DG. Puis le CERT-FR.              |
| 6. QUALIFIER avec la grille. En cas de doute : ON NOTIFIE.    |
| 7. NOTIFIER : alerte precoce sous 24 h, meme incomplete.      |
| 8. NE PAS REINSTALLER avant d'avoir fait les images disque.   |
+--------------------------------------------------------------+
|  DELAIS : 24 h alerte | 72 h notification |                   |
|           1 MOIS rapport final A COMPTER DE LA NOTIF 72 H     |
|  RGPD : 72 h a la CNIL si donnees personnelles (delai propre) |
+--------------------------------------------------------------+
|  CONTACTS (annuaire papier - salle de crise)                  |
|  CERT-FR ........ voir fiche contacts                         |
|  Autorite NIS2 .. MonEspaceNIS2 + courriel de secours         |
|  CNIL ........... teleservice de notification                 |
|  Assureur cyber . police n° .....                             |
|  Prefecture / ARS ..... voir fiche contacts                   |
+--------------------------------------------------------------+
```

---

## 11. Conclusion

Le scénario montre trois choses :

1. **Les délais de l'article 23 sont tenables** — à condition d'avoir écrit la procédure **avant**.
   L'alerte précoce a été envoyée à T0 + 10 h, la notification à T0 + 61 h, le rapport final 28 jours
   après la notification. Les trois échéances ont été respectées avec de la marge.
2. **La continuité du service d'eau ne dépend pas de l'informatique** — les automates ont régulé
   seuls pendant six jours. C'est une **propriété de conception**, à exiger contractuellement et à
   tester chaque année.
3. **Les mesures les moins chères sont celles qui ont sauvé la situation.** Six des sept facteurs
   décisifs proviennent de la phase 0 du plan, soit 95 k€ sur 956 k€.

📗 L'article 21(4) impose de corriger sans délai les manquements constatés : le retour d'expérience
produit six actions correctives datées, présentées au COSSI le 20 avril 2027.

---

⬅️ [Bloc 3 — Architecture](job-3-architecture.md) · 📎 [Les notifications rédigées](annexes/) ·
🏠 [Sommaire](README.md)
