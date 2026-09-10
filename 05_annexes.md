# 05 — Annexes

> 🎯 **À quoi sert cette fiche** : c'est le mémo qu'on ouvre **pendant** le travail — glossaire,
> commandes, ports industriels, dépannage, modèles, sources. Rien à apprendre, tout à retrouver vite.

---

## 1. Glossaire

### Réglementaire

| Terme | Définition |
|---|---|
| **NIS2** | Directive (UE) 2022/2555 du 14 décembre 2022 sur un niveau élevé commun de cybersécurité dans l'Union |
| **Directive** | Texte européen fixant un objectif ; chaque État le transpose dans son droit national |
| **Règlement** | Texte européen **directement applicable**, sans transposition (ex. RGPD, DORA) |
| **Entité essentielle (EE)** | Statut NIS2 le plus contraignant — supervision *ex ante* possible (art. 32) |
| **Entité importante (EI)** | Statut NIS2 allégé — supervision *ex post* seulement (art. 33) |
| **Incident important / significatif** | Incident qui cause une perturbation opérationnelle grave, une perte financière, ou un dommage considérable à des tiers (art. 23(3)) |
| **Alerte précoce** | Premier signalement, dans les **24 h** (art. 23(4)(a)) |
| **Notification d'incident** | Signalement étayé, dans les **72 h** (art. 23(4)(b)) |
| **Rapport final** | Bilan complet, dans **1 mois** après la notification (art. 23(4)(d)) |
| **CSIRT** | *Computer Security Incident Response Team* — équipe nationale de réponse à incident (art. 10-11) |
| **ANSSI** | Agence nationale de la sécurité des systèmes d'information — autorité compétente et CSIRT national en France |
| **ENISA** | Agence de l'Union européenne pour la cybersécurité |
| **MonEspaceNIS2** | Plateforme ANSSI d'enregistrement des entités NIS2 |
| **Directive REC** | Directive (UE) 2022/2557 sur la résilience des entités critiques — le pendant « physique » de NIS2 |
| **DORA** | Règlement (UE) 2022/2554, régime spécifique au secteur financier (art. 4 NIS2 : *lex specialis*) |
| **EBIOS RM** | Méthode française d'analyse de risques (ANSSI), adaptée à l'art. 21(2)(a) |

### Technique

