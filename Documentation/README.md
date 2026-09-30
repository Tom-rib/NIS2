# 📗 Documentation — réponse au sujet, job par job

Ce dossier contient **le rendu évalué**. Un fichier par bloc, lisible indépendamment.

| Bloc | Livrable attendu par le sujet | Fichier | Statut |
|---|---|---|---|
| **1** | Note de qualification réglementaire | [job-1-qualification.md](job-1-qualification.md) | ✅ Rédigé |
| **2** | Analyse d'écart et feuille de route | [job-2-analyse-ecart.md](job-2-analyse-ecart.md) | ✅ Rédigé |
| **3** | Schéma d'architecture réseau segmentée IT/OT | [job-3-architecture.md](job-3-architecture.md) | ✅ Rédigé |
| **4** | Chronologie de crise et notifications rédigées | [job-4-crise-notifications.md](job-4-crise-notifications.md) | ✅ Rédigé |

## 📎 Annexes — les notifications prêtes à l'emploi

| Document | Délai | Fichier |
|---|---|---|
| Alerte précoce | **24 h** — art. 23(4)(a) | [annexes/A-alerte-precoce-24h.md](annexes/A-alerte-precoce-24h.md) |
| Notification d'incident | **72 h** — art. 23(4)(b) | [annexes/B-notification-72h.md](annexes/B-notification-72h.md) |
| Rapport final | **1 mois** — art. 23(4)(d) | [annexes/C-rapport-final-1-mois.md](annexes/C-rapport-final-1-mois.md) |
| Information des usagers | art. 23(1) | [annexes/D-information-usagers.md](annexes/D-information-usagers.md) |
| Notification CNIL (RGPD) | 72 h — art. 33 RGPD | [annexes/E-notification-cnil.md](annexes/E-notification-cnil.md) |
| Registre des écarts (tableur) | — | [annexes/F-registre-des-ecarts.csv](annexes/F-registre-des-ecarts.csv) |

## 🎤 Support de soutenance

| Document | Contenu |
|---|---|
| 🔴 **[presentation-soutenance.pdf](presentation-soutenance.pdf)** | **La présentation complète — 21 slides**, annexes intégrées dans le raisonnement |
| [presentation-soutenance.html](presentation-soutenance.html) | La source, modifiable dans un éditeur de texte |
| [annexes-soutenance.pdf](annexes/annexes-soutenance.pdf) | Les 7 tableaux de référence en 16:9, à ouvrir pendant les questions du jury |
| [annexes-soutenance.html](annexes/annexes-soutenance.html) | La source du PDF ci-dessus |
| [`../schemas/architecture-cible.png`](../schemas/architecture-cible.png) | Le schéma d'architecture, déjà intégré en slide 13 |
| [`../schemas/flux-notification.png`](../schemas/flux-notification.png) | Le processus de notification, en complément |

### Formats non publiés sur le dépôt

`presentation-soutenance.pptx` et `slides-png.zip` sont volumineux et **regénérables**. Les produire
en une commande :

```bash
python scripts/documentation/regenerer-presentation.py
```

Le script refait les quatre formats depuis le HTML : PDF, 21 PNG en 2560×1440, l'archive ZIP,
et le PPTX.

> ⚠️ **N'importe pas le PDF dans Canva.** Un PDF ne contient pas de tableaux, seulement du texte
> positionné et des traits. Canva recrée une zone de texte par fragment puis recalcule la mise en
> page avec ses propres polices — or le deck utilise **Segoe UI**, absente de Canva. La substitution
> change les métriques et fait glisser les blocs. Importer le **PPTX** produit par le script.

## 🔎 Conventions de lecture

| Marqueur | Signification |
|---|---|
| 📗 | Vient du texte de la directive (UE) 2022/2555 — l'article est cité |
| 📙 | Vient d'une source officielle (ANSSI, ENISA, Légifrance) — le lien est donné |
| 📕 | **Hypothèse de travail** — chiffre, date ou scénario construit pour ce cas d'école |

⚠️ **Rappel important** : à la date de rédaction (10/09/2026), **la loi française de transposition
n'est pas promulguée**. Toutes les obligations citées s'appuient sur le texte de la directive.
Voir [`Cour/reglementation/00-calendrier-et-transposition.md`](../Cour/reglementation/00-calendrier-et-transposition.md).

⬅️ [Retour au README principal](../README.md)
