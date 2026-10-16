# 10 — Gestion de crise cyber

> 🎯 **Objectif** : savoir organiser, décider et communiquer quand tout tombe — et tenir les délais
> réglementaires en même temps.
> ⏱️ 8 minutes. **Base du bloc 4.**

---

## 1. Les 5 phases

```
DETECTION -> QUALIFICATION -> ESCALADE -> REMEDIATION -> RETOUR D'EXPERIENCE
   |             |                |            |                |
 "quelque    "c'est un       "on active   "on contient,   "qu'est-ce qu'on
  chose       incident        la cellule   on eradique,    change ?"
  cloche"     important"      de crise"    on retablit"
```

| Phase | Question centrale | Sortie |
|---|---|---|
| **Détection** | Que voit-on ? | Alerte horodatée, main courante ouverte |
| **Qualification** | Est-ce un incident **important** au sens de l'art. 23(3) ? | Décision écrite, **T0 posé** |
| **Escalade** | Qui doit être prévenu, et dans quel ordre ? | Cellule de crise réunie |
| **Remédiation** | Comment contenir, éradiquer, rétablir ? | Service rétabli, preuves conservées |
| **Retour d'expérience** | Qu'est-ce qui change durablement ? | Plan d'actions, procédures mises à jour |

## 2. 🔴 Le T0 : le moment le plus important de la crise

> **T0 = l'instant où l'entité « a connaissance » de l'incident.**
> C'est de lui que partent les 24 h et les 72 h de l'article 23(4).

Trois règles :

1. **Il s'écrit.** Dans la main courante, à la minute près, avec la source de la détection.
2. **Il ne se négocie pas rétroactivement.** Reculer T0 pour se donner de l'air est un mensonge
   documenté qui se retourne contre l'entité.
3. **En cas de doute, T0 est le premier signal, pas le moment où on a compris.**

## 3. L'organisation en deux cellules

Ne jamais mélanger ceux qui décident et ceux qui réparent : **c'est l'erreur n°1 en exercice.**

```
        +----------------------------+
        |  CELLULE DE CRISE          |   Decide, arbitre, communique, NOTIFIE
        |  DG (directeur de crise)   |
        |  DSI, RSSI                 |
        |  Responsable exploitation  |
        |  Communication, Juridique  |
        |  Un SECRETAIRE (main       |
        |  courante) <-- essentiel   |
        +-------------+--------------+
                      | points de situation toutes les heures
        +-------------v--------------+
        |  CELLULE TECHNIQUE         |   Analyse, contient, restaure
        |  Admins IT et OT           |
        |  Prestataire de reponse    |
        |  Integrateur automatismes  |
        +----------------------------+
```

| Rôle | Responsabilité | Ne fait pas |
|---|---|---|
| **Directeur de crise** (DG) | Décide, arbitre, engage l'entité | Ne met pas les mains dans la technique |
| **RSSI** | Qualifie, rédige les notifications, fait le lien avec le CSIRT | Ne décide pas seul de notifier |
| **Responsable exploitation** | Garantit la continuité de la distribution d'eau | — |
| **Communication** | Usagers, presse, élus | N'improvise pas : messages préparés |
| **Secrétaire de crise** | **Main courante horodatée** | Ne participe pas aux décisions |

> 🔑 **Le secrétaire de crise est le poste le plus sous-estimé.** Sans main courante, il sera
> impossible d'écrire le rapport final de l'article 23(4)(d) un mois plus tard — et impossible de
> prouver qu'on a respecté les délais.

## 4. La main courante

Un tableau, papier **et** numérique hors domaine :

| Heure | Source | Fait constaté | Décision | Qui | Diffusion |
|---|---|---|---|---|---|
| 04:12 | Astreinte exploitation | Alarmes SCADA multiples, postes bureautiques inaccessibles | Ouverture main courante | J. Martin | — |
| 04:40 | RSSI | Rançongiciel confirmé sur 3 serveurs | Isolement du lien IT/OT | RSSI | Cellule |

Règles : **on n'efface jamais**, on ajoute. Toute correction est une nouvelle ligne.

## 5. Les décisions qui ne s'improvisent pas

Ces arbitrages doivent être **tranchés à l'avance**, par écrit, validés par la direction :

