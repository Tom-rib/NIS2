# Annexe A — Alerte précoce (24 h)

> 📗 **Fondement** : article 23(4)(a) de la directive (UE) 2022/2555
> **Délai** : sans retard injustifié et **en tout état de cause dans les 24 heures** après avoir eu
> connaissance de l'incident important.
> **Contenu minimal exigé** : indiquer si l'incident est **susceptible d'avoir été causé par des
> actes illicites ou malveillants** et s'il peut avoir un **impact transfrontalier**.

---

## ⚠️ Mode d'emploi

- Ce document est **un modèle rempli** avec les données du scénario du [bloc 4](../job-4-crise-notifications.md).
  Les champs entre `<...>` sont à compléter le jour J.
- 📙 Le **format exact** sera imposé par la plateforme nationale (MonEspaceNIS2) et par les actes
  d'exécution prévus à l'article 23(11). Ce modèle en couvre le contenu ; il sert aussi de
  **brouillon de travail** quand la plateforme est inaccessible.
- 🔴 **Ne jamais retarder l'envoi pour compléter une information manquante.** Écrire
  « non déterminé à ce stade » est parfaitement recevable : l'article 23(4)(a) demande un signalement,
  pas une analyse.
- L'alerte se **prépare à froid** et se conserve **sur papier** : le jour J, l'intranet peut être chiffré.

---

## ALERTE PRÉCOCE — INCIDENT DE CYBERSÉCURITÉ

**Fondement juridique** : article 23(4)(a) de la directive (UE) 2022/2555
**Destinataire** : autorité nationale compétente / CSIRT national
**Émetteur** : HydroRégie — entité essentielle (annexe I, point 6 — eau potable)
**Référence interne** : `INC-2027-0316-001`
**Date et heure d'envoi** : **mardi 16 mars 2027, 14 h 30**
**Délai écoulé depuis la connaissance de l'incident** : **10 h 18** ✅

---

### 1. Identification de l'entité

| Champ | Valeur |
|---|---|
| Raison sociale | HydroRégie |
| Statut NIS2 | **Entité essentielle** — art. 3(1)(a) |
| Secteur | **Annexe I, point 6 — Eau potable** |
| Identifiant d'enregistrement | `<n° MonEspaceNIS2>` |
| Adresse | `<adresse du siège>` |
| Population desservie | 450 000 habitants — 240 000 abonnés — 62 communes |
| Référent NIS2 | `<nom, fonction>` |
| Téléphone d'astreinte 24/7 | `<n°>` |
| Adresse électronique de crise | `<adresse hors domaine>` |

> ⚠️ **Les coordonnées transmises doivent être celles de l'astreinte**, pas celles d'un standard.
> Elles servent au retour de l'autorité prévu à l'article 23(5), sous 24 h.

### 2. Date et heure de l'incident

| Champ | Valeur |
|---|---|
| **Date et heure de connaissance de l'incident (T0)** | **16/03/2027 à 04 h 12** |
| Source de la détection | Astreinte exploitation — alarmes SCADA multiples et indisponibilité des postes bureautiques |
| Date et heure de début estimée de l'incident | Non déterminée à ce stade — investigations en cours |
| Incident **toujours en cours** ? | ✅ **Oui** |

### 3. Nature de l'incident

**Description succincte** :

