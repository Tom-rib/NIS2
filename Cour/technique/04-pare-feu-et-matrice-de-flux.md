# 04 — Pare-feu et matrice de flux

> 🎯 **Objectif** : savoir écrire une politique de filtrage qui protège **sans casser
> l'exploitation**, et savoir la défendre.
> ⏱️ 8 minutes.

---

## 1. Le principe fondateur

> 🔴 **Tout ce qui n'est pas explicitement autorisé est interdit** (*default deny*).

Un jeu de règles se lit **de haut en bas**, première correspondance gagnante. La dernière règle est
toujours un **DENY ALL journalisé** — journalisé, sinon on ne saura jamais ce qu'on a cassé.

## 2. La matrice de flux : le vrai livrable

Le schéma d'architecture est joli. **La matrice de flux est ce qui se met en œuvre.**

Une ligne de matrice contient **7 colonnes** :

| Source | Destination | Port / protocole | Sens | Justification métier | Validé par | Date |
|---|---|---|---|---|---|---|

> 💡 La colonne **« Justification métier »** est la plus importante. Une règle sans justification
> est une règle qu'on n'osera jamais supprimer trois ans plus tard, parce que personne ne saura à
> quoi elle sert. C'est ainsi que naissent les pare-feu passoires.

## 3. La matrice d'HydroRégie (extrait)

### ✅ Flux autorisés

| # | Source | Destination | Port | Justification |
|---|---|---|---|---|
| 1 | Z3 IT métier (GMAO) | Z5 relais OPC UA | 4840/TCP | Remontée des compteurs de fonctionnement des pompes |
| 2 | Z6 SCADA | Z5 relais OPC UA | 4840/TCP | Le SCADA **pousse** ses données vers la DMZ |
| 3 | Z6 SCADA | Z7 automates | 502/TCP, 2404/TCP | Pilotage — **seul** flux autorisé vers les automates |
| 4 | Z6 SCADA | Z8 sites distants | 2404/TCP via VPN | Télégestion des réservoirs |
| 5 | Z9 bastion | Z5, Z6, Z7 | 22/TCP, 3389/TCP | Administration tracée, depuis le bastion uniquement |
| 6 | Z5 serveur MAJ | Z6, Z7 | 445/TCP, 8530/TCP | Distribution des correctifs, en fenêtre planifiée |
| 7 | Toutes zones | Z9 collecteur | 6514/TCP (syslog TLS) | Journalisation centralisée |
| 8 | Z2 IT | Z1 exposition | 443/TCP | Accès aux services web internes |
| 9 | Z5 relais | Internet (télémaintenance éditeur) | 443/TCP sortant | Mises à jour éditeur — **sortant uniquement, sur demande** |

### ⛔ Flux explicitement interdits (les règles qui font le livrable)

| # | Source | Destination | Port | Raison |
|---|---|---|---|---|
| D1 | **Z2 IT bureautique** | **Z6, Z7, Z8** | **tout** | 🔴 **Règle centrale : la bureautique ne parle jamais à l'industriel** |
| D2 | Z7 automates | Internet | tout | Un automate n'a rien à faire sur Internet |
| D3 | Z5 DMZ | Z7 automates | tout | La DMZ ne doit pas devenir un tremplin |
| D4 | Internet | Z5, Z6, Z7, Z8 | tout entrant | Aucun flux entrant vers l'industriel |
| D5 | Z1 exposition | Z3, Z4 | tout | Un portail compromis n'atteint pas l'ERP ni les sauvegardes |
| D6 | Toute zone | Z4 sauvegarde | tout sauf le protocole de sauvegarde | Protection contre le chiffrement des sauvegardes |
| D7 | — | — | — | **DENY ALL journalisé** en dernière règle |

## 4. Traduction en règles concrètes

### OPNsense / pfSense (interface graphique, logique équivalente)

