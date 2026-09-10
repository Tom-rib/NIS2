# 07 — Les protocoles industriels et leurs faiblesses

> 🎯 **Objectif** : savoir dire, pour chaque protocole, **ce qu'il permet à un attaquant** — c'est
> l'argument qui justifie la segmentation.
> ⏱️ 6 minutes.

---

## 1. Le tableau de référence

| Protocole | Port | Usage | Authentification | Chiffrement |
|---|---|---|---|---|
| **Modbus/TCP** | 502/TCP | Lecture/écriture de registres | ❌ **Aucune** | ❌ **Aucun** |
| **IEC 60870-5-104** | 2404/TCP | Téléconduite (eau, énergie) | ❌ Aucune | ❌ Aucun (sauf IEC 62351) |
| **DNP3** | 20000/TCP | Téléconduite | ❌ Aucune | ❌ Aucun (sauf DNP3-SA) |
| **EtherNet/IP (CIP)** | 44818/TCP, 2222/UDP | Automates Rockwell | ❌ Faible | ❌ Aucun |
| **S7comm** | 102/TCP | Automates Siemens | ❌ Faible | ❌ Aucun |
| **BACnet** | 47808/UDP | Gestion technique de bâtiment | ❌ Aucune | ❌ Aucun |
| **OPC DA (DCOM)** | 135/TCP + plage dynamique | Ancien OPC | Windows | ❌ Non — **infiltrable** |
| ✅ **OPC UA** | 4840/TCP | Échange industriel moderne | ✅ Certificats + comptes | ✅ Signature et chiffrement |

## 2. Ce que ça veut dire concrètement

### Modbus/TCP : le cas d'école

Le protocole date de 1979 (version série) et n'a **jamais** été conçu pour un réseau ouvert. Une
trame Modbus contient : une adresse d'esclave, un code fonction, une adresse de registre, une valeur.
**Rien d'autre.** Pas d'identité, pas de signature, pas d'horodatage.

```bash
# Lire 10 registres d'entree sur l'automate 10.220.10.15
mbpoll -a 1 -t 3 -r 1 -c 10 10.220.10.15

# ECRIRE la valeur 1 dans le registre 100  <-- demarrer une pompe, par exemple
mbpoll -a 1 -t 4 -r 100 10.220.10.15 1
```

> 🔴 **Il n'y a aucune différence, pour l'automate, entre cette commande envoyée par le SCADA et la
> même commande envoyée par un poste bureautique compromis.** Le protocole ne sait pas qui parle.

C'est **l'argument massue** du bloc 3 : puisque le protocole ne peut pas se défendre, **c'est le
réseau qui doit le faire**.

### Les codes fonction Modbus à connaître

| Code | Fonction | Danger |
|---|---|---|
| 01 / 02 | Lire bobines / entrées | Reconnaissance |
| 03 / 04 | Lire registres | Reconnaissance |
| **05** | **Écrire une bobine** | 🔴 Ouvrir/fermer une vanne, démarrer une pompe |
| **06 / 16** | **Écrire un ou plusieurs registres** | 🔴 Modifier une consigne (dosage de chlore, seuil de niveau) |
| **08** | Diagnostic (dont *restart communications*) | 🔴 Peut perturber l'automate |

> 💡 **Détection utile** : une sonde passive qui alerte dès qu'un **code fonction d'écriture (05,
> 06, 16)** provient d'une adresse IP autre que celle du SCADA. C'est une règle simple, peu bruyante
> et à très forte valeur.

## 3. Pourquoi on ne peut pas « simplement chiffrer »

| Obstacle | Explication |
|---|---|
| L'automate ne sait pas faire | Un M340 de 2010 n'a ni TLS ni la puissance de calcul pour |
| La contrainte temps réel | Certaines régulations tolèrent quelques dizaines de millisecondes de latence, pas plus |
| Le remplacement coûte cher | 350 automates à remplacer, en service, sans couper l'eau |
| La certification du procédé | Modifier une chaîne de traitement peut imposer une requalification |

➡️ **La réponse est architecturale, pas cryptographique** : on cantonne les protocoles non
sécurisés à l'intérieur d'une zone, et on ne franchit les frontières de zone qu'avec **OPC UA**
(authentifié et chiffré). C'est une **mesure compensatoire**, explicitement admise par la logique
de proportionnalité de l'art. 21(1) et par la gestion des vulnérabilités de l'art. 21(2)(e).

## 4. La migration progressive vers OPC UA

| Étape | Action | Horizon 📕 |
|---|---|---|
| 1 | OPC UA pour **tous les nouveaux** équipements (clause d'achat) | Immédiat |
| 2 | Passerelle Modbus → OPC UA en frontière de zone | 6 mois |
| 3 | Migration des automates les plus critiques lors des renouvellements | 3 à 10 ans |
| 4 | Modbus **cantonné** aux segments terminaux, jamais routé entre zones | Permanent |

## 5. Les autres faiblesses à connaître

| Faiblesse | Où | Contre-mesure |
|---|---|---|
| **Mots de passe par défaut** sur automates et IHM | Partout | Inventaire + changement, consigné |
| **Serveurs web embarqués** obsolètes | Automates et RTU | Désactiver si inutile, sinon filtrer |
| **Ports d'ingénierie ouverts** (téléchargement de programme) | Automates | Commutateur à clé en position RUN, filtrage |
| **Firmwares non signés** | Nombreux équipements anciens | Contrôle des sources, accès physique restreint |
| **Clés USB** de mise à jour | Postes d'ingénierie | Poste de décontamination dédié |

## ✅ Vérification

- [ ] Pourquoi Modbus/TCP est-il dangereux sur un réseau partagé ?
- [ ] Quels codes fonction Modbus doivent déclencher une alerte ?
- [ ] Pourquoi ne peut-on pas simplement chiffrer les échanges avec un automate ancien ?
- [ ] Quel protocole utilise-t-on pour franchir une frontière de zone, et pourquoi ?

---

⬅️ [06 — Accès distant](06-acces-distant-vpn-et-bastion.md) · ➡️ [08 — Détection et journalisation](08-detection-et-journalisation.md)
