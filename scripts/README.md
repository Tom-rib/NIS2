# 🧰 scripts/ — fichiers de configuration et scripts

> Tous les fichiers de ce dossier sont **des modèles commentés**, écrits pour la maquette décrite
> dans [`01_preparation.md`](../01_preparation.md) et pour l'architecture du
> [bloc 3](../Documentation/job-3-architecture.md).
>
> 🔴 **Ils ne s'appliquent jamais tels quels en production.** Adresses, interfaces et noms
> d'équipements sont à adapter, et toute mise en œuvre côté OT suit la procédure de migration
> par étapes (journalisation seule d'abord).

---

## Contenu

| Fichier | Rôle | Où il est utilisé |
|---|---|---|
| [`reseau/vlan-switch.cfg`](reseau/vlan-switch.cfg) | Configuration type d'un commutateur : VLAN, ports d'accès, trunk, durcissement | Bloc 3, étape 3 de la migration |
| [`reseau/wireguard-site-distant.conf`](reseau/wireguard-site-distant.conf) | Tunnel VPN d'un réservoir ou d'une station de relevage | Bloc 3, zone Z8 |
| [`pare-feu/nftables-segmentation.nft`](pare-feu/nftables-segmentation.nft) | Règles de filtrage complètes issues de la matrice de flux | Bloc 3, étapes 5 et 6 |
| [`pare-feu/opnsense-regles.md`](pare-feu/opnsense-regles.md) | Les mêmes règles, en version interface graphique OPNsense | Maquette |
| [`verification/test-segmentation.sh`](verification/test-segmentation.sh) | Teste automatiquement que le blocage fonctionne **et** que les flux légitimes passent | [`04_tests.md`](../04_tests.md) |
| [`verification/inventaire-passif.sh`](verification/inventaire-passif.sh) | Découverte **passive** du réseau OT, sans émettre un seul paquet | Écart E-08 |
| [`sauvegarde/sauvegarde-3-2-1.sh`](sauvegarde/sauvegarde-3-2-1.sh) | Sauvegarde chiffrée avec vérification d'intégrité et rapport | Écart E-04 |
| [`documentation/`](documentation/) | Régénération de `Documentation.md` et `Documentation.docx` à partir des livrables | Rendu |

---

## ⚠️ Avertissement OT

Avant d'exécuter quoi que ce soit sur un réseau industriel en production :

1. **Découverte passive d'abord.** Un scan actif peut faire tomber un automate ancien.
2. **Fenêtre planifiée**, avec l'exploitant présent et une procédure de retour arrière.
3. **Jamais d'initiative individuelle.** L'exploitation a le dernier mot sur la sûreté.

---

## Licences des outils employés

| Outil | Licence |
|---|---|
| nftables | GPLv2 |
| WireGuard | GPLv2 |
| OPNsense | BSD 2-clauses |
| nmap | Nmap Public Source License |
| tcpdump / libpcap | BSD |
| OpenPLC | GPLv3 |
| mbpoll | GPLv3 |

⬅️ [Retour au README principal](../README.md)
