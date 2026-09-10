# 01 — IT vs OT : deux mondes, deux priorités

> 🎯 **Objectif** : comprendre pourquoi on ne sécurise pas un automate comme un serveur de fichiers.
> ⏱️ 6 minutes.

---

## 1. La définition

| | **IT** — *Information Technology* | **OT** — *Operational Technology* |
|---|---|---|
| Rôle | Traiter de l'**information** | Piloter un **procédé physique** |
| Exemples | Messagerie, ERP, serveur de fichiers, AD | Automate, SCADA, capteur, variateur de pompe |
| Ce qui casse en cas de panne | Un service numérique | **Une pompe, une vanne, une chloration** |
| Conséquence extrême | Perte de données, arrêt d'activité | **Atteinte à la santé ou à la sécurité des personnes** |

## 2. La triade inversée — le point clé

```
        IT                          OT
   C  Confidentialite          D  Disponibilite   <- priorite absolue
   I  Integrite                I  Integrite
   D  Disponibilite            C  Confidentialite <- souvent secondaire
                              (+ S  Surete des personnes, au-dessus de tout)
```

**Pourquoi ?** Une fuite de la liste des abonnés est grave. Une pompe de relevage arrêtée pendant
6 heures, c'est un quartier sans eau — et potentiellement une dépression du réseau qui aspire des
contaminants. La disponibilité **est** la sécurité.

## 3. Les 8 différences qui changent la façon de travailler

| Sujet | IT | OT |
|---|---|---|
| **Durée de vie du matériel** | 3 à 5 ans | **15 à 25 ans** — des automates de 2003 tournent encore |
| **Correctifs** | Automatiques, mensuels | Rares, planifiés à l'arrêt, souvent **impossibles** (perte de garantie, certification du procédé) |
| **Redémarrage** | Anodin | **Interdit** sans procédure — le procédé s'arrête |
| **Systèmes d'exploitation** | Supportés | Windows XP / 7 embarqué, firmware propriétaire |
| **Antivirus** | Standard | Parfois impossible : il consomme du CPU ou déclenche des faux positifs bloquants |
| **Protocoles** | TLS partout | Modbus, IEC-104 : **ni authentification ni chiffrement** |
| **Contrainte temps réel** | Rare | Forte : une latence ajoutée peut fausser une régulation |
| **Qui administre** | La DSI | **L'exploitation**, souvent avec un intégrateur externe |

> 💡 **La conséquence pratique** : en OT, on **ne corrige pas**, on **compense**. Si un automate ne
> peut pas être mis à jour, on l'isole derrière un pare-feu et on surveille son trafic. C'est ce
> qu'on appelle une **mesure compensatoire**, parfaitement admise par l'art. 21(2)(e).

## 4. La cohabitation forcée

Historiquement, l'OT était **physiquement isolé** (*air gap*). Ce n'est plus vrai :

| Besoin métier | Ce qu'il a créé comme lien IT ↔ OT |
|---|---|
| Suivre les consommations et les rendements | Export de données du SCADA vers la GMAO / le SIG |
| Maintenance à distance des automates | Accès distant de l'intégrateur |
| Télégestion des sites isolés | Liaisons 4G / radio |
| Reporting réglementaire (qualité de l'eau) | Extraction automatisée de mesures |
| Économies | Mutualisation de l'infrastructure réseau ← **la cause de la situation d'HydroRégie** |

➡️ L'*air gap* total est un mythe aujourd'hui. L'objectif n'est pas de le rétablir, mais de
**maîtriser les points de passage**. C'est exactement l'objet de la DMZ industrielle.

## 5. Les erreurs classiques d'un informaticien lâché dans un réseau OT

| ❌ Erreur | Conséquence possible | ✅ La bonne pratique |
|---|---|---|
| Lancer un `nmap -A` sur le réseau industriel | **Plantage d'automate**, arrêt de procédé | Découverte **passive** d'abord (`tcpdump`), scan bridé et planifié ensuite |
| Pousser une mise à jour Windows sur un poste SCADA | Perte de la supervision | Fenêtre de maintenance, validation de l'éditeur, retour arrière prêt |
| Installer un antivirus classique sur une IHM | Blocage d'un exécutable métier | Liste blanche d'applications (*allow-listing*) |
| Changer un mot de passe d'automate sans prévenir | L'intégrateur ne peut plus intervenir | Coordination avec l'exploitation |
| Couper un flux « inutile » | Arrêt d'une régulation | **Matrice de flux validée par l'exploitation** avant tout filtrage |

> 🔑 **La règle d'or** : en OT, **l'exploitation a le dernier mot sur la sûreté**. Le RSSI propose,
> l'exploitant valide. Une mesure de sécurité qui met en danger le procédé n'est pas une mesure de
> sécurité.

## ✅ Vérification

- [ ] Pourquoi la disponibilité passe-t-elle avant la confidentialité en OT ?
- [ ] Que fait-on quand un automate ne peut pas être corrigé ?
- [ ] Pourquoi l'*air gap* n'existe-t-il plus en pratique ?

---

➡️ [02 — Le modèle de Purdue](02-modele-de-purdue.md) · 🏠 [Sommaire](../README.md)