| Terme | Définition |
|---|---|
| **IT** | Informatique de gestion (bureautique, ERP, messagerie) |
| **OT** | Informatique industrielle qui pilote un procédé physique |
| **ICS** | *Industrial Control System* — terme générique pour les systèmes de contrôle industriel |
| **SCADA** | Logiciel de supervision et de commande à distance d'un procédé |
| **API / PLC** | Automate programmable industriel |
| **RTU** | Automate déporté sur un site isolé |
| **IHM / HMI** | Interface homme-machine (écran d'exploitation) |
| **Historian** | Base de données qui archive les mesures du procédé dans le temps |
| **DMZ** | *DeMilitarized Zone* — zone tampon entre deux réseaux qui ne doivent pas se voir |
| **VLAN** | Réseau logique isolé au sein d'un même réseau physique (802.1Q) |
| **Bastion** | Serveur unique par lequel passent toutes les sessions d'administration, tracées |
| **Diode réseau** | Équipement laissant physiquement passer les données dans un seul sens |
| **IEC 62443** | Norme internationale de cybersécurité des systèmes d'automatisation industrielle (modèle zones/conduits) |
| **Purdue** | Modèle de référence à 6 niveaux pour structurer un réseau industriel |
| **RTO / RPO** | Durée maximale d'interruption admissible / perte de données maximale admissible |
| **PCA / PRA** | Plan de continuité / de reprise d'activité |

---

## 2. Les ports industriels à connaître

> 🔥 Ce tableau sert à écrire les règles de pare-feu **et** à repérer une anomalie dans un scan.

| Port | Protocole | Usage | Sécurisé nativement ? |
|---|---|---|---|
| **502/TCP** | **Modbus/TCP** | Lecture/écriture de registres d'automates | ❌ **Aucune authentification, aucun chiffrement** |
| **2404/TCP** | IEC 60870-5-104 | Téléconduite (énergie, eau) | ❌ Non (sauf IEC 62351) |
| **20000/TCP** | DNP3 | Téléconduite (Amérique du Nord surtout) | ❌ Non (sauf DNP3-SA) |
| **44818/TCP**, 2222/UDP | EtherNet/IP (CIP) | Automates Rockwell/Allen-Bradley | ❌ Non |
| **102/TCP** | S7comm / ISO-TSAP | Automates Siemens | ❌ Non (S7comm+ partiellement) |
| **4840/TCP** | **OPC UA** | Échange de données industrielles moderne | ✅ **Oui** — signature + chiffrement possibles |
| **135/TCP + plages** | OPC DA (DCOM) | Ancien OPC | ❌ Non, et très difficile à filtrer |
| **47808/UDP** | BACnet | Gestion technique de bâtiment | ❌ Non |
| **1911/TCP, 4911/TCP** | Niagara Fox | GTB Tridium | ❌ Non |

> 💡 **Le message à retenir** : la quasi-totalité des protocoles industriels historiques
> **n'ont ni authentification ni chiffrement**. Ils ont été conçus pour un réseau supposé fermé.
> C'est exactement pour cela que la sécurité doit être apportée **par le réseau** (segmentation),
> et non par le protocole. C'est l'argument central du bloc 3.

---

## 3. Commandes utiles

### 3.1 Cartographier (avec précaution)

```bash
# Decouverte passive (aucun paquet envoye) : la seule methode sans risque en OT
sudo tcpdump -i eth0 -nn -c 2000 -w capture-ot.pcap

# Decouverte active TRES prudente cote OT : jamais de -A, -sV agressif ni de scripts
nmap -sn 10.220.0.0/22                 # ping sweep uniquement
nmap -Pn -sT -p 502,102,2404 --max-rate 10 10.220.10.0/24   # debit bride
```

> ⚠️ **Avertissement OT** : un scan agressif peut **planter un automate ancien**. Sur un réseau
> industriel en production : découverte passive d'abord, scan actif seulement en fenêtre planifiée,
> avec l'exploitant présent et une procédure de retour arrière. Jamais d'initiative individuelle.

### 3.2 Tester un filtrage

```bash
nc -zv 10.200.0.20 4840          # test d'un port TCP
nmap -Pn -p 502 10.220.10.15     # etat du port : open / closed / filtered
traceroute -T -p 502 10.220.10.15  # ou le paquet meurt-il ?
```

### 3.3 Lire les journaux d'un pare-feu OPNsense

```bash
# Les blocages recents
tail -f /var/log/filter/latest.log | grep block

# Compter les tentatives par IP source (top 10)
grep block /var/log/filter/latest.log | awk '{print $NF}' | sort | uniq -c | sort -rn | head
```

### 3.4 VLAN sous Linux (utile pour la maquette)

```bash
# Creer une interface taguee VLAN 30 sur eth0
sudo ip link add link eth0 name eth0.30 type vlan id 30
sudo ip addr add 172.16.30.10/24 dev eth0.30
sudo ip link set eth0.30 up

# Verifier
ip -d link show eth0.30
```

### 3.5 Modbus (lecture seule pour tester)

```bash
mbpoll -a 1 -t 3 -r 1 -c 10 10.220.10.15    # lire 10 registres d'entree
# -a : adresse esclave   -t 3 : registres d'entree   -r : premier registre   -c : nombre
```

---

## 4. Dépannage

| Symptôme | Cause probable | Vérification |
|---|---|---|
| Le VLAN ne passe pas entre deux commutateurs | Port non configuré en *trunk*, ou VLAN absent du trunk | `show interfaces trunk` |
| Tout est bloqué après ajout du pare-feu | Règle *deny any* placée **avant** les règles d'autorisation | Relire l'ordre des règles : il est évalué **de haut en bas** |
| Le SCADA ne voit plus un automate | Flux Modbus non autorisé dans la matrice, ou route manquante | Journaux du pare-feu, puis `traceroute -T -p 502` |
| Le VPN se connecte mais rien ne passe | Réseaux poussés (*split tunneling*) incomplets | Table de routage du client : `ip route` |
| Un poste se retrouve dans le mauvais VLAN | VLAN non balisé (*untagged*) mal affecté sur le port d'accès | `show vlan brief` |
| Le scan nmap renvoie `closed` au lieu de `filtered` | Le pare-feu **rejette** (RST) au lieu de **jeter** (drop) | Passer la règle en `drop` : ne rien répondre du tout |
| L'automate redémarre pendant un scan | Pile réseau ancienne saturée | **Arrêter le scan immédiatement**, prévenir l'exploitant, documenter |

---

## 5. Modèles réutilisables

### 5.1 Ligne de matrice de flux

```
| Source | Destination | Port/proto | Sens | Justification metier | Valide par | Date |
```

### 5.2 Fiche d'écart

```markdown
### ECART-XX — <titre court>
- **Article NIS2** : 21(2)(x)
- **Constat** : <ce qui a ete observe, factuellement>
- **Risque** : <consequence concrete si rien n'est fait>
- **Maturite actuelle / cible** : 1 / 3
- **Action** : <ce qu'on fait>
- **Responsable** : <nom, fonction>
- **Echeance** : <AAAA-MM-JJ>
- **Preuve de cloture** : <document ou test qui prouvera que c'est fait>
```

### 5.3 Entrée de registre d'incident (art. 21(2)(b))

```
Date/heure detection | Source de detection | Description | Systemes touches |
Qualification (significatif O/N) | Justification | Decisions | Notifications envoyees | Cloture
```

---

## 6. Erreurs classiques à ne pas commettre dans le rendu

| ❌ Erreur | ✅ À faire à la place |
|---|---|
| Écrire « la loi NIS2 » | Écrire « la directive (UE) 2022/2555 » — et signaler que la transposition française est en cours |
| Citer une obligation sans article | Toujours rattacher : « art. 21(2)(c) » |
| Confondre les délais RGPD et NIS2 | RGPD = 72 h à la CNIL (art. 33 RGPD). NIS2 = **24 h / 72 h / 1 mois** à l'autorité NIS2. Les deux peuvent s'appliquer en même temps |
| Dire « on chiffre tout, c'est plus sûr » en OT | Le chiffrement peut casser une supervision temps réel : on justifie **où** on chiffre |
| Proposer une segmentation sans matrice de flux | La matrice **est** le livrable ; le schéma n'en est que l'illustration |
| Oublier la continuité du service | En OT, le pire n'est pas la fuite de données, c'est **l'arrêt du service** |
| Présenter une action non faite comme faite | Distinguer clairement « réalisé », « en cours », « planifié » |

---

## 7. Sources

### Textes

| Source | Lien |
|---|---|
| Directive (UE) 2022/2555 (NIS2) | <https://eur-lex.europa.eu/eli/dir/2022/2555/oj> |
| Directive (UE) 2022/2557 (REC — entités critiques) | <https://eur-lex.europa.eu/eli/dir/2022/2557/oj> |
| Recommandation 2003/361/CE (définition des PME) | <https://eur-lex.europa.eu/eli/reco/2003/361/oj> |
| Directive (UE) 2020/2184 (eau destinée à la consommation humaine) | <https://eur-lex.europa.eu/eli/dir/2020/2184/oj> |
| Règlement d'exécution (UE) 2024/2690 (exigences techniques art. 21, entités numériques) | <https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj> |

### Autorités

| Source | Lien |
|---|---|
| ANSSI — Directive NIS 2 | <https://messervices.cyber.gouv.fr/nis2> |
| MonEspaceNIS2 — FAQ officielle | <https://aide.monespacenis2.cyber.gouv.fr/> |
| Dossier législatif — projet de loi résilience | <https://www.legifrance.gouv.fr/dossierlegislatif/JORFDOLE000050349138/> |
| ENISA — NIS Directive | <https://www.enisa.europa.eu/topics/nis-directive> |
| CERT-FR — alertes et avis | <https://www.cert.ssi.gouv.fr/> |

### Guides techniques utiles

| Source | Sujet |
|---|---|
| ANSSI — *La cybersécurité des systèmes industriels* | Méthode de classification et mesures OT |
| ANSSI — *Guide d'hygiène informatique* | Les 42 mesures de base (art. 21(2)(g)) |
| IEC 62443 | Zones, conduits, niveaux de sécurité en environnement industriel |
| ANSSI — EBIOS Risk Manager | Analyse de risques (art. 21(2)(a)) |

---

⬅️ [04 — Tests](04_tests.md) · 🏠 [README](README.md)
