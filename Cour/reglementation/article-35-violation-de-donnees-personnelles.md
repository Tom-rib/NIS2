# Article 35 — Infractions entraînant une violation de données à caractère personnel

> 🎯 **En une phrase** : quand un incident NIS2 est aussi une violation de données personnelles,
> **les deux régimes s'appliquent**, mais on ne peut pas être **sanctionné financièrement deux fois
> pour le même fait**.
> ⏱️ 3 minutes.

---

## Ce que dit l'article, en simple

- Lorsque les autorités compétentes NIS2 constatent qu'un manquement aux articles 21 ou 23 peut
  entraîner une **violation de données à caractère personnel** au sens du RGPD, elles en informent
  **sans retard injustifié** l'autorité de contrôle compétente (la **CNIL** en France).
- Si l'autorité de protection des données décide d'infliger une **amende** au titre du RGPD, les
  autorités NIS2 **n'infligent pas d'amende** au titre de l'article 34 pour le **même comportement**.
- Elles peuvent en revanche appliquer les **autres mesures d'exécution** de l'article 32 :
  injonctions, ordre de mise en conformité, désignation d'un contrôleur, publicité du manquement.

## 🔑 À retenir

```
Un rancongiciel chiffre l'ERP de facturation d'HydroRegie
        |
        +--> Incident NIS2 (service perturbe)      -> ANSSI  : 24 h / 72 h / 1 mois
        |
        +--> Violation de donnees personnelles     -> CNIL   : 72 h (art. 33 RGPD)
                                                    -> personnes concernees si risque eleve
                                                       (art. 34 RGPD)

Sanction : une seule AMENDE pour le meme comportement (art. 35 NIS2),
           mais les autres mesures d'execution NIS2 restent applicables.
```

- **Les obligations de notification, elles, ne fusionnent pas** : il faut **deux notifications**,
  à **deux autorités**, avec **deux calendriers** et deux contenus différents.
- Le principe est celui du ***non bis in idem*** appliqué aux amendes, pas aux obligations.

## 🏢 Chez HydroRégie

HydroRégie facture **240 000 abonnés** : nom, adresse, coordonnées bancaires pour les prélèvements,
consommations (qui révèlent des habitudes de vie). Un incident sur l'ERP est donc, presque par
construction, **aussi** une violation de données personnelles.

### Ce qu'il faut avoir préparé

| Élément | Décision |
|---|---|
| Qui coordonne les deux notifications ? | Le **RSSI** rédige, le **DPO** valide le volet RGPD, le **DG** autorise l'envoi |
| Quel calendrier ? | Une seule chronologie de crise avec **deux échéanciers superposés** — voir bloc 4 |
| Comment éviter les contradictions ? | Un **fait unique** consigné dans la main courante ; les deux notifications sont rédigées à partir de la même source |
| Faut-il prévenir les abonnés ? | Oui si risque élevé (art. 34 RGPD) et/ou si le service est affecté (art. 23(1) NIS2) — décision de la cellule de crise |

> ⚠️ **Erreur classique en exercice** : traiter les 72 h RGPD comme si c'était le même délai que les
> 72 h NIS2. Ce sont **deux délais distincts**, avec **deux points de départ** potentiellement
> différents : « avoir connaissance de l'incident » (NIS2) et « avoir connaissance de la violation »
> (RGPD).

## ⚠️ Le piège

Croire que l'article 35 dispense de l'une des deux notifications. Il ne porte que sur le
**cumul des amendes**, jamais sur le cumul des **obligations**.

---

⬅️ [Article 34](article-34-amendes-administratives.md) · ➡️ [Articles 36 à 45 — Dispositions finales](articles-36-a-45-dispositions-finales.md)
