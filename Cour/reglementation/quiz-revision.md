# 🎓 Quiz de révision — NIS2

> 🎯 **Usage** : à faire la veille de l'oral. 25 questions, réponses cachées.
> Objectif : **20/25**. En dessous, relire les articles 3, 20, 21, 23, 32 et 34.

---

## Partie 1 — Le cadre (5 questions)

**1.** Quel est le numéro officiel de la directive NIS2 et sa date d'adoption ?
<details><summary>Réponse</summary>Directive **(UE) 2022/2555** du Parlement européen et du Conseil du **14 décembre 2022**.</details>

**2.** Depuis quelle date NIS2 s'applique-t-elle, et quelle était la date limite de transposition ?
<details><summary>Réponse</summary>Application depuis le **18 octobre 2024** ; transposition due au **17 octobre 2024** (art. 41). NIS1 est abrogée au 18/10/2024 (art. 44).</details>

**3.** Où en est la transposition française ?
<details><summary>Réponse</summary>**Non achevée.** Le projet de loi « résilience des infrastructures critiques et renforcement de la cybersécurité » a été adopté par le Sénat les 11-12 mars 2025 et voté en commission spéciale à l'Assemblée nationale le 10 septembre 2025. Les décrets suivront la promulgation.</details>

**4.** Combien de secteurs et combien d'entités NIS2 concerne-t-elle en France ?
<details><summary>Réponse</summary>**18 secteurs**, environ **15 000 entités** (source ANSSI), contre 6 secteurs et ~500 opérateurs sous NIS1.</details>

**5.** Quelle est la différence entre une directive et un règlement européen ?
<details><summary>Réponse</summary>La **directive** doit être **transposée** dans le droit national ; le **règlement** est **directement applicable**. NIS2 est une directive, le RGPD et DORA sont des règlements.</details>

---

## Partie 2 — La qualification (7 questions)

**6.** Quels sont les deux critères de la règle générale du champ d'application ?
<details><summary>Réponse</summary>Le **secteur** (annexe I ou II) et la **taille** (au moins moyenne entreprise au sens de la recommandation **2003/361/CE**) — art. 2(1).</details>

**7.** Une entreprise de 240 salariés, 60 M€ de CA, 30 M€ de bilan : grande ou moyenne ?
<details><summary>Réponse</summary>**Moyenne.** Sous 250 salariés, il faut **CA > 50 M€ ET bilan > 43 M€**. Ici le bilan est trop faible.</details>

**8.** Dans quel point de l'annexe I figure l'eau potable ?
<details><summary>Réponse</summary>**Annexe I, point 6** — fournisseurs et distributeurs d'eau destinée à la consommation humaine au sens de la directive (UE) 2020/2184.</details>

**9.** Quel article fait d'une grande entreprise de l'annexe I une entité essentielle ?
<details><summary>Réponse</summary>**Article 3(1)(a).**</details>

**10.** Citez deux cas où la taille ne compte pas.
<details><summary>Réponse</summary>Art. 2(2) : fournisseurs DNS / registres TLD / prestataires de services de confiance ; **seul prestataire** d'un service essentiel dans un État ; entité dont la perturbation aurait un **impact important sur la santé publique**, la sécurité ou la sûreté publiques ; administration publique centrale ; risque systémique transfrontalier.</details>

**11.** Quelles informations faut-il transmettre à l'autorité pour l'enregistrement, et sous quel délai les mettre à jour ?
<details><summary>Réponse</summary>Art. 3(4) : nom, adresse, coordonnées à jour (courriels, plages IP, téléphones), secteur et sous-secteur, États membres où des services sont fournis. Mise à jour **sans délai et au plus tard sous deux semaines**.</details>

**12.** Une entreprise de l'annexe II avec 800 salariés est-elle essentielle ?
<details><summary>Réponse</summary>**Non — importante.** L'annexe II ne donne jamais le statut essentiel par la taille.</details>

---

## Partie 3 — Les obligations (7 questions)

**13.** Quelles sont les trois obligations de l'organe de direction (art. 20(1)) ?
<details><summary>Réponse</summary>**Approuver** les mesures, **superviser** leur mise en œuvre, et pouvoir être **tenu responsable** des manquements.</details>

**14.** Que dit l'article 20(2) ?
<details><summary>Réponse</summary>Les dirigeants doivent **suivre une formation** cyber, et l'entité doit offrir une **formation similaire à ses employés**, de manière régulière.</details>

