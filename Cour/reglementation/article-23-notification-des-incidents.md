# Article 23 — Obligations de notification

> 🎯 **En une phrase** : **24 heures**, **72 heures**, **un mois** — trois échéances à ne jamais
> confondre, à compter du moment où l'on **a connaissance** d'un incident important.
> ⏱️ 12 minutes. **Cœur du bloc 4.**

---

## 1. Qu'est-ce qu'un incident « important » ? (art. 23(3))

> 📗 Un incident est considéré comme **important** si :
> **(a)** il a causé ou est susceptible de causer une **perturbation opérationnelle grave** des
> services ou des **pertes financières** pour l'entité concernée ;
> **(b)** il a affecté ou est susceptible d'affecter **d'autres personnes** physiques ou morales
> en causant des **dommages matériels ou immatériels considérables**.

Trois observations décisives :

1. **« est susceptible de »** : il n'est pas nécessaire que le dommage se soit réalisé. Un
   rançongiciel bloqué à temps mais qui aurait pu tout chiffrer **peut être** important.
2. Les deux critères sont **alternatifs** : (a) **ou** (b) suffit.
3. Les **seuils précis** seront fixés par les textes nationaux et, pour certains secteurs, par des
   actes d'exécution. 📙 En France, ils dépendent des décrets à paraître.

## 2. Les trois échéances (art. 23(4))

```
T0 = moment ou l'entite A CONNAISSANCE de l'incident important
 |
 |--- 24 h ----> ALERTE PRECOCE            art. 23(4)(a)
 |               "Il se passe quelque chose"
 |
 |--- 72 h ----> NOTIFICATION D'INCIDENT   art. 23(4)(b)
 |               "Voila ce que c'est, voila l'impact"
 |
 |--- sur demande --> RAPPORT INTERMEDIAIRE art. 23(4)(c)
 |
 |--- 1 mois ---> RAPPORT FINAL            art. 23(4)(d)
                  a compter de la NOTIFICATION (72 h), pas de T0
```

### 🔴 Le point que tout le monde rate

Le **mois** court à compter de la **notification d'incident** (celle des 72 h), **et non** à compter
de la découverte. Il faut donc écrire dans la procédure : *« rapport final = date d'envoi de la
notification 72 h + 1 mois »*.

### Détail de chaque échéance

| Échéance | Article | Contenu attendu |
|---|---|---|
| **Alerte précoce — 24 h** | 23(4)(a) | Sans retard injustifié et **en tout état de cause dans les 24 heures** après avoir eu connaissance de l'incident. Indique si l'incident est **susceptible d'avoir été causé par des actes illicites ou malveillants** et s'il peut avoir un **impact transfrontalier** |
| **Notification d'incident — 72 h** | 23(4)(b) | Sans retard injustifié et **dans les 72 heures**. Met à jour l'alerte précoce, fournit une **évaluation initiale** de l'incident (gravité, impact) et, **lorsqu'ils sont disponibles**, les **indicateurs de compromission** |
| **Rapport intermédiaire** | 23(4)(c) | **À la demande** du CSIRT ou de l'autorité compétente : point d'étape sur les mises à jour pertinentes |
| **Rapport final — 1 mois** | 23(4)(d) | Au plus tard **un mois après la notification des 72 h**. Contient : description détaillée de l'incident (gravité, impact), **type de menace ou cause profonde**, **mesures d'atténuation** appliquées et en cours, et le cas échéant l'**impact transfrontalier** |
| **Rapport d'avancement** | 23(4)(e) | Si l'incident est **toujours en cours** au moment du rapport final : on envoie un **rapport d'avancement** à cette date, puis le **rapport final dans le mois suivant le traitement** de l'incident |

> 💡 **Cas particulier** : les **prestataires de services de confiance** disposent d'un délai réduit
> à **24 heures** pour la notification d'incident concernant les services de confiance (art. 23(4),
> dernier alinéa). Ne s'applique pas à HydroRégie.

## 3. Les autres obligations de l'article 23

