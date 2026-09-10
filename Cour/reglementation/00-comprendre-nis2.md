# 00 — Comprendre NIS2 en 10 minutes

> 🎯 **En une phrase** : NIS2 oblige environ 15 000 entités françaises de 18 secteurs à gérer
> sérieusement leur cybersécurité, sous la responsabilité personnelle de leurs dirigeants, avec des
> amendes à la clé.

---

## 1. D'où ça vient

| Année | Événement |
|---|---|
| 2016 | **NIS1** (directive 2016/1148) : premier texte européen de cybersécurité, ~500 opérateurs en France |
| 2017-2021 | WannaCry, NotPetya, SolarWinds, Colonial Pipeline, hôpitaux français… Les attaques touchent des services vitaux |
| 14/12/2022 | **NIS2** adoptée — directive (UE) 2022/2555 |
| 16/01/2023 | Entrée en vigueur de la directive |
| **17/10/2024** | Date limite de **transposition** par les États membres |
| **18/10/2024** | **Application** de NIS2 et abrogation de NIS1 (art. 41 et 44) |
| 17/04/2025 | Date à laquelle les États devaient établir la liste de leurs entités (art. 3(3)) |

## 2. Ce que NIS2 change par rapport à NIS1

| Sujet | NIS1 | NIS2 |
|---|---|---|
| **Qui est concerné** | L'État **désigne** chaque opérateur | L'entité **s'auto-qualifie** (secteur + taille) et s'enregistre |
| **Combien** | ~500 en France | ~15 000 en France, 18 secteurs |
| **Dirigeants** | Non visés | **Approuvent, supervisent, peuvent être tenus responsables, se forment** (art. 20) |
| **Mesures** | Peu détaillées | **10 domaines minimum** listés (art. 21) |
| **Notification** | Variable | **24 h / 72 h / 1 mois** harmonisés (art. 23) |
| **Sanctions** | Symboliques | **10 M€ ou 2 % du CA mondial** (art. 34) |
| **Fournisseurs** | Absent | **Sécurité de la chaîne d'approvisionnement** obligatoire (art. 21(2)(d)) |

## 3. La structure de la directive

```
Chapitre I    (art. 1-6)    Objet, champ d'application, definitions
Chapitre II   (art. 7-13)   Ce que chaque Etat doit mettre en place
Chapitre III  (art. 14-19)  La cooperation europeenne
Chapitre IV   (art. 20-25)  >>> LES OBLIGATIONS DES ENTITES <<<
Chapitre V    (art. 26-30)  Competence, registre, partage d'informations
Chapitre VI   (art. 31-37)  Supervision, execution, SANCTIONS
Chapitre VII  (art. 38-45)  Dispositions finales
Annexe I                    11 secteurs hautement critiques  (eau potable = point 6)
Annexe II                   7 autres secteurs critiques
```

> 🔑 **Si tu ne dois retenir que 3 articles** : **20** (les dirigeants),
> **21** (les 10 mesures), **23** (les délais de notification).

## 4. La logique d'ensemble en une image

```
   Je suis dans un secteur liste ?  (annexes I / II)
                |
                v
   Quelle est ma taille ?  (recommandation 2003/361/CE)
                |
                v
   +--> ENTITE ESSENTIELLE ou IMPORTANTE  (art. 3)
                |
     +----------+-----------+-------------------+
     v          v           v                   v
  Je m'ENREGISTRE  Ma DIRECTION   J'applique  Je NOTIFIE
  (art. 3(4))      s'implique     les 10       les incidents
                   (art. 20)      mesures      24h / 72h / 1 mois
                                  (art. 21)    (art. 23)
                |
                v
   Si je ne le fais pas : SUPERVISION (art. 32/33) puis AMENDES (art. 34)
```

## 5. Les 5 phrases à savoir dire à l'oral

1. « NIS2 est **une directive**, donc elle doit être transposée ; en France, la loi n'est pas
   encore promulguée à ce jour, on raisonne donc sur le texte européen. »
2. « HydroRégie relève de l'**annexe I point 6, eau potable**, et dépasse les seuils de la grande
   entreprise : elle est **entité essentielle** au sens de l'**article 3(1)(a)**. »
3. « Les obligations de fond sont **identiques** pour une entité essentielle et une entité
   importante ; ce qui change, c'est **la supervision** et **le montant des amendes**. »
4. « L'**article 21** impose une approche **tous risques**, proportionnée, couvrant **dix domaines
   minimum**. »
5. « Les délais de notification sont **24 heures** pour l'alerte précoce, **72 heures** pour la
   notification, **un mois** pour le rapport final. »

---

➡️ Suite : [Calendrier et transposition](00-calendrier-et-transposition.md) · ⬅️ [Sommaire du cours](../README.md)
