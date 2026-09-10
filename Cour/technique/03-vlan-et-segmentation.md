# 03 — VLAN et segmentation

> 🎯 **Objectif** : savoir découper un réseau plat en VLAN, comprendre trunk / access, et savoir
> pourquoi le VLAN **ne suffit pas**.
> ⏱️ 8 minutes.

---

## 1. Le problème du réseau plat

HydroRégie utilise aujourd'hui **10.0.0.0/8** pour tout : postes, serveurs, SCADA, automates.

```
Consequence : tout le monde parle a tout le monde.
Un poste bureautique compromis peut, sans franchir aucun equipement de filtrage,
ouvrir une session Modbus/TCP (port 502) vers une pompe de relevage.
```

Un même domaine de diffusion, c'est aussi : ARP spoofing possible partout, tempêtes de diffusion,
et une visibilité totale du réseau pour l'attaquant.

## 2. Le VLAN en 3 minutes

Un **VLAN** (*Virtual LAN*, norme **802.1Q**) crée plusieurs réseaux logiques sur un même
équipement physique. Chaque trame se voit ajouter une **étiquette** de 4 octets contenant un
identifiant (VID) de 1 à 4094.

| Type de port | Rôle | Étiquetage |
|---|---|---|
| **Access** (accès) | Raccorde un équipement final (PC, automate) | Trames **non étiquetées** ; le commutateur ajoute le VLAN à l'entrée |
| **Trunk** | Relie deux commutateurs ou un commutateur au pare-feu | Trames **étiquetées** ; transporte plusieurs VLAN |

```
[PC bureautique] --access VLAN 110--+
                                    |
[Automate]       --access VLAN 220--+--[Commutateur]==trunk(110,220,...)==[Pare-feu]
```

## 3. 🔴 Le point que les jurys adorent

> **Un VLAN n'est PAS une mesure de sécurité à lui seul.**

Trois raisons :

1. Les VLAN doivent être **routés** entre eux pour que l'exploitation fonctionne. Sans règles de
   filtrage, le routeur laisse tout passer : on a juste déplacé le problème.
2. Un VLAN mal configuré est contournable (*VLAN hopping* par double étiquetage, ou par négociation
   automatique de trunk).
3. Un VLAN protège du **bruit**, pas de l'**intention**.

✅ **La bonne formulation** : *« le VLAN organise le réseau, le pare-feu le protège. »*

## 4. Le plan d'adressage retenu chez HydroRégie

| VLAN | Zone | Réseau | Passerelle | Contenu |
|---|---|---|---|---|
| 100 | Z1 Exposition | 10.100.0.0/24 | .254 | Portail abonnés, relais mail |
| 110 | Z2 IT bureautique | 10.110.0.0/22 | .254 | 420 postes, AD, fichiers |
| 120 | Z3 IT métier | 10.120.0.0/24 | .254 | ERP, GMAO, SIG |
| 130 | Z4 Sauvegarde | 10.130.0.0/24 | .254 | Serveur de sauvegarde, stockage immuable |
| 200 | Z5 **DMZ industrielle** | 10.200.0.0/24 | .254 | Relais OPC UA, historian miroir, serveur MAJ, bastion |
| 210 | Z6 Supervision OT | 10.210.0.0/24 | .254 | SCADA, historian primaire |
| 220 | Z7 Contrôle OT | 10.220.0.0/22 | .254 | Automates, IHM locales |
| 230 | Z8 Sites distants | 10.230.0.0/22 | .254 | RTU réservoirs et stations (VPN) |
| 240 | Z9 Administration | 10.240.0.0/24 | .254 | Bastion, supervision, collecteur de journaux |

> 💡 **Astuce de lisibilité** : faire correspondre le numéro de VLAN au 2ᵉ octet de l'adresse
> (VLAN 210 → 10.210.x.x). Un an plus tard, on lit une adresse et on sait immédiatement dans quelle
> zone on est. C'est un gain de temps considérable en crise.

## 5. Configuration type (commutateur)

```
! ---- Creation des VLAN ----
vlan 110
 name IT-BUREAUTIQUE
vlan 220
 name OT-CONTROLE
!
! ---- Port d'acces : un automate ----
interface GigabitEthernet0/5
 description Automate station de relevage Nord
 switchport mode access
 switchport access vlan 220
 switchport nonegotiate          ! interdit la negociation de trunk (anti VLAN hopping)
 spanning-tree portfast
 spanning-tree bpduguard enable
!
! ---- Lien montant vers le pare-feu ----
interface GigabitEthernet0/24
 description Trunk vers pare-feu OT
 switchport mode trunk
 switchport trunk allowed vlan 200,210,220,230   ! liste EXPLICITE
 switchport trunk native vlan 999                ! VLAN natif inutilise et non route
 switchport nonegotiate
```

### Les 4 durcissements à ne pas oublier

| Mesure | Pourquoi |
|---|---|
| `switchport nonegotiate` | Empêche un poste de négocier un trunk (attaque de *switch spoofing*) |
| VLAN natif **dédié et inutilisé** (999) | Empêche le *double tagging* |
| `switchport trunk allowed vlan <liste>` | Un trunk ne transporte que ce dont il a besoin |
| Désactiver les ports non utilisés (`shutdown`) | Un port libre dans un local technique est une porte d'entrée |

## 6. Migration depuis un réseau plat : la méthode en 6 étapes

C'est **le point qui inquiète l'exploitation**. Il faut un plan sans interruption de service.

| Étape | Action | Risque |
|---|---|---|
| 1 | **Cartographier** les flux réels (capture passive pendant 2 à 4 semaines, y compris un week-end et une astreinte) | Nul |
| 2 | Rédiger la **matrice de flux** et la faire **valider par l'exploitation** | Nul |
| 3 | Créer les VLAN et le routage, **sans filtrage** (mode ouvert) | Faible |
| 4 | Basculer les équipements **par lots**, en commençant par l'IT | Modéré — prévoir un retour arrière |
| 5 | Activer le filtrage en mode **journalisation seule** (*log only*) pendant 2 semaines | Faible — révèle les flux oubliés |
| 6 | Passer en **blocage** zone par zone, en commençant par la moins critique | Maîtrisé |

> 🔑 **L'étape 5 est celle qu'on saute et qu'on regrette.** Elle révèle les flux non documentés
> (sonde de qualité qui envoie ses mesures en direct, imprimante de laboratoire, licence flottante
> d'un logiciel métier…) **avant** de casser quoi que ce soit.

## ✅ Vérification

- [ ] Différence entre port access et port trunk ?
- [ ] Pourquoi un VLAN seul ne sécurise-t-il pas ?
- [ ] Que fait `switchport nonegotiate` et contre quoi protège-t-il ?
- [ ] Pourquoi passer par une phase « journalisation seule » ?

---

⬅️ [02 — Purdue](02-modele-de-purdue.md) · ➡️ [04 — Pare-feu et matrice de flux](04-pare-feu-et-matrice-de-flux.md)
