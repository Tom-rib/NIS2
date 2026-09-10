# 03 — Mise en conformité & architecture

> 🎯 **Objectifs de cette fiche**
> 1. Connaître les **10 mesures de l'article 21** et savoir les traduire en actions concrètes.
> 2. Savoir conduire une **analyse d'écart** (méthode + échelle de maturité).
> 3. Comprendre **pourquoi** on segmente l'IT et l'OT, et **comment** (zones, DMZ, VLAN, pare-feu, VPN).
> 4. Savoir justifier chaque choix technique devant un jury.
>
> ⏱️ Lecture : 25 minutes.

---

# Partie A — Les mesures de l'article 21

## A.1 Ce que dit le texte

📗 **Article 21(1)** : les entités prennent des mesures **techniques, opérationnelles et
organisationnelles** appropriées et proportionnées pour gérer les risques, et pour **limiter les
conséquences** des incidents.

📗 **Article 21(2)** : ces mesures sont fondées sur une approche **« tous risques »** (*all-hazards*)
— donc pas seulement la cyberattaque : la panne, l'incendie, l'inondation, l'erreur humaine et la
défaillance d'un fournisseur comptent aussi. Elles comprennent **au moins** dix domaines.

📗 **Article 21(1), 2e alinéa** : la proportionnalité s'apprécie au regard de l'**exposition au
risque**, de la **taille** de l'entité, de la **probabilité** de survenance des incidents, de leur
**gravité**, et du **coût** des mesures. Autrement dit : on n'attend pas d'une régie des eaux le
dispositif d'une banque, mais on attend qu'elle protège ce qui fait couler l'eau.

## A.2 Les 10 domaines, traduits en français simple

| # | Article | Intitulé du texte | Ce que ça veut dire concrètement |
|---|---|---|---|
| 1 | 21(2)(a) | Politiques d'analyse des risques et de sécurité des SI | Avoir une **analyse de risques écrite** (méthode EBIOS RM par exemple) et une **PSSI** validée par la direction |
| 2 | 21(2)(b) | Gestion des incidents | Savoir **détecter, qualifier, escalader, traiter** un incident. Procédure écrite + astreinte |
| 3 | 21(2)(c) | Continuité d'activité : gestion des sauvegardes, reprise sur sinistre, gestion de crise | **PCA / PRA testés**, sauvegardes **hors ligne**, cellule de crise |
| 4 | 21(2)(d) | Sécurité de la chaîne d'approvisionnement | Clauses de sécurité dans les contrats avec les **intégrateurs et fournisseurs directs** |
| 5 | 21(2)(e) | Sécurité de l'acquisition, du développement et de la maintenance, y compris **gestion et divulgation des vulnérabilités** | Suivre les **CVE** de ses automates, avoir un plan de correctifs (et un **contournement** quand on ne peut pas patcher) |
| 6 | 21(2)(f) | Politiques et procédures pour **évaluer l'efficacité** des mesures | **Audits**, tests d'intrusion, indicateurs, revue annuelle. « Mesurer, pas croire » |
| 7 | 21(2)(g) | **Hygiène informatique de base** et formation à la cybersécurité | Mots de passe, mises à jour, moindre privilège, **sensibilisation** de tous |
| 8 | 21(2)(h) | Politiques d'usage de la **cryptographie** et, le cas échéant, du chiffrement | Chiffrer les flux d'administration, les sauvegardes, les postes nomades |
| 9 | 21(2)(i) | Sécurité des **ressources humaines**, politiques de **contrôle d'accès**, **gestion des actifs** | Arrivées/départs, **inventaire** à jour, droits revus périodiquement |
| 10 | 21(2)(j) | **Authentification multifacteur** ou continue, communications sécurisées (voix, vidéo, texte), systèmes de communication d'urgence sécurisés | **MFA** partout où c'est possible + un **moyen de communiquer en crise** quand la messagerie est tombée |

