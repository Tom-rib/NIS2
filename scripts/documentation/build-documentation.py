#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assemble Documentation.md a partir des livrables job-1 a job-4 et des annexes."""
import re
import pathlib

RACINE = pathlib.Path(r"C:\Users\Tom\Documents\Github\B3_TempPlein\NIS2")
DOC = RACINE / "Documentation"

EN_TETE = """# Mise en conformité NIS2 — HydroRégie

## Réponse complète au cas pratique

---

| | |
|---|---|
| **Entité** | HydroRégie — régie des eaux, 450 000 habitants desservis |
| **Objet** | Mise en conformité à la directive (UE) 2022/2555 (NIS2) |
| **Statut de l'entité** | Entité essentielle — art. 3(1)(a), annexe I point 6 |
| **Autorité compétente** | France — ANSSI |
| **Document** | Réponse aux 4 blocs du cas pratique |
| **Date** | 10 septembre 2026 |
| **Version** | 1.0 |
| **Classification** | Diffusion restreinte |

---

## Avertissement méthodologique

Ce document distingue systématiquement trois natures d'information :

| Marqueur | Signification |
|---|---|
| 📗 **Texte** | Provient directement de la directive (UE) 2022/2555 — l'article est cité |
| 📙 **Source** | Provient d'une source officielle (ANSSI, ENISA, Légifrance) — le lien est donné |
| 📕 **Hypothèse** | Hypothèse de travail construite pour ce cas d'école (chiffres, dates, scénario) |

**Point de vigilance sur le droit applicable** (vérifié le 10 septembre 2026) : au niveau européen,
NIS2 s'applique depuis le **18 octobre 2024** (art. 41) et abroge NIS1 à cette même date (art. 44).
En France, **la loi de transposition n'est pas promulguée à ce jour** : le projet de loi
« résilience des infrastructures critiques et renforcement de la cybersécurité » a été adopté par le
Sénat les 11 et 12 mars 2025, puis voté en commission spéciale à l'Assemblée nationale le
10 septembre 2025 ; les décrets et arrêtés suivront la promulgation.

**Conséquence** : toutes les obligations citées dans ce document s'appuient sur **le texte de la
directive**, et non sur un droit français qui n'existe pas encore. Les points qui dépendront des
textes nationaux (seuils précis de qualification d'un incident, modalités exactes d'enregistrement,
calendrier d'application) sont signalés comme tels, et un jalon de revue réglementaire est inscrit
à la feuille de route.

---

## Sommaire

| Partie | Livrable | Bloc du sujet |
|---|---|---|
| **1** | Note de qualification réglementaire | Bloc 1 |
| **2** | Analyse d'écart et feuille de route de mise en conformité | Bloc 2 |
| **3** | Architecture réseau segmentée IT / OT | Bloc 3 |
| **4** | Chronologie de gestion de crise et notifications réglementaires | Bloc 4 |
| **A** | Annexe — Alerte précoce (24 h) | Bloc 4 |
| **B** | Annexe — Notification d'incident (72 h) | Bloc 4 |
| **C** | Annexe — Rapport final (1 mois) | Bloc 4 |
| **D** | Annexe — Information des usagers | Bloc 4 |
| **E** | Annexe — Notification CNIL (RGPD) | Bloc 4 |

---

## Le projet en une page

**Le contexte.** HydroRégie capte, traite, stocke et distribue l'eau potable à 450 000 habitants
répartis sur 62 communes, pour 240 000 abonnés facturés. Son système d'information de gestion (IT)
et son système industriel (OT) partagent aujourd'hui **le même réseau**, sans aucun cloisonnement.
Un courrier de l'autorité nationale vient de confirmer son statut d'**entité essentielle**.

**Le risque.** Sur un réseau plat, une compromission bureautique — une pièce jointe piégée, un mot
de passe volé — donne un accès direct aux automates qui commandent les pompes, les vannes et la
chloration. L'enjeu n'est pas la fuite de données : c'est **la continuité et la qualité de l'eau
potable**, donc la santé publique.

**La réponse, en quatre temps.**

1. **Qualifier** — HydroRégie relève de l'annexe I, point 6 (eau potable) et dépasse les seuils de
   la grande entreprise : elle est **entité essentielle** au titre de l'article 3(1)(a). La
   qualification est confirmée par trois voies indépendantes.
2. **Mesurer** — Sa maturité au regard des dix domaines de l'article 21 est de **0,6 sur 4**, avec
   **18 écarts** dont **6 critiques**. Un plan de 24 mois, chiffré à environ **956 k€**, porte cette
   maturité à **3,3 sur 4**.
3. **Concevoir** — Une architecture en **9 zones**, séparées par **deux pare-feu en cascade** et une
   **DMZ industrielle** qui constitue le seul point de rencontre entre l'IT et l'OT. Aucun flux
   direct entre la bureautique et l'industriel ; le seul protocole franchissant une frontière de
   zone est OPC UA, authentifié et chiffré.
4. **S'entraîner** — Un scénario de crise complet montre que les délais de **24 heures**,
   **72 heures** et **un mois** sont tenables, et surtout que **l'eau continue de couler** pendant
   six jours d'exploitation en mode dégradé autonome.

**La conviction du projet.** La segmentation IT/OT n'est pas une exigence de conformité : c'est la
mesure qui permet de continuer à distribuer de l'eau pendant qu'on traite l'incident. Tout le reste
en découle.

---
"""