| § | Obligation | En clair |
|---|---|---|
| 23(1) | Notifier **sans retard injustifié** tout incident important au CSIRT ou à l'autorité compétente ; le cas échéant, notifier **sans retard injustifié aux destinataires de leurs services** les incidents importants susceptibles de nuire à la fourniture de ces services | 💧 **Prévenir les usagers** quand le service est affecté |
| 23(2) | En cas de **cybermenace importante**, informer les destinataires potentiellement affectés des **mesures ou corrections** qu'ils peuvent appliquer, et le cas échéant de la menace elle-même | Prévenir même sans incident réalisé |
| 23(5) | Le CSIRT ou l'autorité fournit une **réponse** à l'entité **dans les 24 heures** suivant la réception de l'alerte précoce, y compris des orientations, un appui, ou une **assistance technique** | 🔑 **La notification n'est pas à sens unique : on reçoit de l'aide** |
| 23(6) | Le CSIRT peut informer les autres États membres et l'ENISA en cas d'**impact transfrontalier** | — |
| 23(7) | Le point de contact unique transmet à l'ENISA une **synthèse** des notifications | — |
| 23(11) | La Commission peut adopter des **actes d'exécution** précisant le type d'informations, le format et la procédure | — |

📗 **Article 23(8)** prévoit par ailleurs que l'autorité, lorsqu'une **sensibilisation du public**
est nécessaire pour prévenir un incident ou y faire face, peut **informer le public** ou exiger de
l'entité qu'elle le fasse.

## 4. 🔑 À retenir absolument

1. **24 h / 72 h / 1 mois**, et le mois part de la **notification**, pas de la découverte.
2. Le point de départ est la **connaissance** de l'incident — d'où l'importance de **journaliser
   l'heure exacte de détection** et de savoir la prouver.
3. L'alerte précoce **ne demande pas de comprendre l'incident**. Elle demande de dire qu'il existe.
   **Ne jamais retarder l'alerte pour "avoir plus d'informations".**
4. On peut recevoir de l'**assistance** en retour (23(5)) : notifier tôt est un **avantage**, pas
   seulement une contrainte.
5. Prévenir **les usagers** est une obligation distincte de la notification à l'autorité.

## 5. ⚠️ NIS2 ≠ RGPD : ne pas confondre

| | **NIS2** (art. 23) | **RGPD** (art. 33-34) |
|---|---|---|
| Objet | Incident affectant les services / réseaux | Violation de **données à caractère personnel** |
| Destinataire | CSIRT / autorité compétente (ANSSI) | Autorité de contrôle (**CNIL**) |
| Délais | **24 h**, puis **72 h**, puis **1 mois** | **72 h** (une seule échéance) |
| Personnes concernées | Destinataires des services, si affectés | Personnes concernées, si risque élevé |

> 🔴 **Chez HydroRégie, les deux s'appliqueront souvent en même temps** : un rançongiciel qui
> chiffre l'ERP de facturation touche les données de 240 000 abonnés. Il faut donc **deux
> notifications, à deux autorités, avec deux calendriers**. C'est exactement l'objet de
> l'article 35 de NIS2.

## 6. 🏢 Chez HydroRégie — la procédure à mettre en place

| Élément | Décision |
|---|---|
| Qui **qualifie** un incident d'important ? | Le RSSI, sur la base d'une grille écrite ; en cas de doute → **on notifie** |
| Qui **valide** l'envoi ? | Le directeur général ou son suppléant désigné |
| Qui **rédige** ? | Le RSSI, à partir de modèles **pré-rédigés** ([`Documentation/annexes/`](../../Documentation/annexes/)) |
| Où sont les modèles ? | **Sur papier et sur un support hors domaine** — le jour J, l'intranet peut être chiffré |
| Comment on envoie ? | Plateforme de l'autorité (MonEspaceNIS2) + courriel de secours hors domaine |
| Comment on prouve ? | Horodatage, accusé de réception, copie archivée dans le dossier de crise |

### La grille de qualification (📕 proposition)

| Question | Si oui → incident important |
|---|---|
| La distribution ou la qualité de l'eau est-elle affectée, ou susceptible de l'être ? | ✅ |
| Le SCADA ou des automates sont-ils indisponibles ou suspectés compromis ? | ✅ |
| Un service à l'usager est-il interrompu plus de 4 h ? | ✅ |
| Des données personnelles d'abonnés sont-elles concernées ? | ✅ (+ RGPD) |
| L'incident est-il d'origine malveillante avérée ou probable ? | ✅ |
| La perte financière estimée dépasse-t-elle un seuil défini par la direction ? | ✅ |

---

## 🔗 Liens

⬅️ [Article 22](article-22-evaluations-coordonnees.md) · ➡️ [Article 24 — Certification](article-24-certification.md) ·
📎 [Bloc 4 — chronologie de crise](../../Documentation/job-4-crise-notifications.md) ·
📎 [Modèles de notification](../../Documentation/annexes/)
