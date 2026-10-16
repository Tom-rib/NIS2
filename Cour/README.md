# 📚 Cours — tout ce qu'il faut savoir pour ce projet

Ce dossier est le **cours condensé**. Il se lit indépendamment du rendu.
Deux parties, deux logiques :

| Partie | Ce que tu y trouves | Quand la lire |
|---|---|---|
| [`reglementation/`](reglementation/) | **Un fichier par article de NIS2**, réécrit en français simple, avec « ce que ça change pour HydroRégie » | Pour les blocs 1, 2 et 4, et pour réviser avant l'oral |
| [`technique/`](technique/) | Les concepts techniques : IT vs OT, Purdue, VLAN, DMZ, VPN, SCADA, détection, continuité, crise | Pour les blocs 3 et 4 |

---

## 🚀 Si tu n'as que 20 minutes

Lis dans cet ordre :

1. [`reglementation/00-comprendre-nis2.md`](reglementation/00-comprendre-nis2.md) — la vue d'ensemble
2. [`reglementation/article-03-entites-essentielles-et-importantes.md`](reglementation/article-03-entites-essentielles-et-importantes.md) — qui est concerné
3. [`reglementation/article-21-mesures-de-gestion-des-risques.md`](reglementation/article-21-mesures-de-gestion-des-risques.md) — quoi faire
4. [`reglementation/article-23-notification-des-incidents.md`](reglementation/article-23-notification-des-incidents.md) — les délais
5. [`technique/02-modele-de-purdue.md`](technique/02-modele-de-purdue.md) — comment on segmente

---

## 🧭 Plan du cours réglementaire

### Le socle
| Fichier | Article(s) | Sujet |
|---|---|---|
| [00-comprendre-nis2.md](reglementation/00-comprendre-nis2.md) | — | Vue d'ensemble : d'où vient NIS2, ce qu'elle change |
| [00-calendrier-et-transposition.md](reglementation/00-calendrier-et-transposition.md) | 41, 44 | Dates clés et état réel de la transposition française |
| [article-01-objet-et-champ.md](reglementation/article-01-objet-et-champ.md) | 1 | Ce que la directive vise |
| [article-02-champ-application.md](reglementation/article-02-champ-application.md) | 2 | Qui est dans le champ |
| [article-03-entites-essentielles-et-importantes.md](reglementation/article-03-entites-essentielles-et-importantes.md) | 3 | Essentielle ou importante |
| [article-04-actes-sectoriels.md](reglementation/article-04-actes-sectoriels.md) | 4 | Quand un autre texte prime (DORA…) |
| [article-05-harmonisation-minimale.md](reglementation/article-05-harmonisation-minimale.md) | 5 | Les États peuvent aller plus loin |
| [article-06-definitions.md](reglementation/article-06-definitions.md) | 6 | Les 41 définitions utiles |

### Le dispositif public
| Fichier | Article(s) | Sujet |
|---|---|---|
| [articles-07-a-13-dispositif-national.md](reglementation/articles-07-a-13-dispositif-national.md) | 7-13 | Stratégie, autorités, CSIRT, divulgation des vulnérabilités |
| [articles-14-a-19-cooperation-europeenne.md](reglementation/articles-14-a-19-cooperation-europeenne.md) | 14-19 | Groupe de coopération, réseau des CSIRT, EU-CyCLONe |