**15.** Citez les 10 domaines de l'article 21(2).
<details><summary>Réponse</summary>(a) analyse des risques et sécurité des SI — (b) gestion des incidents — (c) continuité, sauvegardes, reprise, gestion de crise — (d) sécurité de la chaîne d'approvisionnement — (e) acquisition, développement, maintenance et gestion des vulnérabilités — (f) évaluation de l'efficacité des mesures — (g) cyberhygiène et formation — (h) cryptographie et chiffrement — (i) RH, contrôle d'accès, gestion des actifs — (j) MFA, communications sécurisées et communication d'urgence.</details>

**16.** Que signifie l'approche « tous risques » ?
<details><summary>Réponse</summary>Les mesures ne visent pas que les cyberattaques : pannes, incendie, inondation, erreur humaine, défaillance fournisseur. Le texte vise aussi **l'environnement physique** des systèmes.</details>

**17.** Sur quels critères s'apprécie la proportionnalité (art. 21(1)) ?
<details><summary>Réponse</summary>État des connaissances, normes applicables, **coût**, degré d'exposition au risque, taille de l'entité, probabilité et gravité des incidents, **y compris leurs conséquences sociétales et économiques**.</details>

**18.** Que doit faire une entité qui constate qu'elle ne respecte pas l'article 21 ?
<details><summary>Réponse</summary>Art. 21(4) : prendre **sans délai** les mesures correctives nécessaires. Constater un écart et ne rien faire est un manquement.</details>

**19.** Quel article impose de prendre en compte les vulnérabilités des fournisseurs directs ?
<details><summary>Réponse</summary>**Art. 21(3)**, en complément du point (d) de l'art. 21(2).</details>

---

## Partie 4 — La notification (3 questions)

**20.** Donnez les trois délais de l'article 23 et leurs points de départ.
<details><summary>Réponse</summary>**Alerte précoce : 24 h** après avoir eu connaissance de l'incident (23(4)(a)). **Notification d'incident : 72 h** après en avoir eu connaissance (23(4)(b)). **Rapport final : 1 mois après la notification des 72 h** (23(4)(d)) — ⚠️ pas après la découverte.</details>

**21.** Qu'est-ce qu'un incident « important » au sens de l'article 23(3) ?
<details><summary>Réponse</summary>Un incident qui **a causé ou est susceptible de causer** une perturbation opérationnelle grave des services ou des pertes financières pour l'entité, **ou** qui **a affecté ou est susceptible d'affecter** d'autres personnes en causant des dommages matériels ou immatériels considérables.</details>

**22.** Que reçoit l'entité après son alerte précoce ?
<details><summary>Réponse</summary>Art. 23(5) : une **réponse du CSIRT ou de l'autorité dans les 24 heures**, comprenant des orientations, un appui à la mise en œuvre de mesures, et le cas échéant une **assistance technique**.</details>

---

## Partie 5 — Contrôle et sanctions (3 questions)

**23.** Quelle est la différence de supervision entre EE et EI ?
<details><summary>Réponse</summary>EE : supervision ***ex ante* et *ex post*** (art. 32) — audits, inspections, scans **sans incident préalable**. EI : ***ex post* uniquement** (art. 33), sur éléments laissant présumer un manquement.</details>

**24.** Quels sont les montants maximaux d'amende ?
<details><summary>Réponse</summary>EE : **au moins 10 M€ ou 2 %** du CA annuel mondial, **le plus élevé** (art. 34(4)). EI : **au moins 7 M€ ou 1,4 %**, le plus élevé (art. 34(5)).</details>

**25.** Que se passe-t-il si un incident NIS2 est aussi une violation de données personnelles ?
<details><summary>Réponse</summary>Art. 35 : les autorités s'informent. Si la CNIL inflige une amende RGPD, l'autorité NIS2 **n'inflige pas d'amende** pour le **même comportement** — mais elle conserve ses **autres mesures d'exécution**. Les **deux notifications restent dues** (ANSSI 24 h/72 h/1 mois, CNIL 72 h).</details>

---

## 🏆 Barème

| Score | Verdict |
|---|---|
| 23-25 | Prêt pour l'oral |
| 20-22 | Solide — revoir les articles ratés |
| 15-19 | Relire les articles 3, 21, 23 |
| < 15 | Reprendre [00-comprendre-nis2.md](00-comprendre-nis2.md) et le parcours complet |

---

⬅️ [Annexe II](annexe-2-autres-secteurs-critiques.md) · 🏠 [Sommaire du cours](../README.md)
