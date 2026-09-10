# Articles 7 à 13 — Ce que chaque État doit mettre en place

> 🎯 **En une phrase** : ces articles ne créent pas d'obligation pour l'entreprise, mais ils
> décrivent **l'interlocuteur** auquel elle aura affaire — l'ANSSI en France.
> ⏱️ 6 minutes.
>
> ℹ️ Ces sept articles sont regroupés car ils s'adressent aux **États**, pas aux entités. Ils sont
> néanmoins utiles pour savoir **à qui l'on parle** lors d'un incident (bloc 4).

---

## Article 7 — Stratégie nationale de cybersécurité

Chaque État adopte une stratégie nationale définissant objectifs, gouvernance, ressources et
politiques : chaîne d'approvisionnement, gestion des vulnérabilités, sensibilisation, soutien aux
PME, disponibilité de l'open source, formation…

## Article 8 — Autorités compétentes et point de contact unique

Chaque État désigne une ou plusieurs **autorités compétentes** chargées de la cybersécurité et de
la supervision, et un **point de contact unique** qui assure la liaison transfrontalière.

📙 **En France** : l'**ANSSI** est l'autorité nationale de sécurité des systèmes d'information et
assure ces rôles (à confirmer formellement par la loi de transposition).

## Article 9 — Cadres nationaux de gestion des crises cyber

Chaque État désigne des **autorités de gestion des crises cyber**, adopte un **plan national de
réponse** aux incidents et crises de cybersécurité à grande échelle, décrivant objectifs, rôles,
procédures, moyens et parties prenantes.

## Article 10 — Les CSIRT

Chaque État désigne un ou plusieurs **CSIRT** (*Computer Security Incident Response Team*),
techniquement compétents, dotés de moyens et de canaux de communication **redondants et sécurisés**,
et disponibles **24 h/24, 7 j/7**.

📙 En France : le **CERT-FR**, au sein de l'ANSSI.

## Article 11 — Missions des CSIRT

| Mission | En clair |
|---|---|
| Surveillance et analyse des cybermenaces | Veille |
| **Alerte précoce, alertes, annonces**, diffusion d'informations | Les avis et alertes du CERT-FR |
| Réponse aux incidents et **assistance** aux entités concernées | 📞 **Le numéro qu'on appelle en crise** |
| Collecte et analyse de données de criminalistique | Investigation numérique |
| Analyse dynamique des risques, connaissance situationnelle | Vision d'ensemble |
| Analyse **coordonnée** des vulnérabilités | Art. 12 |
| Contribution au déploiement d'outils de partage sécurisés | — |

> 🔑 **Point clé pour le bloc 4** : le CSIRT n'est pas seulement un guichet de déclaration, c'est
> **une aide**. Un bon plan de crise l'appelle **tôt**, pas seulement pour respecter un délai.

## Article 12 — Divulgation coordonnée des vulnérabilités

Chaque État désigne un **CSIRT coordinateur** qui sert d'intermédiaire entre celui qui découvre une
vulnérabilité et le fabricant ou fournisseur concerné. L'**ENISA** développe et maintient une
**base de données européenne des vulnérabilités** (EUVD).

> 💡 Utile pour un exploitant OT : les vulnérabilités d'automates sont souvent publiées via les
> avis du CERT-FR et les *ICS advisories*. Les suivre relève de l'art. 21(2)(e).

## Article 13 — Coopération au niveau national

Les autorités compétentes, le point de contact unique et les CSIRT **coopèrent entre eux**, et avec
les autorités chargées de la protection des données, de l'application de la loi et de la protection
civile.

> 🔑 Cela explique qu'une notification NIS2 peut **croiser** une notification RGPD (voir art. 35) :
> les autorités se parlent.

---

## 🏢 Ce qu'il faut en retenir pour HydroRégie

Dans le plan de crise du bloc 4, la fiche « **Qui appelle-t-on ?** » s'appuie sur ces articles :

| Interlocuteur | Rôle | Quand |
|---|---|---|
| **ANSSI / autorité compétente** (art. 8) | Destinataire des notifications réglementaires | 24 h / 72 h / 1 mois |
| **CERT-FR / CSIRT** (art. 10-11) | Assistance technique, qualification, remédiation | **Le plus tôt possible** |
| Autorité de gestion de crise (art. 9) | En cas de crise de grande ampleur | Sur activation |
| Préfecture / ARS | Continuité de la distribution d'eau, santé publique | Si impact usagers |
| CNIL | Si violation de données personnelles (art. 35 NIS2, art. 33 RGPD) | 72 h |
| Dépôt de plainte | Judiciarisation | Sous 24-48 h |

---

## ⚠️ Le piège

Attendre d'avoir « tout compris » de l'incident avant d'appeler le CSIRT. La directive prévoit une
**alerte précoce à 24 h justement parce qu'on ne sait pas encore** : l'article 23(4)(a) demande une
première information, pas un rapport d'analyse.

---

⬅️ [Article 6](article-06-definitions.md) · ➡️ [Articles 14 à 19 — Coopération européenne](articles-14-a-19-cooperation-europeenne.md)