```
Interface : OT (VLAN 220)
  Regle 1  PASS  source 10.210.0.10  dest 10.220.0.0/22  port 502   (SCADA -> automates)
  Regle 2  PASS  source 10.240.0.5   dest 10.220.0.0/22  port 22    (bastion)
  Regle 3  PASS  source 10.220.0.0/22 dest 10.240.0.20   port 6514  (journaux)
  Regle 4  BLOCK source any          dest any            log        (deny all)
```

### nftables (équivalent en ligne de commande)

```bash
table inet segmentation {
  chain forward {
    type filter hook forward priority 0; policy drop;

    ct state established,related accept

    # SCADA -> automates : Modbus et IEC-104
    ip saddr 10.210.0.10 ip daddr 10.220.0.0/22 tcp dport { 502, 2404 } accept

    # Bastion -> zones administrees
    ip saddr 10.240.0.5 ip daddr { 10.200.0.0/24, 10.210.0.0/24, 10.220.0.0/22 } \
        tcp dport { 22, 3389 } accept

    # Journalisation centralisee
    ip daddr 10.240.0.20 tcp dport 6514 accept

    # Interdiction explicite et tracee : bureautique -> industriel
    ip saddr 10.110.0.0/22 ip daddr { 10.210.0.0/24, 10.220.0.0/22, 10.230.0.0/22 } \
        log prefix "BLOC-IT-VERS-OT: " drop

    # Tout le reste
    log prefix "DENY-DEFAUT: " drop
  }
}
```

> 💡 **Pourquoi écrire D1 explicitement alors que le `policy drop` suffirait ?**
> Pour **la journalisation** et pour **la démonstration**. Une règle nommée
> `BLOC-IT-VERS-OT` produit une ligne de journal identifiable : c'est une **preuve** exploitable
> lors d'un contrôle (art. 32) et une **alerte** exploitable en détection (art. 21(2)(b)).

## 5. Les 7 erreurs classiques

| ❌ Erreur | Conséquence | ✅ Correction |
|---|---|---|
| Règle `any → any` « temporaire » pour dépanner | Devient permanente | Règle avec **date d'expiration** et revue mensuelle |
| Autoriser par sous-réseau entier au lieu de l'hôte | Toute la zone devient source légitime | Autoriser **l'IP du SCADA**, pas le /24 |
| Ne pas journaliser les blocages | Aucun diagnostic possible | `log` sur les DENY significatifs |
| Oublier le trafic retour | Le flux ne fonctionne pas | Pare-feu à état : `ct state established,related accept` |
| Mettre le DENY ALL avant les PASS | Tout est bloqué | Vérifier **l'ordre** — première correspondance gagnante |
| Administrer le pare-feu depuis n'importe où | Compromission du pare-feu = fin de la segmentation | Administration **depuis Z9 uniquement**, avec MFA |
| Ne jamais réviser la matrice | Empilement de règles mortes | **Revue semestrielle** documentée (art. 21(2)(f)) |

## 6. Le cycle de vie d'une règle

```
Demande metier  ->  Analyse de risque  ->  Validation exploitation + RSSI
      -> Mise en oeuvre  ->  TEST (le flux passe / le reste ne passe pas)
      -> Documentation dans la matrice  ->  Revue semestrielle
      -> Suppression si le besoin a disparu
```

Une règle non documentée dans la matrice est une **anomalie** : elle doit être supprimée ou
régularisée. C'est un excellent indicateur d'audit (art. 21(2)(f)) :
**nombre de règles actives non présentes dans la matrice — cible : 0.**

## ✅ Vérification

- [ ] Que veut dire *default deny* et où se place cette règle ?
- [ ] Pourquoi écrire une règle de blocage explicite alors que la politique par défaut bloque déjà ?
- [ ] Quelle colonne de la matrice de flux est la plus importante à long terme ?

---

⬅️ [03 — VLAN](03-vlan-et-segmentation.md) · ➡️ [05 — DMZ industrielle](05-dmz-industrielle.md)
