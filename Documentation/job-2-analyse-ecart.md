# Bloc 2 — Analyse d'écart et feuille de route de mise en conformité

> **Objet** : mesurer l'écart entre la situation actuelle d'HydroRégie et les exigences de
> l'article 21 de la directive (UE) 2022/2555, puis bâtir un plan d'actions daté et responsabilisé.
> **Date** : 10 septembre 2026 · **Version** : 1.0 · **T0 du plan** : 1ᵉʳ octobre 2026
> **Classification** : Diffusion restreinte

---

## 1. Synthèse pour la direction

| Indicateur | Valeur |
|---|---|
| Domaines de l'article 21(2) évalués | **10 / 10** |
| Maturité moyenne actuelle | **0,6 / 4** |
| Maturité cible à 24 mois | **3,3 / 4** |
| Écarts identifiés | **18** |
| Écarts critiques (à traiter sous 3 mois) | **6** |
| Durée du plan | **24 mois** (octobre 2026 → septembre 2028) |
| Budget total estimé 📕 | **≈ 956 k€** dont **≈ 520 k€ d'investissement** et **≈ 436 k€ de fonctionnement sur 2 ans** |
| Amende maximale encourue en cas de manquement | **10 000 000 €** (art. 34(4)) |

> 🎯 **Le message en une phrase** : la mise en conformité coûte **moins d'un dixième** de l'amende
> maximale encourue, et **environ un tiers** du coût estimé d'un seul incident majeur
> (1,5 à 4 M€ 📕).

### Le risque majeur, en une image

```
Aujourd'hui : reseau PLAT
  [Poste bureautique] --- rien ne bloque ---> [Automate de pompe]
  Une piece jointe piegee peut arreter la distribution d'eau de 450 000 habitants.

Cible : reseau SEGMENTE
  [Poste bureautique] --X-- [pare-feu] --X-- [DMZ] --X-- [pare-feu] --X-- [Automate]
  L'incident reste dans l'IT ; l'eau continue de couler.
```

---

## 2. Méthode d'évaluation

### 2.1 Référentiel

L'évaluation porte sur les **10 domaines de l'article 21(2)** de la directive, complétés par
l'**article 20** (gouvernance) et l'**article 23** (notification). Les mesures techniques sont
appréciées au regard du **guide ANSSI sur la cybersécurité des systèmes industriels** et de la
norme **IEC 62443**, conformément à ce que permet l'article 25.

### 2.2 Échelle de maturité

| Niveau | Nom | Critère |
|---|---|---|
| **0** | Inexistant | Le sujet n'est pas identifié, rien n'est fait |
| **1** | Initialisé | Des actions existent, informelles, dépendantes des personnes |
| **2** | Reproductible | La pratique est écrite, mais pas systématiquement appliquée |
| **3** | Défini | Procédure formalisée, appliquée, connue, avec des preuves |
| **4** | Maîtrisé | Mesurée par des indicateurs, contrôlée, améliorée |

🎯 **Cible retenue** : **niveau 3 minimum** sur tous les domaines, **niveau 4** sur les quatre
domaines critiques pour une entité essentielle du secteur de l'eau : gestion des incidents (b),
continuité (c), contrôle d'accès (i), MFA et communications d'urgence (j).

### 2.3 Sources de l'évaluation 📕

Entretiens avec la DSI, l'exploitation et les deux intégrateurs ; revue documentaire ; inventaire
technique partiel ; capture réseau passive de 15 jours ; revue des comptes Active Directory ;
revue des contrats fournisseurs.

---

## 3. La cotation, domaine par domaine

| # | Art. | Domaine | Actuel | Cible | Écart | Criticité |
|---|---|---|---|---|---|---|
| 1 | 21(2)(a) | Analyse des risques et sécurité des SI | **0** | 3 | 3 | 🟠 Élevée |
| 2 | 21(2)(b) | Gestion des incidents | **1** | 4 | 3 | 🔴 **Critique** |
| 3 | 21(2)(c) | Continuité, sauvegardes, gestion de crise | **1** | 4 | 3 | 🔴 **Critique** |
| 4 | 21(2)(d) | Sécurité de la chaîne d'approvisionnement | **0** | 3 | 3 | 🟠 Élevée |
| 5 | 21(2)(e) | Acquisition, maintenance, vulnérabilités | **1** | 3 | 2 | 🟠 Élevée |
| 6 | 21(2)(f) | Évaluation de l'efficacité des mesures | **0** | 3 | 3 | 🟡 Moyenne |
| 7 | 21(2)(g) | Cyberhygiène et formation | **1** | 3 | 2 | 🟠 Élevée |
| 8 | 21(2)(h) | Cryptographie et chiffrement | **1** | 3 | 2 | 🟡 Moyenne |
| 9 | 21(2)(i) | RH, contrôle d'accès, gestion des actifs | **1** | 4 | 3 | 🔴 **Critique** |
| 10 | 21(2)(j) | MFA et communications sécurisées | **0** | 4 | 4 | 🔴 **Critique** |
| — | art. 20 | Gouvernance | **0** | 4 | 4 | 🔴 **Critique** |
| — | art. 23 | Notification des incidents | **0** | 4 | 4 | 🔴 **Critique** |

