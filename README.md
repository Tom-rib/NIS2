# 🛡️ Mise en conformité NIS2 — cas HydroRégie

> **Projet B3 — Administration systèmes & réseaux**
> Cas pratique de mise en conformité à la **directive (UE) 2022/2555 (NIS2)** pour
> **HydroRégie**, régie des eaux desservant 450 000 habitants, qualifiée **entité essentielle**.
>
> Ce dépôt est à la fois **le rendu du projet** et **un cours condensé** réutilisable :
> chaque fichier se lit seul, comme une fiche mémo.

---

## 🎯 En une phrase

HydroRégie distribue l'eau potable à 450 000 habitants avec un réseau informatique **plat** :
la bureautique et les automates qui pilotent les pompes sont sur le même réseau.
NIS2 l'oblige à se qualifier, à mesurer ses écarts, à **séparer l'IT de l'OT**, et à savoir
notifier un incident en **24 h / 72 h / 1 mois**. Ce dépôt fait les quatre.

---

## 🗺️ Sommaire

### 📘 Le parcours pédagogique (à lire dans l'ordre la première fois)

| # | Fiche | Ce que tu y apprends |
|---|---|---|
| 01 | [Préparation](01_preparation.md) | Le contexte, le vocabulaire, la maquette de test, la méthode de travail |
| 02 | [Qualification & cadre réglementaire](02_qualification.md) | Comment décider si une entité est concernée, et à quel titre |
| 03 | [Mise en conformité & architecture](03_mise_en_conformite.md) | Les mesures de l'article 21, la segmentation IT/OT, les choix techniques |
| 04 | [Tests & vérifications](04_tests.md) | Comment **prouver** que la segmentation et les procédures fonctionnent |
| 05 | [Annexes](05_annexes.md) | Glossaire, commandes utiles, dépannage, modèles, sources |

### 📕 Le cours

| Dossier | Contenu |
|---|---|
| [`Cour/reglementation/`](Cour/reglementation/) | **Un fichier par article de NIS2**, réécrit en français simple |
| [`Cour/technique/`](Cour/technique/) | Les concepts techniques : IT vs OT, modèle de Purdue, VLAN, DMZ, VPN, SCADA, crise |

### 📗 Le rendu (réponse au sujet, job par job)

| Bloc | Livrable attendu | Fichier |
|---|---|---|
| 1 | Note de qualification réglementaire | [`Documentation/job-1-qualification.md`](Documentation/job-1-qualification.md) |
| 2 | Analyse d'écart + feuille de route | [`Documentation/job-2-analyse-ecart.md`](Documentation/job-2-analyse-ecart.md) |
| 3 | Schéma d'architecture segmentée IT/OT | [`Documentation/job-3-architecture.md`](Documentation/job-3-architecture.md) |
| 4 | Chronologie de crise + notifications rédigées | [`Documentation/job-4-crise-notifications.md`](Documentation/job-4-crise-notifications.md) |
| — | Notifications prêtes à envoyer (24 h / 72 h / 1 mois) | [`Documentation/annexes/`](Documentation/annexes/) |

### 📄 Le document unique

| Fichier | Usage |
|---|---|
| [`Documentation.md`](Documentation.md) | Réponse complète au sujet, d'un seul tenant (~2 700 lignes) |
| `Documentation.docx` | Même contenu, format Word — page de garde, sommaire automatique, à imprimer ou à déposer |

> ⚙️ Ces deux fichiers sont **générés** à partir de `Documentation/`. Pour les mettre à jour :
> corriger le livrable concerné, puis relancer les deux scripts de
> [`scripts/documentation/`](scripts/documentation/). Ne jamais les éditer à la main.

### 🧰 Les fichiers techniques

| Dossier | Contenu |
|---|---|
| [`scripts/`](scripts/) | Configurations VLAN, règles de pare-feu, scripts de vérification, sauvegarde |
| [`schemas/`](schemas/) | Schémas d'architecture (avant / après), format Mermaid + HTML |

---

## ⚡ Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/<ton-compte>/NIS2.git
cd NIS2

# Lire le rendu dans l'ordre
cat Documentation/job-1-qualification.md
```

Aucun outil n'est obligatoire pour lire le rendu. Pour **rejouer la partie technique**,
voir les prérequis dans [01_preparation.md](01_preparation.md) (3 VM + un pare-feu virtuel).

---

## ⚠️ Ce que ce dépôt affirme, et ce qu'il suppose

Le projet distingue systématiquement trois natures d'information :

| Marqueur | Signification |
|---|---|
| 📗 **Texte** | Vient directement de la directive (UE) 2022/2555 — l'article est cité |
| 📙 **Source** | Vient de l'ANSSI, de l'ENISA ou d'un texte officiel — le lien est donné |
| 📕 **Hypothèse** | Choix de travail fait pour ce cas d'école (chiffres HydroRégie, dates, scénario) |

**Point de vigilance important** (vérifié le 10/09/2026) : au niveau européen, NIS2 s'applique
depuis le **18 octobre 2024** (art. 41). En France, **la loi de transposition n'est pas encore
promulguée** — le projet de loi « résilience des infrastructures critiques et renforcement de la
cybersécurité » a été adopté par le Sénat les 11-12 mars 2025 et voté en commission spéciale à
l'Assemblée nationale le 10 septembre 2025. Les décrets d'application suivront.
👉 Toutes les obligations citées ici s'appuient donc sur **le texte de la directive**, pas sur un
droit français qui n'existe pas encore. Voir [`Cour/reglementation/00-calendrier-et-transposition.md`](Cour/reglementation/00-calendrier-et-transposition.md).

---

## 🎓 Compétences travaillées

- Qualifier une entité au regard de NIS2 (secteur, taille, statut essentiel / important)
- Conduire une analyse d'écart et bâtir une feuille de route datée et responsabilisée
- Concevoir une architecture réseau segmentée IT / OT (zones, DMZ, VLAN, pare-feu, VPN)
- Piloter une crise cyber et respecter les délais de notification réglementaire

---

## 📚 Sources principales

- [Directive (UE) 2022/2555 — texte intégral (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- [ANSSI — Directive NIS 2 (MesServicesCyber)](https://messervices.cyber.gouv.fr/nis2)
- [MonEspaceNIS2 — FAQ officielle](https://aide.monespacenis2.cyber.gouv.fr/)
- [ENISA — NIS2 Directive](https://www.enisa.europa.eu/topics/nis-directive)
- [Dossier législatif — projet de loi résilience (Légifrance)](https://www.legifrance.gouv.fr/dossierlegislatif/JORFDOLE000050349138/)

---

*Dépôt rendu dans le cadre du cas pratique NIS2 / HydroRégie — 2 jours, 4 blocs.*
