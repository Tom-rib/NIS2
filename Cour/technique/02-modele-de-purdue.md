# 02 — Le modèle de Purdue

> 🎯 **Objectif** : savoir dessiner et expliquer les 6 niveaux, et en déduire où placer les
> pare-feu.
> ⏱️ 8 minutes. **La base du bloc 3.**

---

## 1. D'où ça vient

Le **PERA** (*Purdue Enterprise Reference Architecture*), conçu dans les années 1990 à l'université
Purdue, est devenu le modèle de référence pour structurer un réseau industriel. Il est repris par la
norme **IEC 62443** sous la forme du modèle **« zones et conduits »**.

## 2. Les 6 niveaux

```
+--------------------------------------------------------------+
| Niveau 5 : RESEAU D'ENTREPRISE                          [IT]  |
|   Internet, messagerie, ERP, portail abonnes                  |
+--------------------------------------------------------------+
| Niveau 4 : RESEAU DE SITE / METIER                      [IT]  |
|   GMAO, SIG, bureautique d'exploitation                       |
+==============================================================+
|            *** DMZ INDUSTRIELLE ***  (niveau 3.5)             |
|   Serveur relais OPC UA, historian miroir, serveur de MAJ,    |
|   bastion d'administration OT                                 |
+==============================================================+
| Niveau 3 : SUPERVISION / EXPLOITATION                   [OT]  |
|   SCADA, historian primaire, serveurs d'alarmes               |
+--------------------------------------------------------------+
| Niveau 2 : CONTROLE DE ZONE                             [OT]  |
|   IHM locales, postes operateurs de site                      |
+--------------------------------------------------------------+
| Niveau 1 : CONTROLE                                     [OT]  |
|   Automates (API/PLC), RTU, regulateurs                       |
+--------------------------------------------------------------+
| Niveau 0 : PROCEDE                                  [PHYSIQUE]|
|   Capteurs, pompes, vannes, analyseurs de chlore              |
+--------------------------------------------------------------+
```

## 3. La règle d'or

> 🔴 **Aucun flux ne traverse directement les niveaux 4/5 vers les niveaux 3 et inférieurs.**
> Tout passe par la **DMZ industrielle**, où la donnée est **recopiée**, jamais routée.

Deux corollaires :

1. **L'IT ne parle jamais à un automate.** Il lit une **copie** de la donnée dans la DMZ.
2. **Le SCADA pousse** vers la DMZ ; la DMZ **n'initie jamais** vers le SCADA ni vers les automates.
   Sinon, compromettre la DMZ suffirait à atteindre le procédé.

## 4. Où placer les pare-feu

| Position | Rôle | Priorité |
|---|---|---|
| Entre niveau 5 et Internet | Pare-feu périmétrique classique | Existant |
| **Entre niveaux 4/5 et la DMZ industrielle** | 🔴 **Le pare-feu qui compte** — sépare IT et OT | **P0** |
| **Entre la DMZ et le niveau 3** | Second filtre, empêche le rebond depuis la DMZ | **P0** |
| Entre niveaux 3 et 2/1 | Filtrage fin par site ou par zone de procédé | P1 |
| Entre sites distants et le cœur OT | Terminaison VPN + filtrage | P1 |

> 💡 **Architecture à deux pare-feu** : idéalement, le pare-feu haut (IT ↔ DMZ) et le pare-feu bas
> (DMZ ↔ OT) sont **de constructeurs différents**. Une vulnérabilité sur l'un ne compromet pas
> l'autre. C'est plus cher et plus complexe à exploiter : à arbitrer selon les moyens. 📕 Chez
> HydroRégie, on retient **deux pare-feu distincts, même constructeur**, avec des administrateurs
> et des jeux de règles séparés — compromis assumé et documenté.

## 5. Le modèle appliqué à HydroRégie

| Niveau | Équipements HydroRégie | Zone retenue |
|---|---|---|
| 5 | Internet, Microsoft 365, portail abonnés | Z1 / Z2 |
| 4 | ERP facturation, GMAO, SIG, postes bureautiques | Z2 / Z3 |
| 3.5 | **Serveur relais OPC UA, historian miroir, serveur de mises à jour OT, bastion** | **Z5 — DMZ industrielle** |
| 3 | Superviseur SCADA redondé, historian primaire | Z6 |
| 2 | IHM locales des 2 usines et des stations | Z7 |
| 1 | ~350 automates M340 / S7, RTU des réservoirs | Z7 / Z8 |
| 0 | Pompes, vannes, analyseurs de chlore, débitmètres | Physique |

## 6. Les limites du modèle (à savoir dire à l'oral)

Le modèle de Purdue a été conçu pour une usine, pas pour un réseau de 1 200 km. Trois nuances :

| Limite | Comment on la traite ici |
|---|---|
| Les **sites distants** (réservoirs, stations) ne rentrent pas dans une pile à 6 niveaux | On crée une **zone dédiée Z8**, reliée par VPN sur APN privé, traitée comme un niveau 1/2 déporté |
| L'**IIoT** et les capteurs 4G contournent la pyramide | Ils sont raccordés à Z8, jamais directement au niveau 3 |
| Le **cloud** industriel (télémaintenance éditeur) casse le modèle | Flux **sortant uniquement**, initié depuis la DMZ, jamais entrant |

> 🎯 **La bonne formule en soutenance** : « Nous avons appliqué le modèle de Purdue comme cadre de
> raisonnement, en l'adaptant à un réseau géographiquement réparti par une zone dédiée aux sites
> distants. »

## ✅ Vérification

- [ ] Cite les 6 niveaux dans l'ordre.
- [ ] Où se situe la DMZ industrielle et pourquoi ?
- [ ] Pourquoi la DMZ ne doit-elle jamais initier de connexion vers l'OT ?

---

⬅️ [01 — IT vs OT](01-it-vs-ot.md) · ➡️ [03 — VLAN et segmentation](03-vlan-et-segmentation.md)
