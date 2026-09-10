# 01 — Préparation

> 🎯 **Objectifs de cette fiche**
> 1. Comprendre le contexte HydroRégie et pourquoi il pose problème.
> 2. Maîtriser le vocabulaire minimum (IT, OT, SCADA, entité essentielle).
> 3. Savoir de quoi on a besoin pour rejouer la partie technique.
> 4. Connaître la méthode de travail des 4 blocs.
>
> ⏱️ Lecture : 10 minutes.

---

## 1. Le contexte en 5 lignes

**HydroRégie** est une régie des eaux : elle capte, traite, stocke et distribue l'eau potable
à **450 000 habitants**. Elle facture ses abonnés, gère ses interventions, et **pilote à distance**
ses usines, ses pompes et ses réservoirs.

Le problème : son **système d'information de gestion (IT)** et son **système industriel (OT)**
partagent aujourd'hui le même réseau. Un rançongiciel qui arrive par une pièce jointe dans la
messagerie peut donc atteindre, sans aucun obstacle, l'automate qui commande une pompe de relevage.

Un courrier de l'autorité nationale vient de confirmer son statut d'**entité essentielle** NIS2.

---

## 2. Le vocabulaire minimum

Ne pas confondre ces deux mondes est **le cœur du projet**.

| Terme | Définition simple | Chez HydroRégie |
|---|---|---|
| **IT** (*Information Technology*) | L'informatique de bureau et de gestion | Messagerie, ERP de facturation, portail abonnés, GMAO, postes de travail |
| **OT** (*Operational Technology*) | L'informatique qui **pilote des choses physiques** | Automates de pompes, vannes, capteurs de chlore, superviseur SCADA |
| **SCADA** | *Supervisory Control And Data Acquisition* — le logiciel depuis lequel un opérateur voit et commande l'usine | Écrans de la salle de supervision : niveaux de réservoirs, débits, alarmes |
| **API / PLC** | *Automate Programmable Industriel* — le petit ordinateur durci qui exécute la logique (« si niveau < 2 m, démarrer la pompe ») | ~350 automates et RTU sur le territoire |
| **RTU** | *Remote Terminal Unit* — un automate déporté sur un site isolé, relié par radio ou 4G | Réservoirs et stations de relevage isolés |
| **Entité essentielle (EE)** | Statut NIS2 le plus contraignant : contrôle possible **avant** tout incident | Statut confirmé pour HydroRégie |
| **Entité importante (EI)** | Statut NIS2 allégé : contrôle **après** signalement seulement | — |

> 💡 **La différence qui compte** : en IT, la priorité est **C-I-D** (Confidentialité, Intégrité,
> Disponibilité). En OT, elle est **inversée** : d'abord la **Disponibilité** et la **Sûreté**
> des personnes, ensuite l'Intégrité, la Confidentialité en dernier. Une pompe qui s'arrête,
> c'est une ville sans eau. On ne « redémarre pas pour appliquer un correctif » une station de pompage.

---

## 3. L'existant : ce qu'on a trouvé

📕 *Hypothèse de travail — chiffres construits pour le cas d'école, cohérents avec une régie de cette taille.*

### 3.1 Chiffres de l'entité

| Donnée | Valeur |
|---|---|
| Habitants desservis | 450 000 |
| Abonnés facturés | 240 000 |
| Effectif | 380 salariés |
| Chiffre d'affaires annuel | 72 M€ |
| Total de bilan | 95 M€ |
| Communes desservies | 62 |
| Linéaire de réseau | ~1 200 km |

### 3.2 Le parc IT

- 1 domaine Active Directory (Windows Server 2016), 420 postes Windows 10/11
- ERP de facturation abonnés, portail usagers exposé sur Internet
- GMAO (maintenance), SIG (cartographie du réseau)
- Messagerie Microsoft 365, sans authentification multifacteur généralisée
- Télérelève de 60 000 compteurs communicants

### 3.3 Le parc OT

- 1 superviseur SCADA redondé au siège + 1 poste de repli à l'usine principale
- ~350 automates et RTU (Schneider M340, Siemens S7-300/1200)
- Protocoles : **Modbus/TCP**, **IEC 60870-5-104**, **OPC UA** (partiellement)
- Liaisons : fibre entre les gros sites, 4G APN privé pour les sites isolés
- 2 intégrateurs externes avec accès permanent en **TeamViewer** pour la maintenance

### 3.4 Les 7 constats qui font mal

| # | Constat | Pourquoi c'est grave |
|---|---|---|
| 1 | **Un seul réseau à plat** (10.0.0.0/8), aucun VLAN entre IT et OT | Rien n'arrête une propagation latérale |
| 2 | Le poste d'ingénierie automates est aussi un poste bureautique | Une pièce jointe piégée = accès direct aux automates |
| 3 | Accès distant intégrateurs en TeamViewer permanent, compte partagé | Pas de traçabilité, pas de révocation, pas de MFA |
| 4 | Pas de MFA sur la messagerie ni sur le VPN | Un mot de passe volé suffit |
| 5 | Sauvegardes sur un NAS unique, sur le même réseau | Le rançongiciel chiffre aussi les sauvegardes |
| 6 | Pas de journalisation centralisée, pas de supervision de sécurité | On ne voit pas l'attaque et on ne peut pas la reconstituer |
| 7 | Pas de plan de continuité formalisé pour l'exploitation en mode dégradé | En crise, on improvise |

