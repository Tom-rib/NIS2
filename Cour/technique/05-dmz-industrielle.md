# 05 — La DMZ industrielle

> 🎯 **Objectif** : comprendre pourquoi une zone tampon est **la** pièce maîtresse d'une
> segmentation IT/OT, et ce qu'on y met.
> ⏱️ 6 minutes.

---

## 1. Le problème qu'elle résout

L'IT a **besoin** de données de l'OT : rendement des pompes, volumes produits, alarmes pour la GMAO,
mesures de qualité pour les rapports réglementaires.

Deux mauvaises solutions, une bonne :

| Solution | Verdict |
|---|---|
| ❌ Ouvrir un flux direct IT → SCADA | Le poste bureautique compromis atteint le SCADA |
| ❌ Isoler totalement (*air gap*) et transporter par clé USB | Ingérable, et la clé USB est **elle-même** un vecteur d'attaque documenté |
| ✅ **DMZ industrielle** | L'IT et l'OT ne se voient jamais ; ils se rencontrent dans une zone tampon contrôlée |

## 2. Le principe : la donnée est **recopiée**, pas **routée**

```
      ZONE IT                 DMZ INDUSTRIELLE                ZONE OT
 +---------------+        +---------------------+        +---------------+
 |   GMAO / SIG  |  lit   |  Relais OPC UA      |  ecrit |  SCADA        |
 |               |------->|  Historian miroir   |<-------|  Historian    |
 +---------------+        +---------------------+        +---------------+
        |                          |                            |
        |  4840/TCP (lecture)      |                            | 4840/TCP
        |  initie par l'IT         |    LE SCADA POUSSE ------->+ initie par l'OT
        v                          v
   Jamais de session IT ---------------------------> OT
```

Deux règles absolues :

| # | Règle | Pourquoi |
|---|---|---|
| 1 | **Aucune session ne traverse la DMZ de bout en bout** | L'IT termine sa connexion sur le serveur de la DMZ. Point. |
| 2 | **La DMZ n'initie jamais de connexion vers l'OT** | Sinon, compromettre la DMZ suffit à atteindre les automates |

Le sens des flèches est **le cœur du raisonnement** : c'est l'**OT qui pousse** vers la DMZ,
et l'**IT qui vient lire** dans la DMZ.

## 3. Ce qu'on met dans la DMZ industrielle

| Service | Rôle | Sens des flux |
|---|---|---|
| **Serveur relais OPC UA** | Expose une copie des variables du procédé, en **lecture seule** | OT → DMZ (écriture), IT → DMZ (lecture) |
| **Historian miroir** | Réplique de la base d'historique, interrogée par l'IT | OT → DMZ |
| **Serveur de mises à jour OT** (WSUS dédié, dépôt de correctifs) | Télécharge les correctifs depuis Internet, les met à disposition de l'OT en fenêtre planifiée | Internet → DMZ (sortant initié), puis OT → DMZ (l'OT vient chercher) |
| **Serveur antivirus / listes blanches OT** | Distribue les signatures sans exposer l'OT | Idem |
| **Bastion d'administration OT** | Point de passage unique et **enregistré** pour toute session d'administration | Admin → bastion → OT |
| **Serveur de saut pour les intégrateurs** | Accès prestataires, temporaire et tracé | VPN → bastion → OT |

> ⚠️ **Ce qu'on n'y met JAMAIS** : un contrôleur de domaine de l'AD bureautique, un serveur de
> fichiers partagé avec l'IT, ou un poste utilisé aussi pour la bureautique. La DMZ doit avoir sa
> **propre gestion d'identités**.

## 4. Le durcissement de la DMZ

Puisqu'elle est le point de passage, elle est **la cible**. Elle doit donc être plus dure que ce
qu'elle protège :

| Mesure | Détail |
|---|---|
| Système minimal | Aucune interface graphique, aucun service superflu |
| Comptes séparés | **Pas d'AD bureautique** — annuaire dédié OT ou comptes locaux gérés |
| MFA obligatoire | Sur le bastion, sans exception (art. 21(2)(j)) |
| Journalisation exhaustive | Toutes les sessions **enregistrées** (rejouables) |
| Correctifs | Régime IT (mensuel), car ces serveurs ne pilotent pas le procédé |
| Sauvegarde | Configuration versionnée hors zone |
| Supervision | Toute connexion inhabituelle **alerte** |

## 5. Le cas OPC UA — pourquoi ce protocole

| Critère | Modbus/TCP | **OPC UA** |
|---|---|---|
| Authentification | ❌ Aucune | ✅ Certificats, utilisateurs |
| Chiffrement | ❌ Aucun | ✅ Oui (`Sign`, `SignAndEncrypt`) |
| Modèle de données | Registres numérotés | Structuré, nommé, typé |
| Contrôle d'accès fin | ❌ Non | ✅ Par nœud, lecture seule possible |
| Port | 502/TCP | 4840/TCP |

➡️ **C'est pourquoi le flux IT ↔ DMZ est en OPC UA et non en Modbus** : on utilise le seul protocole
industriel réellement sécurisable pour franchir une frontière de zone. Modbus reste **cantonné à
l'intérieur** de la zone OT, où il est protégé par le réseau.

## 6. Et si on veut aller plus loin : la diode réseau

Pour les flux les plus sensibles, on peut employer une **diode de données** : un équipement qui
laisse **physiquement** passer l'information dans un seul sens (OT → IT), sans aucun retour possible.

| Avantage | Inconvénient |
|---|---|
| Garantie **matérielle**, pas logicielle | Coût élevé (dizaines de k€) |
| Aucun retour possible, donc aucune commande depuis l'IT | Aucun accusé de réception : protocoles adaptés nécessaires |
| Argument fort en soutenance | Rend la télémaintenance impossible par ce canal |

📕 **Choix retenu pour HydroRégie** : pas de diode en phase 1 — coût disproportionné au regard du
gain, la DMZ correctement configurée couvrant le risque principal. **À réévaluer** si un flux
temps réel vers un tiers (délégataire, autorité) devait être ouvert. Décision documentée : c'est
exactement ce que demande la proportionnalité de l'art. 21(1).

## ✅ Vérification

- [ ] Qui initie la connexion entre le SCADA et la DMZ ? Et entre l'IT et la DMZ ?
- [ ] Pourquoi ne met-on pas de contrôleur de domaine bureautique dans la DMZ ?
- [ ] Pourquoi OPC UA plutôt que Modbus pour franchir une frontière de zone ?

---

⬅️ [04 — Pare-feu](04-pare-feu-et-matrice-de-flux.md) · ➡️ [06 — Accès distant](06-acces-distant-vpn-et-bastion.md)
