# Règles de pare-feu — version OPNsense (maquette)

> Les mêmes règles que [`nftables-segmentation.nft`](nftables-segmentation.nft), traduites pour
> l'interface graphique **OPNsense** — la solution retenue pour la maquette de test.
>
> Licence OPNsense : BSD 2-clauses.

---

## 1. Rappel du principe

Sur OPNsense, les règles sont évaluées **par interface**, **de haut en bas**, **première
correspondance gagnante**. La dernière règle de chaque interface est un **Block journalisé**.

> 🔴 **Erreur n°1** : placer la règle de blocage général **avant** les autorisations. Tout est alors
> bloqué, et on cherche pendant une heure.

---

## 2. Interfaces à créer

| Interface | VLAN | Réseau | Zone |
|---|---|---|---|
| `WAN` | — | — | Internet |
| `IT` | 110 | 172.16.10.0/24 *(maquette)* | Z2 |
| `DMZ` | 200 | 172.16.20.0/24 *(maquette)* | Z5 |
| `OT` | 220 | 172.16.30.0/24 *(maquette)* | Z7 |

*Chemin : Interfaces → Assignments, puis Interfaces → [nom] → Enable*

---

## 3. Alias à créer

*Chemin : Firewall → Aliases*

| Nom de l'alias | Type | Contenu | Usage |
|---|---|---|---|
| `HOTE_SCADA` | Host(s) | 172.16.30.10 | Seul autorisé à parler aux automates |
| `HOTE_RELAIS_OPC` | Host(s) | 172.16.20.20 | Relais de la DMZ |
| `HOTE_BASTION` | Host(s) | 172.16.20.5 | Administration |
| `RESEAU_OT` | Network(s) | 172.16.30.0/24 | Zone de contrôle |
| `PORTS_INDUS` | Port(s) | 502, 2404, 44818, 102 | Protocoles industriels |
| `PORTS_ADMIN` | Port(s) | 22, 3389 | Administration |

> 💡 **Toujours passer par des alias.** Le jour où le SCADA change d'adresse, on modifie **un**
> alias et non douze règles. C'est aussi ce qui rend les règles lisibles un an plus tard.

---

## 4. Règles — interface `IT` (VLAN 110)

*Chemin : Firewall → Rules → IT*

| # | Action | Source | Destination | Port | Log | Description |
|---|---|---|---|---|---|---|
| 1 | 🔴 **Block** | `IT net` | `RESEAU_OT` | any | ✅ **Oui** | **D-01 — La bureautique ne parle jamais à l'industriel** |
| 2 | 🔴 **Block** | `IT net` | `DMZ net` | any sauf 4840 | ✅ Oui | Seul OPC UA est autorisé vers la DMZ |
| 3 | ✅ Pass | `IT net` | `HOTE_RELAIS_OPC` | 4840 | Non | F-04 — La GMAO lit les données du procédé |
| 4 | ✅ Pass | `IT net` | `WAN net` | 80, 443 | Non | Navigation web |
| 5 | 🔴 **Block** | any | any | any | ✅ Oui | **D-10 — Deny all journalisé** |

---

## 5. Règles — interface `DMZ` (VLAN 200)

| # | Action | Source | Destination | Port | Log | Description |
|---|---|---|---|---|---|---|
| 1 | 🔴 **Block** | `DMZ net` | `RESEAU_OT` | any | ✅ **Oui** | **D-03 — La DMZ n'est pas un tremplin** |
| 2 | 🔴 **Block** | `DMZ net` | `IT net` | any | ✅ Oui | D-07 — La DMZ ne se connecte pas à l'IT |
| 3 | ✅ Pass | `HOTE_BASTION` | `RESEAU_OT` | `PORTS_ADMIN` | ✅ Oui | F-11 — Administration tracée depuis le bastion |
| 4 | ✅ Pass | `DMZ net` | `WAN net` | 443 | Non | F-13 — Téléchargement des correctifs, sortant |
| 5 | 🔴 **Block** | any | any | any | ✅ Oui | D-10 — Deny all journalisé |

> ⚠️ **La règle 3 déroge à la règle 1** parce qu'elle est **placée avant** ? Non : elle est placée
> **après**. C'est volontaire dans cette maquette simplifiée où le bastion est dans la DMZ — il faut
> donc soit remonter la règle 3 au-dessus de la règle 1, soit sortir le bastion de la DMZ (solution
> retenue en cible : le bastion est en zone Z9).
> **Vérifie toujours l'ordre : c'est la première correspondance qui gagne.**

---

## 6. Règles — interface `OT` (VLAN 220)

| # | Action | Source | Destination | Port | Log | Description |
|---|---|---|---|---|---|---|
| 1 | ✅ Pass | `HOTE_SCADA` | `RESEAU_OT` | 502, 2404 | Non | F-08 — Pilotage : seul flux vers les automates |
| 2 | ✅ Pass | `HOTE_SCADA` | `HOTE_RELAIS_OPC` | 4840 | Non | F-06 — Le SCADA pousse vers la DMZ |
| 3 | ✅ Pass | `OT net` | collecteur de journaux | 6514 | Non | F-14 — Journalisation |
| 4 | ✅ Pass | `OT net` | serveur NTP | 123 (UDP) | Non | F-15 — Horloge |
| 5 | 🔴 **Block** | `OT net` | `WAN net` | any | ✅ **Oui** | **D-02 — Un automate ne va pas sur Internet** |
| 6 | 🔴 **Block** | any | any | any | ✅ Oui | D-10 — Deny all journalisé |

---

## 7. Réglages complémentaires

| Réglage | Chemin | Valeur |
|---|---|---|
| Bloquer sans répondre (*drop*, pas *reject*) | Firewall → Settings → Advanced | ✅ Activer « Drop » |
| Journalisation par défaut des blocages | Firewall → Settings → Advanced | ✅ Activer |
| Envoi des journaux vers le collecteur | System → Settings → Logging / targets | `collecteur:6514`, TLS |
| Administration réservée à une zone | System → Settings → Administration | Restreindre l'accès à l'interface de gestion |
| MFA sur l'interface d'administration | System → Access → Servers | TOTP |
| Sauvegarde de configuration | System → Configuration → Backups | Automatique, exportée hors de l'équipement |

---

## 8. Vérification

```bash
# Depuis un poste du VLAN IT : doit ECHOUER
nmap -Pn -p 502 172.16.30.15         # attendu : filtered

# Depuis un poste du VLAN IT : doit REUSSIR
nc -zv 172.16.20.20 4840             # attendu : succeeded

# Suivre les blocages en direct sur OPNsense
tail -f /var/log/filter/latest.log | grep block

# Compter les tentatives par IP source
grep block /var/log/filter/latest.log | awk '{print $NF}' | sort | uniq -c | sort -rn | head
```

➡️ Le script complet de vérification :
[`../verification/test-segmentation.sh`](../verification/test-segmentation.sh)

⬅️ [Retour au dossier scripts](../README.md)
