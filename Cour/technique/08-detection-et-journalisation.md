# 08 — Détection et journalisation

> 🎯 **Objectif** : savoir **voir** ce qui se passe, sans perturber le procédé — et pouvoir
> reconstituer les faits après coup.
> ⏱️ 6 minutes.

---

## 1. Pourquoi c'est indispensable

📗 Trois articles convergent :

| Article | Exigence |
|---|---|
| 21(2)(b) | Gestion des incidents → il faut d'abord les **détecter** |
| 23(4)(a) | Alerte précoce **dans les 24 h après en avoir eu connaissance** → sans détection, l'horloge ne démarre jamais… jusqu'au jour où c'est l'attaquant qui vous prévient |
| 32(2) | L'autorité peut demander des **preuves** → sans journaux, aucune preuve |

📕 **Constat de départ chez HydroRégie** : aucune journalisation centralisée. Les journaux des
pare-feu tournent sur 7 jours en local, ceux des automates n'existent pas. Un incident vieux de
trois semaines serait **impossible à reconstituer**.

## 2. Que journaliser, et combien de temps

| Source | Événements à collecter | Durée de conservation 📕 |
|---|---|---|
| Pare-feu | Blocages significatifs, changements de règles | 12 mois |
| Active Directory | Authentifications, échecs, élévations, créations de comptes | 12 mois |
| Bastion | **Toutes** les sessions, avec enregistrement rejouable | 12 mois |
| VPN | Connexions, déconnexions, comptes utilisés | 12 mois |
| SCADA | Connexions opérateurs, changements de consigne, acquittements d'alarme | 12 mois |
| Sonde OT | Nouveaux équipements, écritures Modbus, protocoles inhabituels | 12 mois |
| Serveurs | Démarrages, arrêts, installations, erreurs critiques | 6 mois |
| Sauvegardes | Succès/échec, tests de restauration | 24 mois |

> ⚠️ **Durées à confirmer** avec le DPO : la conservation de journaux contenant des identifiants
> relève aussi du RGPD (minimisation, durée proportionnée).

## 3. L'architecture de collecte

```
  Pare-feu ---syslog TLS 6514--+
  AD / serveurs ---------------+
  Bastion ---------------------+---> COLLECTEUR (zone Z9)  ---> Stockage
  SCADA -----------------------+         |                      (WORM/immuable)
  Sonde OT --------------------+         v
                                    Regles d'alerte -> astreinte
```

**Deux principes** :

1. 🔴 **Le collecteur est dans une zone à part (Z9)**, et **rien ne peut en sortir vers les autres
   zones**. Un attaquant qui compromet un serveur ne doit pas pouvoir effacer ses traces.
2. Les flux de journaux vont **toujours de la zone vers le collecteur**, jamais l'inverse.

Solutions libres : **Wazuh** (GPLv2), **Graylog** (SSPL — attention à la licence), la suite
**OpenSearch** (Apache 2.0), ou simplement **rsyslog + Loki**. 📕 Choix retenu : **Wazuh**, pour
son agent multiplateforme et ses règles prêtes à l'emploi.

## 4. La détection en OT : passive, toujours

> 🔴 **En OT, une sonde est passive.** Elle écoute une copie du trafic sur un **port miroir**
> (SPAN) ou via un **TAP** réseau. Elle n'envoie **rien** sur le réseau industriel.

```
[Commutateur OT] --port miroir (SPAN)--> [Sonde de detection]
                                              |
                                              +-- ne transmet RIEN vers l'OT
                                              +-- envoie ses alertes vers Z9
```

Solutions libres : **Zeek** (BSD), **Suricata** (GPLv2) avec les règles ICS, **Malcolm** (dérivé
CISA, licence Apache 2.0).

### Les 6 règles de détection à forte valeur en OT

| # | Détection | Pourquoi c'est efficace |
|---|---|---|
| 1 | **Nouvelle adresse MAC / IP** apparue sur le VLAN OT | Un réseau industriel est **statique** : toute nouveauté est suspecte |
| 2 | **Écriture Modbus (codes 05, 06, 16)** depuis une IP autre que le SCADA | Ne devrait **jamais** arriver |
| 3 | **Protocole inhabituel** dans le VLAN OT (SMB, HTTP, DNS vers l'extérieur) | Signature classique d'un outil d'attaque |
| 4 | **Balayage de ports** dans le VLAN OT | Reconnaissance |
| 5 | **Téléchargement de programme automate** hors fenêtre de maintenance | Modification de la logique de commande |
| 6 | **Trafic sortant vers Internet** depuis une zone OT | Exfiltration ou commande à distance |

> 💡 **La règle n°1 est la plus rentable.** Un réseau OT ne change quasiment jamais : un inventaire
> figé plus une alerte sur toute nouveauté donne un taux de faux positifs très faible, pour un coût
> quasi nul.

## 5. Les indicateurs à suivre (art. 21(2)(f))

| Indicateur | Cible 📕 |
|---|---|
| Taux de couverture de la journalisation (sources connectées / sources totales) | > 95 % |
| Délai moyen de détection d'un incident | < 1 h |
| Nombre d'alertes critiques non traitées sous 24 h | 0 |
| Nombre d'équipements OT non inventoriés découverts par la sonde | 0 |
| Règles de pare-feu actives absentes de la matrice de flux | 0 |
| Comptes prestataires actifs hors intervention | 0 |
| Délai de restauration mesuré lors du dernier test | < RTO (4 h) |

Ces indicateurs alimentent le tableau de bord trimestriel du COSSI (art. 20(1)).

## 6. Ce qu'il faut préparer **avant** la crise

| Élément | Pourquoi |
|---|---|
| Horloge **synchronisée** (NTP) sur tous les équipements | Sans horodatage cohérent, la chronologie du bloc 4 est incontestablement fausse |
| Journaux **hors ligne** ou immuables | Un rançongiciel efface les journaux |
| Procédure d'**extraction rapide** des journaux | Le CSIRT en demandera dès l'alerte précoce |
| **Inventaire de référence** du réseau OT | Pour savoir ce qui est normal |

> 🔑 **L'horloge est le détail qui tue.** Une chronologie de crise construite sur des équipements
> désynchronisés de 20 minutes est inexploitable — et décrédibilise toute la notification.

## ✅ Vérification

- [ ] Pourquoi une sonde OT doit-elle être passive ?
- [ ] Pourquoi le collecteur de journaux est-il isolé dans sa propre zone ?
- [ ] Quelle est la règle de détection la plus rentable en OT, et pourquoi ?
- [ ] Que se passe-t-il si les horloges ne sont pas synchronisées ?

---

⬅️ [07 — Protocoles](07-protocoles-industriels.md) · ➡️ [09 — Sauvegardes et continuité](09-sauvegardes-et-continuite.md)