> Chiffrement par rançongiciel d'une partie du système d'information de gestion d'HydroRégie,
> détecté le 16 mars 2027 à 04 h 12. Sont touchés : l'annuaire Active Directory, les serveurs de
> fichiers, l'application de facturation des abonnés, la gestion de maintenance et la messagerie.
>
> Le système industriel (supervision et automates de production et de distribution d'eau) **n'est
> pas affecté à ce stade**. Par précaution, la liaison entre le système d'information de gestion et
> le système industriel a été **physiquement coupée à 04 h 45**, soit 33 minutes après la détection.
>
> **La production et la distribution d'eau potable ne sont pas interrompues.** Les installations
> fonctionnent en mode dégradé autonome : les automates assurent la régulation locale sans
> supervision centralisée.

### 4. 📗 Actes illicites ou malveillants *(mention exigée par l'art. 23(4)(a))*

> ✅ **OUI** — l'incident est **susceptible d'avoir été causé par des actes illicites ou
> malveillants**. Un rançongiciel avec demande de rançon a été identifié sur au moins deux serveurs.
> Un dépôt de plainte est en cours de préparation.

### 5. 📗 Impact transfrontalier *(mention exigée par l'art. 23(4)(a))*

> ❌ **NON** — aucun impact transfrontalier identifié à ce stade. HydroRégie exerce son activité
> exclusivement sur le territoire national et ne fournit aucun service dans un autre État membre.

### 6. Impact constaté à ce stade

| Domaine | État |
|---|---|
| **Production et distribution d'eau potable** | ✅ **Non interrompue** — mode dégradé autonome |
| **Qualité de l'eau** | ✅ Non affectée — contrôles renforcés par prélèvements en cours |
| Supervision centralisée (SCADA) | ⚠️ Volontairement isolée |
| Facturation et espace abonnés | ❌ Indisponibles |
| Accueil téléphonique et messagerie | ❌ Indisponibles |
| Gestion de maintenance (GMAO) | ❌ Indisponible |
| **Données à caractère personnel** | ⚠️ **Potentiellement concernées** — 240 000 abonnés. Notification à l'autorité de protection des données en préparation |
| Nombre d'usagers concernés | 450 000 habitants (service), 240 000 abonnés (données) |

### 7. Mesures déjà prises

1. Coupure physique de la liaison entre le système de gestion et le système industriel (04 h 45)
2. Isolement du système d'information : coupure de l'accès Internet, arrêt des serveurs sains
3. Vérification des sauvegardes hors ligne — **intactes**, restauration possible
4. Activation de la cellule de crise (05 h 30) et de l'astreinte renforcée sur les sites sensibles
5. Bascule en exploitation dégradée autonome, avec rondes et prélèvements renforcés
6. Réalisation d'images disque des serveurs touchés avant toute réinstallation (préservation des preuves)
7. Prise de contact avec le CSIRT national pour assistance technique
8. Information des usagers par les canaux publics (art. 23(1))

### 8. Assistance souhaitée

> Une assistance technique est **sollicitée** au titre de l'article 23(5), en particulier sur :
> l'identification de la souche et des indicateurs de compromission à rechercher, la vérification de
> l'absence de compromission du système industriel, et les précautions de reconstruction.

### 9. Suite prévue

> Une **notification d'incident** au titre de l'article 23(4)(b) sera transmise **dans les 72 heures
> suivant la connaissance de l'incident**, soit au plus tard le **19/03/2027 à 04 h 12**, avec une
> évaluation initiale de la gravité, de l'impact et, lorsqu'ils seront disponibles, les indicateurs
> de compromission.

---

**Rédigé par** : `<nom>`, RSSI
**Validé par** : `<nom>`, Directeur général
**Transmis le** : 16/03/2027 à 14 h 30 · **Accusé de réception** : `AR-2027-0316-1430`

---

## 📋 Aide-mémoire de rédaction

| ✅ À faire | ❌ À éviter |
|---|---|
| Envoyer **même si tout n'est pas su** | Attendre de « tout comprendre » |
| Écrire « non déterminé à ce stade » | Laisser un champ vide, ou inventer |
| Donner l'heure **exacte** de T0 | Arrondir ou reculer T0 |
| Répondre explicitement aux **deux mentions exigées** (actes malveillants, transfrontalier) | Les oublier — ce sont les seules obligations de contenu de l'art. 23(4)(a) |
| Indiquer si le service essentiel est affecté | Se limiter au volet informatique |
| Faire **valider par la direction** avant envoi | Envoyer sans validation (art. 20(1)) |
| Conserver l'accusé de réception | Ne garder aucune preuve d'envoi |

⬅️ [Retour au bloc 4](../job-4-crise-notifications.md) · ➡️ [Annexe B — Notification 72 h](B-notification-72h.md)
