# Annexe E — Notification d'une violation de données personnelles (CNIL)

> 📗 **Fondement** : article 33 du RGPD (règlement (UE) 2016/679) — notification à l'autorité de
> contrôle dans les **72 heures** après en avoir pris connaissance.
> 📗 **Articulation avec NIS2** : article 35 de la directive (UE) 2022/2555 — les autorités
> s'informent mutuellement ; si une amende RGPD est prononcée, l'autorité NIS2 n'inflige pas
> d'amende pour le **même comportement**, mais conserve ses autres mesures d'exécution.

---

## ⚠️ Le point à ne surtout pas confondre

| | **NIS2** (art. 23) | **RGPD** (art. 33-34) |
|---|---|---|
| Objet | Incident affectant les services et les systèmes | **Violation de données à caractère personnel** |
| Autorité | ANSSI / CSIRT national | **CNIL** |
| Délais | **24 h**, puis **72 h**, puis **1 mois** | **72 h**, une seule échéance |
| Point de départ | Connaissance de **l'incident** | Connaissance de **la violation** |
| Information des personnes | Destinataires des services, si affectés (art. 23(1)) | Personnes concernées, si **risque élevé** (art. 34 RGPD) |

> 🔴 **Les deux notifications sont dues.** L'article 35 de NIS2 ne porte que sur le **cumul des
> amendes**, jamais sur le cumul des **obligations**.
> Dans le scénario, T0 NIS2 est le 16/03 à 04 h 12 ; la connaissance de la **violation de données**
> (exfiltration confirmée) date du 18/03 au matin. Les deux horloges sont **distinctes**.

---

## NOTIFICATION DE VIOLATION DE DONNÉES À CARACTÈRE PERSONNEL

**Fondement** : article 33 du règlement (UE) 2016/679
**Autorité destinataire** : Commission nationale de l'informatique et des libertés
**Responsable de traitement** : HydroRégie
**Référence interne** : `VIOL-2027-0318-001`
**Date d'envoi** : **jeudi 18 mars 2027, 17 h 30**
**Type de notification** : ☑ initiale ☐ complémentaire ☐ définitive

---

### 1. Responsable du traitement

| Champ | Valeur |
|---|---|
| Organisme | HydroRégie |
| Adresse | `<adresse>` |
| Numéro SIREN | `<n°>` |
| **Délégué à la protection des données** | `<nom>` — `<courriel>` — `<téléphone>` |

### 2. Nature de la violation

| Champ | Valeur |
|---|---|
| Type | ☑ Confidentialité (exfiltration) ☑ Disponibilité (chiffrement) ☐ Intégrité |
| Origine | ☑ Acte malveillant externe ☐ Erreur interne ☐ Défaillance technique |
| Date de la violation | Exfiltration entre le **12** et le **14 mars 2027** |
| **Date de prise de connaissance de la violation** | **18 mars 2027 au matin** |
| Violation toujours en cours ? | Non — accès de l'attaquant révoqué le 17/03 |

**Description** :

> Dans le cadre d'une attaque par rançongiciel détectée le 16 mars 2027, les auteurs ont exfiltré
> environ **42 Go de données** depuis les serveurs de fichiers d'HydroRégie avant de procéder au
> chiffrement. Les données exfiltrées comprennent des exports de la base de gestion des abonnés.
> L'exfiltration a été confirmée le 18 mars par l'analyse des journaux de flux sortants.

### 3. Catégories et volume de données concernées

| Catégorie de données | Concernée | Volume estimé |
|---|---|---|
| Identité (nom, prénom) | ✅ | 240 000 personnes |
| Coordonnées (adresse postale, téléphone, courriel) | ✅ | 240 000 |
| **Coordonnées bancaires (IBAN de prélèvement)** | ✅ | ≈ 186 000 |
| Historique de consommation et de facturation | ✅ | 240 000 |
| Données de connexion à l'espace abonné (identifiants, empreintes de mots de passe) | ✅ | ≈ 92 000 |
| Numéros de carte bancaire | ❌ | Non conservés par HydroRégie |
| Données sensibles au sens de l'art. 9 RGPD | ❌ | Aucune |
| Données de mineurs | ⚠️ Indirectement | Membres du foyer, non identifiés distinctement |

