# 🖼️ schemas/ — schémas d'architecture

> Les schémas sont écrits en **Mermaid** : ils sont versionnés comme du texte (donc `git diff`
> fonctionne) et **GitHub les affiche directement** dans le navigateur.

| Fichier | Contenu | Format |
|---|---|---|
| [`architecture-avant.mmd`](architecture-avant.mmd) · `.png` | L'existant : réseau plat, aucun cloisonnement | Mermaid + PNG |
| [`architecture-cible.svg`](architecture-cible.svg) · `.png` | 🔴 **La cible, version présentation** — mise en page maîtrisée | SVG + PNG 2400 px |
| [`architecture-apres.mmd`](architecture-apres.mmd) · `.png` | La cible, version Mermaid (source versionnable) | Mermaid + PNG |
| [`flux-notification.mmd`](flux-notification.mmd) · `.png` | Le processus de notification 24 h / 72 h / 1 mois | Mermaid + PNG |

> ⚠️ **Pourquoi deux versions de l'architecture cible ?**
> Le rendu automatique de Mermaid (`architecture-apres.png`) place la **DMZ tout en bas**, sous la
> zone OT — parce que le flux « l'OT pousse vers la DMZ » tire la DMZ vers le bas dans son moteur de
> placement. C'est exact sémantiquement, mais **ça contredit visuellement le message** : la DMZ doit
> apparaître *entre* l'IT et l'OT.
> ➡️ Pour toute présentation ou impression, utiliser **`architecture-cible.svg`**, dont la mise en
> page est fixée à la main. Le fichier Mermaid reste utile comme source légère à versionner.

### Régénérer les images

```bash
# Les diagrammes Mermaid (necessite Node ; utilise Edge plutot que de telecharger Chromium)
npx -y @mermaid-js/mermaid-cli@11 -i schemas/flux-notification.mmd -o schemas/flux-notification.png -w 2400 -b white -p pptr-config.json

# Le schema cible : SVG vers PNG haute definition
msedge --headless=new --disable-gpu --force-device-scale-factor=1.5 --window-size=1600,1120 \
       --screenshot=schemas/architecture-cible.png file:///.../schemas/architecture-cible.svg
```

---

## 1. AVANT — le réseau plat

```mermaid
flowchart TB
    NET(("Internet"))
    subgraph PLAT["RESEAU UNIQUE 10.0.0.0/8 - AUCUN CLOISONNEMENT"]
        P1["420 postes bureautiques"]
        AD["Active Directory"]
        ERP["ERP facturation"]
        NAS["NAS de sauvegarde"]
        ING["Poste d'ingenierie automates"]
        SC["SUPERVISEUR SCADA"]
        AU["350 automates et RTU"]
    end
    PROC["Pompes - Vannes - Chloration"]

    NET --> PLAT
    P1 --- AD
    P1 --- ERP
    P1 --- NAS
    P1 --- ING
    P1 -->|"Modbus 502 : RIEN NE BLOQUE"| AU
    ING --- SC
    SC --- AU
    AU --> PROC
```

> 🔴 **Le problème en une flèche** : un poste bureautique peut ouvrir une session Modbus/TCP vers
> un automate, sans franchir le moindre équipement de filtrage.

---

## 2. APRÈS — le réseau segmenté

```mermaid
flowchart TB
    NET(("Internet"))

    subgraph Z1["Z1 Exposition - VLAN 100"]
        PORT["Portail abonnes"]
    end

    subgraph ZIT["ZONE IT"]
        Z2["Z2 Bureautique - VLAN 110<br/>420 postes, AD"]
        Z3["Z3 Metier - VLAN 120<br/>ERP, GMAO, SIG"]
        Z4["Z4 Sauvegarde - VLAN 130<br/>Stockage immuable"]
    end

    FW1{{"PARE-FEU 1"}}

    subgraph Z5["Z5 DMZ INDUSTRIELLE - VLAN 200"]
        OPC["Relais OPC UA"]
        HM["Historian miroir"]
        MAJ["Serveur de MAJ OT"]
    end

    FW2{{"PARE-FEU 2"}}

    subgraph ZOT["ZONE OT"]
        Z6["Z6 Supervision - VLAN 210<br/>SCADA, historian"]
        Z7["Z7 Controle - VLAN 220<br/>350 automates"]
        Z8["Z8 Sites distants - VLAN 230<br/>Reservoirs (VPN)"]
    end

    PROC["Pompes - Vannes - Chloration"]
    Z9["Z9 Administration - VLAN 240<br/>Bastion, journaux, NTP"]

    NET --> PORT
    PORT -->|443| Z3
    Z2 --> FW1
    Z3 -->|4840 OPC UA| FW1
    FW1 --> OPC
    Z6 -->|"4840 : l'OT POUSSE"| FW2
    FW2 --> OPC
    Z6 -->|"502 / 2404"| Z7
    Z6 -->|VPN| Z8
    Z7 --> PROC
    Z8 --> PROC
    Z9 -.->|admin tracee| FW2
    ZIT -.->|syslog| Z9
    ZOT -.->|syslog| Z9

    Z2 x--x ZOT
```

> ✅ **Ce qui change** : plus aucun chemin direct entre la bureautique et l'industriel.
> L'OT **pousse** ses données dans la DMZ, l'IT **vient les lire**. Aucune session ne traverse.

---

## 3. Le processus de notification

```mermaid
flowchart TB
    D["DETECTION<br/>Noter l'heure = T0"]
    Q{"Incident IMPORTANT ?<br/>art. 23(3)"}
    NON["Consigner au registre<br/>art. 21(2)(b)"]
    VOL{"Doute ?"}
    A24["ALERTE PRECOCE<br/>sous 24 h<br/>art. 23(4)(a)"]
    REP["Reponse du CSIRT<br/>sous 24 h<br/>art. 23(5)"]
    N72["NOTIFICATION<br/>sous 72 h<br/>art. 23(4)(b)"]
    USA["Information des usagers<br/>art. 23(1)"]
    CNIL["Notification CNIL<br/>72 h - art. 33 RGPD"]
    ENC{"Incident<br/>toujours en cours ?"}
    AVA["RAPPORT D'AVANCEMENT<br/>art. 23(4)(e)"]
    FIN["RAPPORT FINAL<br/>1 mois APRES LA NOTIF 72 h<br/>art. 23(4)(d)"]
    REX["Retour d'experience<br/>art. 21(2)(f) et 21(4)"]

    D --> Q
    Q -->|Non| VOL
    VOL -->|Oui| A24
    VOL -->|Non| NON
    Q -->|Oui| A24
    A24 --> REP
    A24 --> N72
    N72 --> USA
    N72 --> CNIL
    N72 --> ENC
    ENC -->|Oui| AVA
    ENC -->|Non| FIN
    AVA -->|1 mois apres traitement| FIN
    FIN --> REX
```

> 🔴 **Le piège** : le mois du rapport final court à compter de la **notification des 72 h**,
> pas de T0.

---

## 4. Comment exporter ces schémas en image

Pour une soutenance ou un document Word :

```bash
# Avec mermaid-cli (npm, licence MIT)
npx @mermaid-js/mermaid-cli -i architecture-apres.mmd -o architecture-apres.png -w 2400
```

Ou par copier-coller dans l'éditeur en ligne **mermaid.live**, puis export PNG / SVG.

⬅️ [Retour au README principal](../README.md)