FICHIERS = [
    ("PARTIE 1", DOC / "job-1-qualification.md"),
    ("PARTIE 2", DOC / "job-2-analyse-ecart.md"),
    ("PARTIE 3", DOC / "job-3-architecture.md"),
    ("PARTIE 4", DOC / "job-4-crise-notifications.md"),
    ("ANNEXE A", DOC / "annexes" / "A-alerte-precoce-24h.md"),
    ("ANNEXE B", DOC / "annexes" / "B-notification-72h.md"),
    ("ANNEXE C", DOC / "annexes" / "C-rapport-final-1-mois.md"),
    ("ANNEXE D", DOC / "annexes" / "D-information-usagers.md"),
    ("ANNEXE E", DOC / "annexes" / "E-notification-cnil.md"),
]

NAV = re.compile(r"^\s*(⬅️|➡️|🏠|📎 \[)")


def nettoyer(texte: str) -> str:
    """Retire les lignes de navigation entre fichiers et demote les titres."""
    lignes = []
    dans_code = False
    for ligne in texte.splitlines():
        if ligne.lstrip().startswith("```"):
            dans_code = not dans_code
            lignes.append(ligne)
            continue
        if not dans_code:
            if NAV.match(ligne):
                continue
            if re.match(r"^#{1,5} ", ligne):
                ligne = "#" + ligne
        lignes.append(ligne)
    # supprime les ---- orphelins en fin de fichier
    while lignes and lignes[-1].strip() in ("", "---"):
        lignes.pop()
    return "\n".join(lignes)


def delier(texte: str) -> str:
    """Transforme les liens relatifs en texte simple (le document est autonome)."""
    def remplace(m):
        libelle, cible = m.group(1), m.group(2)
        if cible.startswith(("http://", "https://", "#")):
            return m.group(0)
        return libelle
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", remplace, texte)


morceaux = [EN_TETE]
for titre, chemin in FICHIERS:
    brut = chemin.read_text(encoding="utf-8")
    corps = delier(nettoyer(brut))
    morceaux.append(f"\n<!-- pagebreak -->\n\n# {titre}\n\n{corps}\n\n---\n")

FIN = """
# Sources et fondements

## Textes de référence

| Référence | Objet |
|---|---|
| Directive (UE) 2022/2555 du 14 décembre 2022 | NIS2 — texte principal |
| Directive (UE) 2022/2557 | REC — résilience des entités critiques |
| Recommandation 2003/361/CE | Définition des catégories d'entreprises (seuils de taille) |
| Directive (UE) 2020/2184 | Eau destinée à la consommation humaine |
| Règlement (UE) 2016/679 | RGPD |
| Règlement (UE) 2022/2554 | DORA — secteur financier |
| Règlement d'exécution (UE) 2024/2690 | Exigences techniques art. 21 pour certaines entités numériques |

## Articles de NIS2 mobilisés dans ce document

| Article | Objet | Partie |
|---|---|---|
| art. 2(1) et 2(2) | Champ d'application, cas particuliers | 1 |
| art. 3(1)(a) | Entité essentielle | 1 |
| art. 3(4) | Enregistrement et mise à jour sous deux semaines | 1 |
| art. 4 | Actes sectoriels (lex specialis) | 1 |
| art. 5 | Harmonisation minimale | 2 |
| art. 6 | Définitions | 1 |
| art. 11 | Missions des CSIRT | 4 |
| art. 20 | Gouvernance et responsabilité des dirigeants | 2 |
| art. 21(1) à 21(4) | Mesures de gestion des risques | 2, 3 |
| art. 23(1) à 23(5) | Notification des incidents | 4 |
| art. 25 | Normalisation | 3 |
| art. 26 | Compétence territoriale | 1 |
| art. 29 et 30 | Partage d'informations, notification volontaire | 4 |
| art. 32 | Supervision des entités essentielles | 1, 2 |
| art. 33 | Supervision des entités importantes | 1 |
| art. 34(4) et 34(5) | Amendes administratives | 1, 2 |
| art. 35 | Articulation avec le RGPD | 4 |
| art. 41 et 44 | Transposition et abrogation de NIS1 | Avertissement |
| annexe I, point 6 | Secteur de l'eau potable | 1 |

## Sources officielles consultées

- Directive (UE) 2022/2555 — texte intégral : https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- ANSSI — Directive NIS 2 : https://messervices.cyber.gouv.fr/nis2
- MonEspaceNIS2 — FAQ officielle : https://aide.monespacenis2.cyber.gouv.fr/
- Dossier législatif du projet de loi résilience (référence PRMD2412608L) :
  https://www.legifrance.gouv.fr/dossierlegislatif/JORFDOLE000050349138/
- ENISA — NIS Directive : https://www.enisa.europa.eu/topics/nis-directive
- CERT-FR — alertes et avis : https://www.cert.ssi.gouv.fr/

## Référentiels techniques mobilisés

| Référentiel | Usage dans ce document |
|---|---|
| IEC 62443 | Modèle zones et conduits — fondement du découpage de la partie 3 |
| Modèle de Purdue (PERA) | Structuration en niveaux 0 à 5 |
| ANSSI — *La cybersécurité des systèmes industriels* | Mesures OT |
| ANSSI — *Guide d'hygiène informatique* | Art. 21(2)(g) |
| EBIOS Risk Manager | Art. 21(2)(a) — analyse de risques |
| ISO 22301 | Art. 21(2)(c) — continuité d'activité |

---

*Fin du document — Mise en conformité NIS2, HydroRégie, version 1.0 du 10 septembre 2026.*
"""

morceaux.append(FIN)

sortie = RACINE / "Documentation.md"
sortie.write_text("\n".join(morceaux), encoding="utf-8")
print("Documentation.md ecrit :", len(sortie.read_text(encoding='utf-8').splitlines()), "lignes")