| Décision | Qui décide | Critère préétabli 📕 |
|---|---|---|
| Couper le lien IT ↔ OT | Responsable exploitation + RSSI | **Dès suspicion de propagation** — on coupe d'abord, on analyse ensuite |
| Arrêter un service à l'usager | DG | Si l'intégrité des données ou la qualité de l'eau est en jeu |
| Basculer en mode dégradé | Responsable exploitation | Si le SCADA est indisponible ou suspect |
| Payer une rançon | **Jamais** — décision de principe actée par la direction | Aucune garantie, financement de la criminalité, et cela n'efface pas l'incident |
| Communiquer publiquement | DG + communication | Dès que les usagers sont affectés |
| Déposer plainte | DG + juridique | **Systématiquement**, sous 24-48 h |
| Notifier l'autorité | DG sur proposition du RSSI | **En cas de doute, on notifie** |

## 6. Communiquer quand la messagerie est morte

📗 Exigence de l'art. 21(2)(j) : « systèmes de communication d'urgence sécurisés au sein de
l'entité ».

| Moyen | Préparation nécessaire |
|---|---|
| **Annuaire de crise papier**, à jour, en plusieurs exemplaires | Mise à jour trimestrielle, exemplaires chez les cadres d'astreinte |
| Messagerie **hors domaine** (comptes dédiés, non liés à l'AD) | Comptes créés et testés **à froid** |
| Groupe de discussion chiffré sur téléphones personnels ou dédiés | Créé à l'avance, testé |
| Téléphones fixes analogiques | Vérifier qu'ils ne dépendent pas de la ToIP |
| Salle de crise physique identifiée | Avec paperboard, imprimante, connexion 4G indépendante |

> 💡 **Le test qui révèle tout** : couper l'accès à la messagerie pendant un exercice et voir en
> combien de temps la cellule arrive à se réunir. Le résultat est en général instructif.

## 7. La superposition des horloges réglementaires

C'est **la difficulté propre à NIS2** : gérer la crise **et** tenir les délais.

```
T0 ---------- +24 h --------- +72 h ------------------- +1 mois (apres la notif 72h)
 |              |               |                            |
 |         ALERTE PRECOCE   NOTIFICATION                RAPPORT FINAL
 |         (ANSSI)          (ANSSI)                     (ANSSI)
 |              |
 |         +72 h RGPD -> CNIL (si donnees personnelles)
 |
 +-- Depot de plainte (24-48 h)
 +-- Information des usagers (art. 23(1)) des que le service est affecte
 +-- Assureur cyber (delai contractuel, souvent 48-72 h)
```

> 🔑 **Le rappel qui sauve** : le rapport final court à compter de la **notification des 72 h**,
> pas de T0.

## 8. Les 7 erreurs classiques en exercice

| ❌ Erreur | Conséquence |
|---|---|
| Attendre de « tout comprendre » pour notifier | Dépassement des 24 h |
| Ne pas tenir de main courante | Rapport final impossible à écrire |
| Mélanger décision et technique | Le DG micro-gère, personne ne décide |
| Réinstaller avant de collecter les preuves | Point d'entrée jamais identifié → réinfection |
| Communiquer sans message préparé | Contradictions, perte de confiance |
| Oublier les usagers (art. 23(1)) | Manquement supplémentaire |
| Ne pas prévoir de relève | À H+18, personne n'est en état de décider |

## 9. Le retour d'expérience

Sous **15 jours** après la fin de la crise, un compte rendu **sans recherche de coupable** :

1. Chronologie factuelle (issue de la main courante)
2. Ce qui a bien fonctionné
3. Ce qui a manqué
4. Plan d'actions **daté et responsabilisé**
5. Mise à jour des procédures et de l'analyse de risques

> 📗 Cela alimente directement l'art. 21(2)(f) (évaluation de l'efficacité) et
> l'art. 21(4) (mesures correctives sans délai).

## ✅ Vérification

- [ ] Qu'est-ce que T0 et pourquoi ne se négocie-t-il pas ?
- [ ] Pourquoi séparer cellule de crise et cellule technique ?
- [ ] À partir de quand court le délai du rapport final ?
- [ ] Comment communique-t-on si la messagerie est chiffrée ?

---

⬅️ [09 — Sauvegardes et continuité](09-sauvegardes-et-continuite.md) · 🏠 [Sommaire du cours](../README.md)