**Maturité moyenne actuelle : 0,6 / 4.**

### Représentation

```
Art. 21(2)  Niveau actuel (#) / cible (o)
(a) risques      # . . o .      0 -> 3
(b) incidents    . # . . o      1 -> 4
(c) continuite   . # . . o      1 -> 4
(d) fournisseurs # . . o .      0 -> 3
(e) vulnerab.    . # . o .      1 -> 3
(f) efficacite   # . . o .      0 -> 3
(g) hygiene      . # . o .      1 -> 3
(h) crypto       . # . o .      1 -> 3
(i) acces        . # . . o      1 -> 4
(j) MFA / comm.  # . . . o      0 -> 4
art. 20 gouv.    # . . . o      0 -> 4
art. 23 notif.   # . . . o      0 -> 4
                 0 1 2 3 4
```

---

## 4. Le détail des 18 écarts

> Format : constat factuel → risque concret → action → article couvert.

### 🔴 Écarts critiques (traitement sous 3 mois)

---

#### ECART-01 — Aucun cloisonnement entre l'IT et l'OT
- **Article** : 21(2)(a), (b), (c), (i)
- **Constat** : un plan d'adressage unique (10.0.0.0/8), aucun VLAN ni pare-feu entre la bureautique
  et les automates. Un poste bureautique peut ouvrir une session Modbus/TCP (port 502) vers
  n'importe quel automate.
- **Risque** : une compromission bureautique (hameçonnage) donne un accès direct au pilotage des
  pompes, des vannes et de la chloration. **Impact potentiel : santé publique.**
- **Action** : projet de segmentation complet — voir [bloc 3](job-3-architecture.md).
- **Maturité** : 0 → 3 · **Effort** : élevé · **Délai** : 18 mois (jalons intermédiaires dès 3 mois)

---

#### ECART-02 — Aucune procédure de notification des incidents
- **Article** : **23**
- **Constat** : aucune procédure écrite, aucun modèle de notification, aucun critère de
  qualification d'un incident important, aucun circuit de validation.
- **Risque** : dépassement des délais **24 h / 72 h / 1 mois** dès le premier incident.
  **Manquement direct** à l'article 23, sanctionnable au titre de l'article 34(4).
- **Action** : rédiger la procédure, les 3 modèles de notification, la grille de qualification et la
  liste de contacts ; les diffuser **sur papier**.
- **Maturité** : 0 → 3 · **Effort** : **faible** · **Délai** : **1 mois** 🔥
- 💡 *Écart le plus rentable du plan : quelques jours de travail, un risque de sanction supprimé.*

---

#### ECART-03 — Accès distant des intégrateurs non maîtrisé
- **Article** : 21(2)(d), (i), (j)
- **Constat** : deux intégrateurs disposent d'un accès **TeamViewer permanent** sur le poste
  d'ingénierie automates, via un **compte partagé**, sans MFA, sans traçabilité, avec un mot de
  passe transmis par courriel il y a trois ans.
- **Risque** : **le vecteur d'attaque documenté** contre les opérateurs d'eau. Aucune capacité à
  savoir qui s'est connecté ni ce qui a été modifié.
- **Action** : suppression de TeamViewer ; VPN nominatif + MFA + bastion avec enregistrement de
  session ; comptes **désactivés par défaut**, activés sur ticket pour une fenêtre limitée.
- **Maturité** : 0 → 4 · **Effort** : moyen · **Délai** : **3 mois**

---