> 💡 **Le n°10 est sous-estimé.** « Communication d'urgence sécurisée » signifie : le jour où
> l'Active Directory et la messagerie sont chiffrés, comment la cellule de crise se parle-t-elle ?
> Réponse attendue : une liste papier + une messagerie hors domaine + des téléphones dédiés.

📗 **Article 21(3)** : dans la sécurité de la chaîne d'approvisionnement, l'entité doit prendre en
compte les vulnérabilités propres à **chaque fournisseur direct** et la qualité globale de leurs
pratiques de cybersécurité.

📗 **Article 21(4)** : si une entité constate qu'elle ne respecte pas ces mesures, elle prend
**sans délai** les mesures correctrices nécessaires.

---

## A.3 Conduire une analyse d'écart : la méthode

### Étape 1 — Choisir une échelle de maturité

On utilise ici une échelle à 5 niveaux (inspirée des échelles de maturité usuelles) :

| Niveau | Nom | Critère |
|---|---|---|
| 0 | Inexistant | Rien n'est fait, le sujet n'est pas identifié |
| 1 | Initialisé | Des actions existent, mais informelles et dépendantes des personnes |
| 2 | Reproductible | La pratique est écrite mais pas systématiquement appliquée |
| 3 | Défini | Procédure formalisée, appliquée, connue de tous |
| 4 | Maîtrisé | Mesuré par des indicateurs, contrôlé, amélioré |

