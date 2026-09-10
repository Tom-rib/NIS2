# 06 — Accès distant : VPN et bastion

> 🎯 **Objectif** : remplacer proprement un TeamViewer permanent par un accès **nominatif,
> temporaire, tracé et à double facteur**.
> ⏱️ 7 minutes.

---

## 1. Le problème de départ

📕 Chez HydroRégie : **deux intégrateurs** disposent d'un accès **TeamViewer permanent** sur le poste
d'ingénierie automates, avec un **compte partagé** et un mot de passe transmis par courriel il y a
trois ans.

| Ce qui cloche | Article NIS2 concerné |
|---|---|
| Compte **partagé** : impossible de savoir **qui** s'est connecté | 21(2)(i) contrôle d'accès |
| Accès **permanent** : ouvert 365 jours par an pour 4 interventions | 21(2)(i) moindre privilège |
| **Pas de MFA** | 21(2)(j) |
| **Pas de traçabilité** de ce qui a été fait | 21(2)(b) gestion des incidents |
| Contournement du pare-feu (sortie 443 chiffrée) | 21(2)(a) |
| **Aucune clause contractuelle** de sécurité avec l'intégrateur | 21(2)(d) |

> 🔴 C'est **le vecteur d'attaque documenté** contre les petits opérateurs d'eau : accès distant mal
> protégé, puis modification de consignes de traitement. Ce point est prioritaire.

## 2. L'architecture cible

```
  Integrateur                Internet            HydroRegie
 +------------+                              +--------------------+
 | Poste      |  1. VPN + MFA   ==========>  | Concentrateur VPN  |
 | integrateur|                              |   (zone Z9)        |
 +------------+                              +---------+----------+
                                                       | 2. session tracee
                                             +---------v----------+
                                             |  BASTION (Z5 DMZ)  |
                                             |  enregistrement    |
                                             +---------+----------+
                                                       | 3. protocole cible uniquement
                                             +---------v----------+
                                             | Automate / SCADA   |
                                             +--------------------+

  4. Acces ACTIVE A LA DEMANDE, pour une duree limitee, puis desactive
```

## 3. Les 6 exigences non négociables

| # | Exigence | Mise en œuvre |
|---|---|---|
| 1 | **Compte nominatif** | Un compte par intervenant, jamais de compte de société |
| 2 | **MFA** | Application d'authentification ou clé matérielle — art. 21(2)(j) |
| 3 | **Activation à la demande** | Le compte est **désactivé par défaut** ; il est activé sur ticket, pour une fenêtre définie |
| 4 | **Passage obligatoire par le bastion** | Aucun accès direct depuis le VPN vers l'OT |
| 5 | **Enregistrement de session** | Rejouable, conservé selon la durée définie par la politique |
| 6 | **Périmètre minimal** | L'intégrateur A voit les automates A, pas ceux de l'intégrateur B |

## 4. La procédure d'intervention (📕 proposition)

```
1. L'integrateur ouvre un TICKET (objet, equipements, creneau demande)
2. L'exploitation VALIDE  (impact procede ? fenetre acceptable ?)
3. Le RSSI ACTIVE le compte pour la duree demandee (+ 1 h de marge)
4. Intervention  ->  session enregistree, actions journalisees
5. L'integrateur CLOTURE le ticket avec un compte rendu ecrit
6. Desactivation AUTOMATIQUE a l'echeance
7. Revue MENSUELLE : liste des acces actifs -> cible = 0 en dehors des interventions
```

> 💡 **L'automatisation compte** : si la désactivation dépend d'un humain qui doit y penser le
> vendredi soir, elle n'aura pas lieu. Elle doit être **portée par l'outil** (expiration de compte,
> tâche planifiée).

## 5. Choix technique du VPN

| Solution | Avantages | Inconvénients | Verdict 📕 |
|---|---|---|---|
| **WireGuard** | Simple, rapide, code réduit, libre (GPLv2) | Pas de MFA natif — à coupler avec un portail ou un bastion | ✅ **Retenu** pour les sites distants (Z8) |
| **OpenVPN** | Mature, MFA facile, libre (GPLv2) | Plus lent, configuration plus lourde | ✅ **Retenu** pour les accès prestataires |
| **IPsec / IKEv2** | Standard, supporté par tous les équipements | Configuration délicate, NAT parfois pénible | Pour les liaisons site à site |
| Solution propriétaire d'éditeur | Intégrée à l'outil | Boîte noire, dépendance fournisseur | ❌ Écarté |

📕 **Décision retenue** : OpenVPN + MFA pour les accès humains, WireGuard pour les tunnels site à
site vers les réservoirs et stations. Deux usages, deux outils, tous deux libres.

## 6. Le bastion

| Fonction | Pourquoi |
|---|---|
| **Point de passage unique** | Une seule porte à surveiller au lieu de 350 |
| **Enregistrement de session** | Preuve pour l'art. 21(2)(i), et outil d'investigation en cas d'incident |
| **Coffre à secrets** | L'intervenant ne connaît **jamais** le mot de passe de l'équipement cible |
| **Traçabilité par personne** | On sait qui, quand, sur quoi, et ce qui a été tapé |

Solutions libres : **Apache Guacamole** (accès web RDP/SSH/VNC, licence Apache 2.0),
**Teleport** édition communautaire, ou **The Bastion** d'OVH (GPLv3). 📕 Choix retenu :
**Apache Guacamole**, pour sa simplicité de déploiement et son enregistrement de session natif.

## 7. Le cas des sites distants (Z8)

Les réservoirs et stations de relevage communiquent par **4G sur APN privé**. Ce n'est **pas**
suffisant : l'APN privé isole du reste d'Internet mais ne chiffre pas de bout en bout et ne protège
pas d'un équipement compromis sur le même APN.

➡️ **Chaque RTU établit un tunnel WireGuard** vers le concentrateur, avec une **clé propre par
site**. Un site compromis ne donne accès qu'à lui-même.

```bash
# Cote concentrateur : une cle publique par site, un /32 par site
[Peer]
PublicKey = <cle-publique-reservoir-nord>
AllowedIPs = 10.230.1.12/32          # UN SEUL hote, pas le /22
PersistentKeepalive = 25
```

> 🔑 **`AllowedIPs` en /32** : c'est ce qui empêche un site compromis d'usurper l'adresse d'un autre
> site. Une erreur fréquente est d'y mettre le sous-réseau entier.

## ✅ Vérification

- [ ] Pourquoi un accès permanent est-il un écart, même avec un bon mot de passe ?
- [ ] Que doit-il se passer automatiquement à la fin d'une fenêtre d'intervention ?
- [ ] À quoi sert un coffre à secrets dans un bastion ?
- [ ] Pourquoi `AllowedIPs` doit-il être en /32 par site ?

---

⬅️ [05 — DMZ](05-dmz-industrielle.md) · ➡️ [07 — Protocoles industriels](07-protocoles-industriels.md)