### Les obligations des entités (le cœur du projet)
| Fichier | Article(s) | Sujet |
|---|---|---|
| [article-20-gouvernance.md](reglementation/article-20-gouvernance.md) | 20 | Responsabilité des dirigeants |
| [article-21-mesures-de-gestion-des-risques.md](reglementation/article-21-mesures-de-gestion-des-risques.md) | 21 | **Les 10 mesures** |
| [article-22-evaluations-coordonnees.md](reglementation/article-22-evaluations-coordonnees.md) | 22 | Chaînes d'approvisionnement critiques |
| [article-23-notification-des-incidents.md](reglementation/article-23-notification-des-incidents.md) | 23 | **24 h / 72 h / 1 mois** |
| [article-24-certification.md](reglementation/article-24-certification.md) | 24 | Schémas de certification européens |
| [article-25-normalisation.md](reglementation/article-25-normalisation.md) | 25 | Recours aux normes |
| [article-26-competence-et-territorialite.md](reglementation/article-26-competence-et-territorialite.md) | 26 | Quel État est compétent |
| [article-27-registre-des-entites.md](reglementation/article-27-registre-des-entites.md) | 27 | Registre tenu par l'ENISA |
| [articles-28-a-30-donnees-partage-notification-volontaire.md](reglementation/articles-28-a-30-donnees-partage-notification-volontaire.md) | 28-30 | Données WHOIS, partage d'informations, notification volontaire |

### Contrôle et sanctions
| Fichier | Article(s) | Sujet |
|---|---|---|
| [article-31-supervision-generale.md](reglementation/article-31-supervision-generale.md) | 31 | Principes de la supervision |
| [article-32-supervision-entites-essentielles.md](reglementation/article-32-supervision-entites-essentielles.md) | 32 | Contrôle *ex ante*, pouvoirs forts |
| [article-33-supervision-entites-importantes.md](reglementation/article-33-supervision-entites-importantes.md) | 33 | Contrôle *ex post* |
| [article-34-amendes-administratives.md](reglementation/article-34-amendes-administratives.md) | 34 | **10 M€ / 2 % et 7 M€ / 1,4 %** |
| [article-35-violation-de-donnees-personnelles.md](reglementation/article-35-violation-de-donnees-personnelles.md) | 35 | Articulation avec le RGPD |
| [articles-36-a-45-dispositions-finales.md](reglementation/articles-36-a-45-dispositions-finales.md) | 36-45 | Sanctions, réexamen, abrogation de NIS1 |

### Les annexes
| Fichier | Sujet |
|---|---|
| [annexe-1-secteurs-hautement-critiques.md](reglementation/annexe-1-secteurs-hautement-critiques.md) | Les 11 secteurs de l'annexe I (dont **eau potable**) |
| [annexe-2-autres-secteurs-critiques.md](reglementation/annexe-2-autres-secteurs-critiques.md) | Les 7 secteurs de l'annexe II |

---

## 🔧 Plan du cours technique

| Fichier | Sujet |
|---|---|
| [01-it-vs-ot.md](technique/01-it-vs-ot.md) | Deux mondes, deux priorités |
| [02-modele-de-purdue.md](technique/02-modele-de-purdue.md) | Le modèle de référence en 6 niveaux |
| [03-vlan-et-segmentation.md](technique/03-vlan-et-segmentation.md) | VLAN, trunk, routage inter-VLAN |
| [04-pare-feu-et-matrice-de-flux.md](technique/04-pare-feu-et-matrice-de-flux.md) | Écrire une politique de filtrage qui tient |
| [05-dmz-industrielle.md](technique/05-dmz-industrielle.md) | Le point de passage obligé |
| [06-acces-distant-vpn-et-bastion.md](technique/06-acces-distant-vpn-et-bastion.md) | Remplacer TeamViewer proprement |
| [07-protocoles-industriels.md](technique/07-protocoles-industriels.md) | Modbus, IEC-104, OPC UA et leurs faiblesses |
| [08-detection-et-journalisation.md](technique/08-detection-et-journalisation.md) | Voir ce qui se passe |
| [09-sauvegardes-et-continuite.md](technique/09-sauvegardes-et-continuite.md) | 3-2-1, RTO/RPO, modes dégradés |
| [10-gestion-de-crise-cyber.md](technique/10-gestion-de-crise-cyber.md) | Organiser, décider, communiquer |

---

## 🎓 Réviser pour l'oral

Un quiz de révision est disponible : [`reglementation/quiz-revision.md`](reglementation/quiz-revision.md).

⬅️ [Retour au README principal](../README.md)