🎯 **La cible raisonnable pour une entité essentielle est le niveau 3** sur l'ensemble des
domaines, et **4 sur les domaines critiques** (continuité, gestion des incidents, contrôle d'accès).

### Étape 2 — Coter chaque domaine

Pour chaque point de l'article 21 : constat → niveau actuel → niveau cible → écart → criticité.

### Étape 3 — Prioriser

On croise **la criticité de l'écart** et **l'effort de correction** :

```
       Effort faible          Effort eleve
     +--------------------+--------------------+
 Fort|  1. A FAIRE TOUT   |  2. PROJETS        |
impact|     DE SUITE      |     STRUCTURANTS   |
     |  (MFA, sauvegardes)|  (segmentation)    |
     +--------------------+--------------------+
Faible|  3. QUAND ON PEUT |  4. PLUS TARD      |
impact|  (inventaire)     |  (certification)   |
     +--------------------+--------------------+
```

### Étape 4 — Dater et responsabiliser

Un plan d'action sans **date** ni **nom** n'est pas un plan d'action. Format minimal :

| ID | Action | Écart couvert (art.) | Responsable | Échéance | Coût | Indicateur de fin |
|---|---|---|---|---|---|---|

➡️ L'analyse complète d'HydroRégie est dans [`Documentation/job-2-analyse-ecart.md`](Documentation/job-2-analyse-ecart.md).

---

# Partie B — L'architecture segmentée IT / OT

## B.1 Pourquoi segmenter : le raisonnement en 3 temps

1. **Le risque** : sur un réseau plat, une compromission bureautique (hameçonnage, mot de passe
   volé) donne un accès réseau direct aux automates. C'est le scénario des attaques réelles contre
   des services d'eau (accès distant mal protégé → modification de consignes).
2. **L'enjeu** : ici, l'impact n'est pas « des données volées », c'est **la qualité et la
   continuité de l'eau potable** — donc la santé publique.
3. **La réponse** : découper le réseau en **zones** de criticité homogène, et n'autoriser entre
   elles que des flux **explicitement justifiés**, à travers des **points de passage contrôlés**.

> 📗 Rattachement réglementaire : la segmentation sert directement l'art. 21(2)(a) (sécurité des SI),
> (c) (continuité), (e) (maintenance / vulnérabilités) et (i) (contrôle d'accès). La directive
> **n'impose pas** une architecture précise : c'est à l'entité de justifier ses choix.
> Le référentiel technique de référence est la norme **IEC 62443** (zones et conduits).

## B.2 Le modèle de Purdue, en une image

C'est le modèle de référence pour organiser un réseau industriel. Il empile 6 niveaux :

```
Niveau 5  |  Reseau d'entreprise (Internet, messagerie, ERP)        <- IT
Niveau 4  |  Reseau de site / bureautique metier (GMAO, SIG)        <- IT
==========|=== DMZ INDUSTRIELLE (zone tampon obligatoire) ==========
Niveau 3  |  Supervision et exploitation (SCADA, historian)         <- OT
Niveau 2  |  Controle de zone (IHM locales, postes operateur)       <- OT
Niveau 1  |  Controle : automates (API/PLC), regulateurs            <- OT
Niveau 0  |  Procede : capteurs, pompes, vannes, chloration         <- Physique
```

> 🔑 **La règle d'or** : **aucun flux ne traverse directement du niveau 4/5 vers le niveau 3 ou
> en dessous.** Tout passe par la DMZ industrielle, où un serveur relais **duplique** la donnée.
> L'IT ne parle jamais à un automate ; il lit une copie de la donnée dans la DMZ.

## B.3 Les 6 briques techniques et leur justification

| Brique | À quoi ça sert | Pourquoi ce choix ici |
|---|---|---|
| **VLAN** (802.1Q) | Découpe le réseau physique en réseaux logiques étanches | Peu coûteux, réutilise les commutateurs existants. **Attention : un VLAN seul n'est pas une mesure de sécurité** — il faut un pare-feu pour filtrer entre VLAN |
| **Pare-feu inter-zones** | Applique la politique « tout ce qui n'est pas explicitement autorisé est interdit » | C'est **lui** qui fait la sécurité, pas le VLAN. Un pare-feu dédié IT/OT évite qu'une règle bureautique ouvre l'industriel |
| **DMZ industrielle** | Zone tampon où l'IT et l'OT déposent/lisent la donnée **sans jamais se voir** | Permet la remontée d'indicateurs vers la GMAO sans exposer le SCADA |
| **Diode / flux unidirectionnel** | Laisse passer la donnée dans **un seul sens** (OT → IT) | Sur les flux de supervision les plus sensibles ; solution matérielle coûteuse, à réserver au strict nécessaire |
| **VPN + bastion** | Accès distant chiffré, nominatif, tracé, **activé à la demande** | Remplace TeamViewer permanent. Le bastion enregistre la session : preuve pour l'art. 21(2)(i) |
| **Sonde de détection passive** | Écoute le trafic industriel et alerte sur l'anormal (nouvelle station Modbus, écriture de consigne inhabituelle) | **Passive = zéro impact** sur le procédé. Indispensable pour l'art. 21(2)(b) |

## B.4 Le découpage en zones retenu

| Zone | VLAN | Réseau | Criticité | Contenu |
|---|---|---|---|---|
| Z1 — Exposition Internet | 100 | 10.100.0.0/24 | Moyenne | Portail abonnés, relais de messagerie |
| Z2 — IT bureautique | 110 | 10.110.0.0/22 | Moyenne | Postes, AD, fichiers |
| Z3 — IT métier | 120 | 10.120.0.0/24 | Haute | ERP facturation, GMAO, SIG |
| Z4 — Sauvegarde | 130 | 10.130.0.0/24 | **Critique** | Sauvegardes, copie hors ligne |
| Z5 — **DMZ industrielle** | 200 | 10.200.0.0/24 | **Critique** | Serveur relais OPC UA, historian miroir, serveur de mises à jour OT, bastion |
| Z6 — Supervision OT | 210 | 10.210.0.0/24 | **Vitale** | SCADA, historian primaire, IHM |
| Z7 — Contrôle OT | 220 | 10.220.0.0/22 | **Vitale** | Automates, RTU, IHM locales |
| Z8 — Sites distants | 230 | 10.230.0.0/22 | **Vitale** | Réservoirs, stations de relevage (VPN sur APN privé) |
| Z9 — Administration | 240 | 10.240.0.0/24 | **Critique** | Bastion d'administration, supervision, journaux |

## B.5 La matrice de flux (le cœur du livrable)

C'est **le document qui prouve** que l'architecture est réfléchie. Principe : par défaut **DENY**,
chaque ligne est une exception justifiée.

| Source | Destination | Port / protocole | Sens | Justification |
|---|---|---|---|---|
| Z3 IT métier | Z5 DMZ (relais OPC) | 4840/TCP OPC UA | → | La GMAO lit les compteurs de fonctionnement des pompes |
| Z6 SCADA | Z5 DMZ (relais OPC) | 4840/TCP OPC UA | → | Le SCADA **pousse** la donnée vers la DMZ (jamais l'inverse) |
| Z6 SCADA | Z7 Automates | 502/TCP Modbus, 2404/TCP IEC-104 | → | Pilotage : c'est le seul flux autorisé vers les automates |
| Z9 Bastion | Z6, Z7 | 22/TCP, 3389/TCP | → | Administration **uniquement** depuis le bastion, session tracée |
| Z2 IT bureautique | Z6, Z7, Z8 | **tout** | ⛔ **DENY** | 🔴 **Règle centrale : la bureautique ne parle jamais à l'industriel** |
| Z7 Automates | Internet | **tout** | ⛔ **DENY** | Un automate n'a rien à faire sur Internet |
| Z5 DMZ | Z7 Automates | **tout** | ⛔ **DENY** | La DMZ ne doit pas devenir un tremplin |
| Toutes zones | Z9 (collecteur journaux) | 514/TCP TLS | → | Journalisation centralisée (art. 21(2)(b)) |

## B.6 La continuité du service d'eau potable

📗 Exigence rattachée à l'**article 21(2)(c)** — continuité d'activité et gestion de crise.

C'est le point qui distingue un bon rendu d'un rendu générique. **L'eau doit couler même si tout
l'informatique est arrêté.** Trois niveaux de repli :

| Mode | Déclencheur | Ce qui fonctionne encore | Durée tenable |
|---|---|---|---|
| **Mode nominal** | — | Télégestion complète depuis le SCADA | — |
| **Mode dégradé** | SCADA indisponible | Les automates continuent en **autonomie locale** (régulation sur niveau et pression, chloration asservie) ; surveillance par IHM locales sur site | Plusieurs jours |
| **Mode manuel** | Automate ou site inaccessible | **Exploitation humaine** : rondes toutes les 4 h, manœuvres manuelles des vannes, dosage de chlore contrôlé par prélèvements | Quelques jours, très consommateur en personnel |

> ⚙️ **Décision d'architecture qui découle de cette exigence** : les automates doivent embarquer
> une **logique de repli autonome** et ne **jamais** dépendre du SCADA pour maintenir le service.
> C'est une exigence à écrire dans les cahiers des charges des intégrateurs (art. 21(2)(d)).

---

## ✅ Vérification de fin de fiche

- [ ] Cite les 10 domaines de l'article 21(2) sans regarder.
- [ ] Pourquoi un VLAN seul ne suffit-il pas à sécuriser ?
      <details><summary>Réponse</summary>Un VLAN isole en couche 2 mais les VLAN sont routés entre eux. Sans règles de pare-feu, tout circule. Le VLAN organise, le pare-feu protège.</details>
- [ ] Quel flux ne doit **jamais** exister dans cette architecture ?
      <details><summary>Réponse</summary>Bureautique (Z2) → industriel (Z6/Z7/Z8), directement.</details>
- [ ] Que se passe-t-il pour l'eau si le SCADA est chiffré par un rançongiciel ?

---

⬅️ [02 — Qualification](02_qualification.md) · ➡️ **Suite** : [04 — Tests & vérifications](04_tests.md)