**Catégories de personnes concernées** : abonnés au service d'eau potable (particuliers,
copropriétés, entreprises, collectivités).

### 4. Conséquences probables

| Risque | Niveau | Justification |
|---|---|---|
| **Usurpation d'identité** | 🟠 Élevé | Identité + adresse + coordonnées complètes |
| **Escroquerie ciblée / hameçonnage** | 🔴 **Très élevé** | Les données permettent des messages crédibles se faisant passer pour HydroRégie |
| **Prélèvement frauduleux** | 🟠 Élevé | IBAN exposés — protection légale existante mais démarche à la charge de la personne |
| Réutilisation de mots de passe | 🟠 Élevé | Empreintes exposées ; réutilisation fréquente sur d'autres services |
| Atteinte à la vie privée | 🟡 Modéré | La consommation d'eau révèle des habitudes d'occupation du logement |
| Publication des données | 🟠 Élevé | Mode opératoire de double extorsion : menace de divulgation |

> ➡️ **Le risque est qualifié d'élevé** au sens de l'article 34 du RGPD.
> **Conséquence : information individuelle des personnes concernées obligatoire.**

### 5. Mesures prises et envisagées

| # | Mesure | Date |
|---|---|---|
| 1 | Isolement des systèmes et révocation des accès de l'attaquant | 16-17/03 |
| 2 | Réinitialisation de tous les mots de passe internes | 17/03 |
| 3 | Réinitialisation forcée des mots de passe de l'espace abonné | 26/03 |
| 4 | Blocage des adresses de commande et contrôle | 16/03 |
| 5 | Reconstruction sur socle sain | 17-26/03 |
| 6 | **Information publique des usagers** (art. 23(1) NIS2) | 16/03 et 19/03 |
| 7 | **Information individuelle des personnes concernées** (art. 34 RGPD) | 📅 prévue au 27/03 |
| 8 | Dépôt de plainte | 17/03 |
| 9 | Notification à l'autorité NIS2 (24 h et 72 h) | 16/03 et 18/03 |
| 10 | Surveillance des espaces de divulgation | En continu |
| 11 | MFA généralisé aux comptes à privilèges et prestataires | 30/03 |
| 12 | Segmentation IT/OT accélérée | 31/12/2027 |

### 6. Information des personnes concernées (art. 34 RGPD)

| Champ | Valeur |
|---|---|
| Information réalisée ? | ☐ Oui ☑ **Prévue** — le 27/03/2027 |
| Modalités | Courriel individuel (abonnés disposant d'une adresse), courrier postal pour les autres, communiqué public en complément |
| Contenu | Nature de la violation, catégories de données, conséquences probables, **mesures recommandées** (surveillance des relevés bancaires, vigilance face aux escroqueries, changement des mots de passe réutilisés), coordonnées du DPO |

📗 L'article 34 du RGPD impose une communication **en des termes clairs et simples**. Le message
figure en [annexe D, message n° 2](D-information-usagers.md).

### 7. Suites

> Une **notification complémentaire** sera transmise dès que le périmètre exact des données
> exfiltrées aura été établi (analyse des journaux en cours), et en cas de divulgation publique des
> données.

---

**Rédigé par** : `<nom>`, DPO · **Validé par** : `<nom>`, Directeur général
**Transmis le** : 18/03/2027 à 17 h 30 · **Accusé de réception** : `<n°>`

---

## 📋 Aide-mémoire

| ✅ À faire | ❌ À éviter |
|---|---|
| Distinguer **deux horloges** : T0 NIS2 et connaissance de la violation RGPD | Croire que les 72 h RGPD partent du même instant |
| Notifier même si le périmètre exact n'est pas connu (notification complémentaire prévue par l'art. 33(4)) | Attendre l'analyse complète |
| Évaluer le risque **du point de vue des personnes**, pas de l'organisme | Minimiser pour éviter l'information individuelle |
| Coordonner RSSI et DPO sur **une seule main courante** | Deux récits divergents envoyés à deux autorités |
| Documenter la violation dans le **registre interne** (art. 33(5) RGPD) même si elle n'est pas notifiée | Ne rien tracer |

⬅️ [Annexe D](D-information-usagers.md) · ➡️ [Annexe F — Registre des écarts](F-registre-des-ecarts.csv)