#### ECART-04 — Sauvegardes vulnérables à un rançongiciel
- **Article** : 21(2)(c)
- **Constat** : sauvegardes sur un **NAS unique**, sur le même réseau, accessible avec les
  identifiants du domaine. Aucune copie hors ligne. Aucun test de restauration documenté depuis
  plus de 24 mois. **Les programmes automates ne sont pas sauvegardés** (ils résident sur le disque
  du poste d'ingénierie).
- **Risque** : un rançongiciel chiffre les données **et** les sauvegardes. La perte des programmes
  automates rendrait la reconstruction d'un site impossible en moins de plusieurs semaines.
- **Action** : règle **3-2-1-1-0** ; copie hors ligne (bande sortie du robot) ou stockage immuable ;
  compte de sauvegarde hors du domaine ; **versionnement des programmes automates** ; tests de
  restauration trimestriels documentés.
- **Maturité** : 1 → 4 · **Effort** : moyen · **Délai** : **3 mois**

---

#### ECART-05 — Aucune authentification multifacteur
- **Article** : 21(2)(j)
- **Constat** : pas de MFA sur la messagerie Microsoft 365, ni sur le VPN, ni sur les comptes
  d'administration.
- **Risque** : un seul mot de passe volé (hameçonnage, fuite externe, réutilisation) suffit à entrer.
- **Action** : MFA obligatoire par ordre de priorité — comptes d'administration, accès distants,
  messagerie, puis ensemble des utilisateurs.
- **Maturité** : 0 → 4 · **Effort** : **faible** · **Délai** : **3 mois** 🔥

---

#### ECART-06 — Aucune gouvernance de la sécurité
- **Article** : **20**
- **Constat** : aucune instance dédiée, aucune PSSI, aucun RSSI identifié, aucun dirigeant formé,
  aucun budget sécurité isolé.
- **Risque** : manquement direct à l'article 20 ; **responsabilité personnelle** des dirigeants
  (art. 20(1)) et interdiction temporaire d'exercer possible (art. 32(5)(b)).
- **Action** : créer le **COSSI** par délibération ; recruter ou désigner un **RSSI** avec lettre de
  mission ; former les membres de la direction ; approuver formellement PSSI et feuille de route.
- **Maturité** : 0 → 4 · **Effort** : faible à moyen · **Délai** : **3 mois**

---

### 🟠 Écarts élevés (traitement sous 9 mois)

---

#### ECART-07 — Aucune analyse de risques formalisée
- **Article** : 21(2)(a) · **Maturité** : 0 → 3 · **Délai** : 6 mois
- **Constat** : aucune analyse de risques, aucune PSSI, aucune cartographie des scénarios redoutés.
- **Risque** : impossible de justifier la **proportionnalité** des mesures devant un contrôle.
- **Action** : analyse **EBIOS Risk Manager** couvrant IT **et** OT, avec 5 scénarios stratégiques
  (rançongiciel, sabotage de la chloration, compromission par un fournisseur, indisponibilité de la
  télégestion, vol de données abonnés) ; PSSI dérivée et approuvée par le COSSI.

---

#### ECART-08 — Inventaire des actifs incomplet
- **Article** : 21(2)(i) · **Maturité** : 1 → 3 · **Délai** : 6 mois
- **Constat** : l'inventaire IT est partiel et l'inventaire OT **inexistant** — le nombre d'automates
  est estimé « environ 350 », sans liste ni versions de firmware.
- **Risque** : impossible de répondre à un avis de sécurité (« combien d'équipements concernés ? »),
  impossible de segmenter correctement, impossible de savoir ce qu'on protège.
- **Action** : inventaire exhaustif IT et OT (marque, modèle, version, localisation, criticité,
  responsable, fournisseur) ; découverte **passive** côté OT ; mise à jour continue via la GMAO.

---

#### ECART-09 — Comptes et droits non maîtrisés
- **Article** : 21(2)(i) · **Maturité** : 1 → 4 · **Délai** : 6 mois
- **Constat** : 68 comptes actifs sans connexion depuis plus de 12 mois 📕 ; comptes génériques
  partagés (`admin`, `technicien`, `scada`) ; aucune revue périodique des droits ; pas de procédure
  formalisée de départ.
- **Risque** : maintien d'accès après un départ ; impossibilité d'imputer une action.
- **Action** : revue complète, suppression des comptes génériques, nominativité, moindre privilège,
  comptes d'administration séparés des comptes bureautiques, **revue semestrielle** documentée.

---

#### ECART-10 — Aucune veille sur les vulnérabilités
- **Article** : 21(2)(e) · **Maturité** : 1 → 3 · **Délai** : 9 mois
- **Constat** : aucune veille CVE, aucun abonnement aux avis du CERT-FR, aucune politique de
  correctifs pour l'OT.
- **Risque** : exploitation de vulnérabilités connues et publiées, sur des équipements en service
  depuis 15 ans.
- **Action** : abonnement aux avis CERT-FR et éditeurs ; processus mensuel d'analyse ; politique de
  correctifs **différenciée IT / OT** ; pour l'OT non corrigeable, **mesures compensatoires
  documentées** (isolement, filtrage, surveillance renforcée) — approche explicitement admise par
  la proportionnalité de l'art. 21(1).

---

#### ECART-11 — Aucune exigence de sécurité vis-à-vis des fournisseurs
- **Article** : 21(2)(d), 21(3) · **Maturité** : 0 → 3 · **Délai** : 9 mois
- **Constat** : aucun contrat ne comporte de clause de sécurité, de délai de notification d'incident,
  ni de droit d'audit. Aucune évaluation des pratiques des intégrateurs.
- **Risque** : compromission par la chaîne d'approvisionnement, sans recours contractuel.
- **Action** : **annexe sécurité type** à insérer dans tous les contrats (notification d'incident
  sous 24 h, MFA, comptes nominatifs, droit d'audit, réversibilité, développement sécurisé) ;
  questionnaire d'évaluation des fournisseurs critiques ; clause de conformité NIS2 pour les
  fournisseurs eux-mêmes soumis à la directive.

---

#### ECART-12 — Sensibilisation quasi inexistante
- **Article** : 21(2)(g), 20(2) · **Maturité** : 1 → 3 · **Délai** : 6 mois
- **Constat** : une sensibilisation à l'arrivée, jamais renouvelée ; aucun exercice d'hameçonnage ;
  **aucun dirigeant formé** — ce qui est un manquement direct à l'article 20(2).
- **Action** : plan annuel de sensibilisation pour tous les agents ; module spécifique pour
  l'exploitation (risques OT, clés USB, accès prestataires) ; **formation obligatoire des membres du
  COSSI et de la direction** ; deux campagnes d'hameçonnage simulé par an.

---

### 🟡 Écarts moyens (traitement sous 18 mois)

---

#### ECART-13 — Aucune journalisation centralisée
- **Article** : 21(2)(b), (f) · **Maturité** : 0 → 3 · **Délai** : 12 mois
- **Constat** : journaux locaux, rétention de 7 jours sur les pare-feu, aucune corrélation, aucune
  alerte. Les horloges ne sont pas synchronisées sur l'ensemble du parc.
- **Risque** : incapacité à détecter, à qualifier et à **reconstituer** un incident — donc à écrire
  le rapport final de l'article 23(4)(d).
- **Action** : collecteur centralisé en zone d'administration isolée, rétention 12 mois, **NTP
  généralisé**, règles d'alerte, astreinte.

---

#### ECART-14 — Aucune détection sur le réseau industriel
- **Article** : 21(2)(b) · **Maturité** : 0 → 3 · **Délai** : 15 mois
- **Constat** : aucune visibilité sur ce qui circule dans le réseau OT.
- **Action** : sonde **passive** sur port miroir ; règles prioritaires : nouvel équipement,
  écriture Modbus hors SCADA, protocole inhabituel, trafic sortant depuis l'OT.

---

#### ECART-15 — Aucun plan de continuité formalisé
- **Article** : 21(2)(c) · **Maturité** : 1 → 4 · **Délai** : 12 mois
- **Constat** : les modes dégradés existent dans la pratique des exploitants, mais ne sont ni
  écrits, ni testés, ni connus des nouveaux arrivants.
- **Action** : formaliser les trois modes (nominal, dégradé autonome, manuel) ; définir RTO et RPO
  par système ; **tester la bascule en mode dégradé une fois par an** ; exercice de crise annuel.

---

#### ECART-16 — Chiffrement absent
- **Article** : 21(2)(h) · **Maturité** : 1 → 3 · **Délai** : 12 mois
- **Constat** : sauvegardes non chiffrées, postes portables non chiffrés, flux d'administration en
  clair (Telnet encore actif sur d'anciens commutateurs 📕).
- **Action** : politique de cryptographie ; chiffrement des sauvegardes et des postes nomades ;
  suppression de Telnet et HTTP au profit de SSH et HTTPS ; gestion des clés documentée.

---

#### ECART-17 — Aucune évaluation de l'efficacité des mesures
- **Article** : 21(2)(f) · **Maturité** : 0 → 3 · **Délai** : 18 mois
- **Constat** : aucun audit, aucun test d'intrusion, aucun indicateur.
- **Action** : tableau de bord trimestriel présenté au COSSI ; audit de configuration annuel ;
  test d'intrusion externe annuel sur le périmètre IT ; **audit de segmentation** après la mise en
  œuvre du bloc 3.

---

#### ECART-18 — Documentation d'architecture obsolète
- **Article** : 21(2)(a), (c) · **Maturité** : 1 → 3 · **Délai** : 12 mois
- **Constat** : les schémas réseau datent de 2019 et ne reflètent plus la réalité ; plusieurs
  liaisons ajoutées depuis ne figurent nulle part.
- **Risque** : en crise, on perd des heures à comprendre son propre réseau.
- **Action** : cartographie à jour, versionnée dans un dépôt Git, **avec une copie papier dans la
  salle de crise**, revue semestrielle.

---

## 5. Priorisation

### 5.1 Matrice impact / effort

```
              EFFORT FAIBLE                 EFFORT ELEVE
            +---------------------------+---------------------------+
   IMPACT   | 1. A FAIRE TOUT DE SUITE  | 2. PROJETS STRUCTURANTS   |
   FORT     |  E-02 notification        |  E-01 segmentation IT/OT  |
            |  E-05 MFA                 |  E-13 journalisation      |
            |  E-04 sauvegardes         |  E-14 detection OT        |
            |  E-06 gouvernance         |  E-03 acces distants      |
            +---------------------------+---------------------------+
   IMPACT   | 3. QUAND ON PEUT          | 4. PLUS TARD              |
   MODERE   |  E-08 inventaire          |  E-17 audits / tests      |
            |  E-09 revue des comptes   |  E-16 chiffrement complet |
            |  E-12 sensibilisation     |  E-11 refonte contrats    |
            |  E-18 documentation       |                           |
            +---------------------------+---------------------------+
```

### 5.2 Les 4 actions à mener en priorité absolue

| Rang | Écart | Pourquoi en premier | Délai |
|---|---|---|---|
| 1 | **E-02** procédure de notification | Coût quasi nul, supprime un risque de sanction immédiat | 1 mois |
| 2 | **E-05** MFA | Meilleur rapport protection / effort de tout le plan | 3 mois |
| 3 | **E-04** sauvegardes hors ligne | C'est ce qui permet de **survivre** à un rançongiciel | 3 mois |
| 4 | **E-03** accès distants | Ferme le vecteur d'attaque le plus documenté du secteur | 3 mois |

> 💡 **Ces quatre actions représentent environ 12 % du budget total** et couvrent une part
> majoritaire du risque de court terme. C'est l'argument à porter au COSSI dès la première séance.

---

## 6. La feuille de route

**T0 = 1ᵉʳ octobre 2026** (première réunion du COSSI).

### Vue d'ensemble

```
2026        2027                              2028
Q4    | Q1     Q2     Q3     Q4        | Q1     Q2     Q3
------+--------------------------------+------------------
PHASE 0  |  PHASE 1        |  PHASE 2          |  PHASE 3
Urgences |  Socle          |  Segmentation     |  Maitrise
3 mois   |  6 mois         |  9 mois           |  6 mois
```

---

### 🔥 PHASE 0 — Urgences (oct. → déc. 2026)

*Objectif : supprimer les risques les plus graves au moindre coût, et poser la gouvernance.*

| ID | Action | Écart | Responsable | Échéance | Coût 📕 | Preuve de clôture |
|---|---|---|---|---|---|---|
| A-01 | Créer le COSSI par délibération | E-06 | **Direction générale** | 31/10/2026 | — | Délibération + PV de la 1ʳᵉ séance |
| A-02 | Désigner le RSSI (lettre de mission signée) | E-06 | **Direction générale** | 31/10/2026 | 65 k€/an | Lettre de mission |
| A-03 | Créer le compte MonEspaceNIS2 et pré-enregistrer | art. 3(4) | **DSI** | 31/10/2026 | — | Accusé d'enregistrement |
| A-04 | Rédiger la procédure de notification + 3 modèles + grille de qualification | E-02 | **RSSI** | 30/11/2026 | — | Procédure validée en COSSI, **diffusée sur papier** |
| A-05 | Activer le MFA sur les comptes d'administration et les accès distants | E-05 | **DSI** | 30/11/2026 | 8 k€ | Capture de configuration + test |
| A-06 | Mettre en place une copie de sauvegarde **hors ligne** hebdomadaire | E-04 | **DSI** | 15/12/2026 | 35 k€ | Procédure + première bande sortie |
| A-07 | Sauvegarder et versionner **tous les programmes automates** | E-04 | **Resp. exploitation** | 15/12/2026 | 5 k€ | Dépôt Git + inventaire des programmes |
| A-08 | Supprimer TeamViewer, déployer VPN + MFA + bastion | E-03 | **DSI** + prestataire | 31/12/2026 | 45 k€ | Configuration + procédure d'intervention |
| A-09 | Constituer l'annuaire de crise **papier** et une messagerie hors domaine | E-02, art. 21(2)(j) | **RSSI** | 31/12/2026 | 2 k€ | Annuaire diffusé + test réalisé |
| A-10 | Vérifier l'assujettissement à la directive REC | — | **Juridique** | 31/12/2026 | — | Réponse écrite de l'autorité |

**Sous-total phase 0 : ≈ 95 k€ + 65 k€/an (RSSI)**

---

### 🧱 PHASE 1 — Socle (janv. → juin 2027)

*Objectif : savoir ce qu'on protège, et rendre la protection mesurable.*

| ID | Action | Écart | Responsable | Échéance | Coût 📕 | Preuve de clôture |
|---|---|---|---|---|---|---|
| A-11 | Analyse de risques EBIOS RM (IT + OT), 5 scénarios stratégiques | E-07 | **RSSI** + cabinet | 31/03/2027 | 35 k€ | Rapport EBIOS validé en COSSI |
| A-12 | Rédiger et faire approuver la **PSSI** | E-07 | **RSSI** | 30/04/2027 | — | PSSI + PV d'approbation (art. 20(1)) |
| A-13 | Inventaire exhaustif IT et OT | E-08 | **DSI** + exploitation | 31/03/2027 | 25 k€ | Base d'inventaire + rapprochement terrain |
| A-14 | Revue complète des comptes et des droits, suppression des comptes génériques | E-09 | **DSI** | 30/04/2027 | — | Rapport de revue + 0 compte générique |
| A-15 | Formation cyber des membres de la direction (art. 20(2)) | E-12 | **RH** + RSSI | 31/03/2027 | 12 k€ | **Attestations individuelles** |
| A-16 | Plan annuel de sensibilisation + 1ʳᵉ campagne d'hameçonnage simulé | E-12 | **RSSI** | 30/06/2027 | 15 k€ | Taux de participation + résultats |
| A-17 | Généraliser le MFA à l'ensemble des utilisateurs | E-05 | **DSI** | 30/06/2027 | 18 k€ | Taux de couverture > 95 % |
| A-18 | Annexe sécurité type dans les contrats + questionnaire fournisseurs | E-11 | **Achats** + RSSI | 30/06/2027 | — | Annexe validée + 5 contrats critiques renégociés |
| A-19 | Mettre en place la veille CVE et la politique de correctifs IT/OT | E-10 | **RSSI** | 30/06/2027 | 8 k€ | Procédure + premier rapport mensuel |
| A-20 | Cartographie réseau à jour, versionnée + copie papier en salle de crise | E-18 | **DSI** | 30/06/2027 | 10 k€ | Schémas datés dans le dépôt |
| A-21 | **Matrice de flux** IT/OT établie et validée par l'exploitation | E-01 | **DSI** + exploitation | 30/06/2027 | 20 k€ | Matrice signée — **prérequis du bloc 3** |

**Sous-total phase 1 : ≈ 143 k€**

---

### 🔒 PHASE 2 — Segmentation (juil. 2027 → mars 2028)

*Objectif : le cœur technique du projet — cloisonner l'IT et l'OT sans interrompre le service.*

| ID | Action | Écart | Responsable | Échéance | Coût 📕 | Preuve de clôture |
|---|---|---|---|---|---|---|
| A-22 | Acquisition des équipements (2 pare-feu, commutateurs administrables, sonde) | E-01 | **DSI** | 30/09/2027 | 180 k€ | Bons de livraison |
| A-23 | Créer les VLAN et le routage, **sans filtrage** | E-01 | **DSI** | 31/10/2027 | 40 k€ | Configurations versionnées |
| A-24 | Déployer la **DMZ industrielle** (relais OPC UA, historian miroir, serveur de MAJ) | E-01 | **DSI** + intégrateur | 31/12/2027 | 95 k€ | Recette fonctionnelle |
| A-25 | Bascule des équipements par lots, IT puis OT | E-01 | **DSI** + exploitation | 31/01/2028 | 30 k€ | Journal de bascule, aucun arrêt de service |
| A-26 | Activer le filtrage en **journalisation seule** pendant 2 semaines | E-01 | **DSI** | 15/02/2028 | — | Analyse des flux non prévus |
| A-27 | Passer en **blocage effectif**, zone par zone | E-01 | **DSI** | 15/03/2028 | — | Configurations + tests de segmentation |
| A-28 | Journalisation centralisée + NTP généralisé (12 mois de rétention) | E-13 | **DSI** | 31/12/2027 | 55 k€ | Taux de couverture > 95 % |
| A-29 | Sonde de détection **passive** sur le réseau OT | E-14 | **DSI** | 31/01/2028 | 45 k€ | Alertes fonctionnelles + inventaire de référence |
| A-30 | Chiffrement des sauvegardes et des postes nomades, suppression de Telnet | E-16 | **DSI** | 31/03/2028 | 15 k€ | Rapport de configuration |
| A-31 | **Audit de segmentation** par un tiers | E-01, E-17 | **RSSI** + auditeur | 31/03/2028 | 25 k€ | 🔴 **Rapport d'audit — la preuve maîtresse** |

**Sous-total phase 2 : ≈ 485 k€**

---

### 🎯 PHASE 3 — Maîtrise (avr. → sept. 2028)

*Objectif : passer de « mis en place » à « mesuré, testé, amélioré » (niveau 4).*

| ID | Action | Écart | Responsable | Échéance | Coût 📕 | Preuve de clôture |
|---|---|---|---|---|---|---|
| A-32 | Formaliser le PCA/PRA et les trois modes de fonctionnement | E-15 | **Resp. exploitation** + RSSI | 30/06/2028 | 25 k€ | PCA validé en COSSI |
| A-33 | **Test de bascule en mode dégradé** en conditions réelles | E-15 | **Resp. exploitation** | 31/07/2028 | 10 k€ | Compte rendu — distribution maintenue |
| A-34 | **Exercice de crise complet** avec la direction | E-15, art. 23 | **RSSI** | 31/07/2028 | 15 k€ | Compte rendu + plan d'amélioration |
| A-35 | Test de restauration complet du SCADA en bac à sable | E-04 | **DSI** | 30/06/2028 | 8 k€ | RTO mesuré < 4 h |
| A-36 | Tableau de bord d'indicateurs trimestriel au COSSI | E-17 | **RSSI** | 30/04/2028 | — | 4 tableaux de bord successifs |
| A-37 | Test d'intrusion externe sur le périmètre IT | E-17 | **RSSI** + prestataire | 30/09/2028 | 30 k€ | Rapport + plan de correction |
| A-38 | **Revue de conformité** à la publication de la loi et des décrets français | art. 5 | **Juridique** + RSSI | Déclenchée par la publication | 15 k€ | Note d'écart au droit national |
| A-39 | Revue annuelle de l'analyse de risques et de la PSSI | E-07 | **RSSI** | 30/09/2028 | — | Version 2 approuvée |

**Sous-total phase 3 : ≈ 103 k€**

---

## 7. Budget consolidé 📕

| Phase | Investissement | Fonctionnement | Total |
|---|---|---|---|
| Phase 0 — Urgences | 85 k€ | 10 k€ + RSSI | **95 k€** |
| Phase 1 — Socle | 55 k€ | 88 k€ | **143 k€** |
| Phase 2 — Segmentation | 380 k€ | 105 k€ | **485 k€** |
| Phase 3 — Maîtrise | — | 103 k€ | **103 k€** |
| Poste RSSI (2 ans) | — | 130 k€ | **130 k€** |
| **TOTAL 24 mois** | **520 k€** | **436 k€** | **≈ 956 k€** |

### Mise en perspective

| Élément de comparaison | Montant |
|---|---|
| Coût de la mise en conformité (24 mois) | **≈ 956 k€** |
| Amende maximale encourue (art. 34(4)) | **10 000 000 €** |
| Coût estimé d'un rançongiciel avec perte de la télégestion 📕 | 1,5 à 4 M€ |
| Chiffre d'affaires annuel | 72 M€ (soit **1,3 %** du CA sur 2 ans) |
| Coût d'une contamination de l'eau distribuée | **Non chiffrable** — santé publique, responsabilité pénale |

> 📕 *Les coûts sont des ordres de grandeur construits pour ce cas d'école. Ils doivent être
> confirmés par des consultations avant tout engagement budgétaire.*

---

## 8. Suivi et pilotage

### 8.1 Gouvernance du plan

| Instance | Fréquence | Rôle |
|---|---|---|
| **COSSI** (DG, DSI, RSSI, exploitation, DPO) | Trimestriel | Approuve, arbitre, suit les indicateurs — **matérialise l'art. 20(1)** |
| Comité de projet | Mensuel | Suit l'avancement des actions |
| Point hebdomadaire DSI / exploitation | Hebdomadaire | Pendant les phases 0 et 2 |

### 8.2 Indicateurs de pilotage

| Indicateur | Cible fin 2027 | Cible fin 2028 |
|---|---|---|
| Maturité moyenne art. 21 | 2,2 / 4 | **3,3 / 4** |
| Écarts critiques ouverts | 0 | 0 |
| Actions du plan réalisées à l'échéance | > 80 % | > 90 % |
| Taux de couverture MFA | 95 % | 100 % |
| Tests de restauration réussis | 4 / 4 | 4 / 4 |
| Flux IT → OT autorisés hors matrice | — | **0** |
| Comptes prestataires actifs hors intervention | 0 | 0 |
| Dirigeants formés (art. 20(2)) | 100 % | 100 % |

### 8.3 Risques du projet lui-même

| Risque | Probabilité | Impact | Parade |
|---|---|---|---|
| **Interruption du service pendant la bascule** | Moyenne | 🔴 Majeur | Bascule par lots, hors période de pointe, retour arrière préparé, phase « journalisation seule » |
| Résistance de l'exploitation à la segmentation | **Élevée** | Élevé | Associer l'exploitation **dès la matrice de flux** ; elle valide, elle ne subit pas |
| Budget non voté | Moyenne | 🔴 Majeur | Découpage en phases finançables séparément ; phase 0 à coût quasi nul |
| Refus de coopération d'un intégrateur | Moyenne | Élevé | Clause contractuelle (A-18) ; calendrier de renégociation |
| Départ du RSSI | Moyenne | Élevé | Documentation systématique, suppléant désigné |
| Écart entre la directive et la future loi française | **Élevée** | Moyen | Jalon A-38 déclenché par la publication ; mesures techniques utiles quoi qu'il arrive |
| Incident majeur **pendant** le plan | Moyenne | 🔴 Majeur | C'est précisément pourquoi E-02 (notification) et E-04 (sauvegardes) sont en phase 0 |

---

## 9. Conclusion

HydroRégie présente aujourd'hui une maturité de **0,6 / 4** au regard de l'article 21, avec
**6 écarts critiques**, dont l'absence totale de cloisonnement entre l'IT et l'OT et l'absence de
procédure de notification.

Le plan proposé porte la maturité à **3,3 / 4 en 24 mois**, pour un budget d'environ **956 k€**,
soit **1,3 % du chiffre d'affaires** sur deux ans.

Trois convictions structurent ce plan :

1. **Les quatre premières actions sont quasi gratuites et couvrent l'essentiel du risque immédiat.**
   Il n'y a aucune raison de les différer.
2. **La segmentation IT/OT est le projet structurant** : elle sert cinq des dix domaines de
   l'article 21 et c'est elle qui garantit que l'eau continue de couler pendant un incident.
3. **Ne pas attendre la loi française.** Les mesures techniques sont utiles quoi qu'il arrive ; seule
   la partie déclarative dépend des décrets, et un jalon de revue est prévu pour cela.

📗 Rappel de l'article 21(4) : une entité qui constate un manquement doit prendre **sans délai** les
mesures correctives. **Cette analyse d'écart déclenche donc, en elle-même, une obligation d'agir.**

---

⬅️ [Bloc 1 — Qualification](job-1-qualification.md) · ➡️ [Bloc 3 — Architecture](job-3-architecture.md) ·
📎 [Registre des écarts (CSV)](annexes/F-registre-des-ecarts.csv)