---

## 4. De quoi tu as besoin pour rejouer la partie technique

Le projet est **réalisable sur un seul PC** avec de la virtualisation. Rien de payant.

### 4.1 Matériel minimum

- Un PC avec **16 Go de RAM** et 60 Go de disque libre (8 Go possible en réduisant les VM)
- La virtualisation activée dans le BIOS (VT-x / AMD-V)

### 4.2 Logiciels (tous libres ou gratuits)

| Logiciel | Rôle | Licence |
|---|---|---|
| **VirtualBox** ou **Proxmox VE** | Hyperviseur | GPL |
| **OPNsense** (ou pfSense) | Pare-feu / routeur inter-VLAN | BSD 2-clauses |
| **Debian 12** | Serveurs de test (côté IT et côté OT) | Libre |
| **OpenPLC** | Simule un automate Modbus/TCP | GPLv3 |
| **mbpoll** ou **ModbusPal** | Client Modbus pour tester | GPL |
| **Wireshark** | Observer les trames et prouver le blocage | GPL |
| **nmap** | Cartographier et tester la segmentation | NPSL |
| **Draw.io / Mermaid** | Schémas d'architecture | Libre |

### 4.3 Vérifier que l'environnement est prêt

```bash
# La virtualisation est-elle disponible ? (Linux)
grep -Eoc "(vmx|svm)" /proc/cpuinfo     # doit renvoyer un nombre superieur a 0

# Les outils reseau sont-ils installes ?
nmap --version
mbpoll --help | head -3
```

```powershell
# Sous Windows : la virtualisation est-elle active ?
Get-ComputerInfo -Property "HyperVRequirementVirtualizationFirmwareEnabled"
```

✅ **Vérification** : tu dois pouvoir créer une VM et lui donner deux interfaces réseau.

---

## 5. La maquette de test

L'idée : reproduire **en petit** la segmentation qu'on propose à HydroRégie.

```
            +-------------------------------------+
            |         OPNsense (pare-feu)         |
            | em0=WAN  em1=IT  em2=DMZ  em3=OT    |
            +----+---------+-------------+--------+
                 |         |             |
            VLAN 10     VLAN 20       VLAN 30
              (IT)    (DMZ ind.)        (OT)
                 |         |             |
           +-----v----+ +--v-------+ +---v---------+
           | Poste IT | | Serveur  | |  OpenPLC    |
           | Debian   | | relais   | | (automate   |
           |          | | OPC/hist.| |  simule)    |
           +----------+ +----------+ +-------------+
```

| VLAN | Nom | Réseau | Rôle |
|---|---|---|---|
| 10 | IT | 172.16.10.0/24 | Bureautique, gestion |
| 20 | DMZ-IND | 172.16.20.0/24 | Serveur relais / historian, point de passage obligé |
| 30 | OT | 172.16.30.0/24 | Automates, SCADA |

> 🎯 **Le but de la maquette** : prouver, Wireshark à l'appui, qu'un poste du VLAN 10 **ne peut
> pas** parler en Modbus (port 502) à l'automate du VLAN 30, mais que la donnée remonte quand même
> jusqu'à l'IT **en passant par la DMZ**. C'est exactement le principe du bloc 3.

---

## 6. La méthode de travail des 4 blocs

```
Bloc 1 - QUALIFIER   ->  "Sommes-nous concernes, et a quel titre ?"
   |                     Sortie : note de qualification (art. 2, 3, annexe I)
   v
Bloc 2 - MESURER     ->  "Ou en sommes-nous par rapport a l'article 21 ?"
   |                     Sortie : analyse d'ecart + feuille de route datee
   v
Bloc 3 - CONCEVOIR   ->  "A quoi doit ressembler le reseau demain ?"
   |                     Sortie : schema d'architecture argumente
   v
Bloc 4 - S'ENTRAINER ->  "Que fait-on le jour ou ca tombe ?"
                         Sortie : chronologie + notifications 24 h / 72 h / 1 mois
```

Chaque bloc **alimente le suivant** : les écarts du bloc 2 justifient l'architecture du bloc 3,
et l'architecture du bloc 3 explique pourquoi, dans le bloc 4, l'eau continue de couler.

---

## ✅ Vérification de fin de fiche

Tu dois pouvoir répondre sans relire :

- [ ] Quelle est la différence entre IT et OT ?
- [ ] Pourquoi la priorité Disponibilité / Confidentialité est-elle inversée en OT ?
- [ ] Cite 3 des 7 constats de l'audit initial.
- [ ] Quel est le rôle d'une DMZ industrielle dans la maquette ?

---

➡️ **Suite** : [02 — Qualification & cadre réglementaire](02_qualification.md)
