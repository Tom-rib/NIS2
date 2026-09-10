# 04 — Tests & vérifications

> 🎯 **Objectifs de cette fiche**
> 1. Savoir **prouver** que la segmentation fonctionne (et pas seulement l'affirmer).
> 2. Savoir tester les procédures : sauvegardes, accès distant, notification.
> 3. Savoir organiser un **exercice de crise** de bout en bout.
> 4. Constituer les **preuves** attendues par un contrôle (art. 21(2)(f) et art. 32).
>
> ⏱️ Lecture : 15 minutes. Manipulation : 1 à 2 heures sur la maquette.

---

## 0. Pourquoi cette fiche existe

📗 **Article 21(2)(f)** impose des « politiques et procédures pour évaluer l'**efficacité** des
mesures de gestion des risques ». Et 📗 **l'article 32** permet à l'autorité de soumettre une entité
essentielle à des **audits, inspections sur site et scans de sécurité**, **sans incident préalable**.

👉 Traduction : il ne suffit pas d'avoir un beau schéma. Il faut des **preuves datées** que la
règle appliquée correspond au schéma. Cette fiche produit ces preuves.

---

## 1. Tester la segmentation IT / OT

### 1.1 Test A — Le blocage bureautique → industriel (le test qui compte)

**Ce qu'on veut prouver** : un poste bureautique (Z2 / VLAN 110) ne peut atteindre **aucun**
automate (Z7 / VLAN 220).

```bash
# Depuis un poste bureautique, vers un automate
# 1) Le port Modbus doit etre INJOIGNABLE
nmap -Pn -p 502,2404,44818 10.220.10.15

# Resultat ATTENDU :
#   502/tcp   filtered mbap
#   2404/tcp  filtered iec-104
#   44818/tcp filtered EtherNet/IP
# "filtered" = le pare-feu a jete le paquet. C'est le bon resultat.
# "closed" serait moins bon : cela signifie que le paquet a atteint la cible.
```

```bash
# 2) Balayage complet du sous-reseau OT : aucun hote ne doit repondre
nmap -sn 10.220.0.0/22

# Resultat ATTENDU : "0 hosts up"
```

```bash
# 3) Tentative d'ecriture Modbus (le pire scenario : changer une consigne)
mbpoll -a 1 -t 4 -r 100 -0 10.220.10.15 1
# Resultat ATTENDU : timeout / "Connection timed out"
```

> 📸 **Preuve à conserver** : capture d'écran horodatée + export Wireshark montrant les SYN sans
> réponse, + la ligne de journal du pare-feu qui a bloqué. Les trois ensemble constituent la preuve.

### 1.2 Test B — Le flux autorisé fonctionne quand même

Une segmentation qui casse l'exploitation ne survit pas trois jours. On prouve aussi que **ce qui
doit passer, passe**.

```bash
# Depuis la GMAO (Z3) vers le relais OPC UA de la DMZ (Z5) : doit REUSSIR
nc -zv 10.200.0.20 4840
# Resultat ATTENDU : "succeeded!"

# Depuis le SCADA (Z6) vers un automate (Z7) : doit REUSSIR
mbpoll -a 1 -t 3 -r 1 -c 5 10.220.10.15
# Resultat ATTENDU : lecture des 5 registres
```

### 1.3 Test C — La DMZ n'est pas un tremplin

```bash
# Depuis le serveur relais de la DMZ (Z5) vers un automate (Z7) : doit ECHOUER
nmap -Pn -p 502 10.220.10.15
# Resultat ATTENDU : filtered
```

> 💡 **Pourquoi ce test ?** Une DMZ mal conçue devient le point de rebond de l'attaquant : il
> compromet le relais, puis atteint l'automate. Le relais doit être **poussé** par l'OT, jamais
> autorisé à initier vers l'OT.

### 1.4 Le tableau de synthèse à remplir

| # | Test | Source | Destination | Attendu | Obtenu | Date | ✔ |
|---|---|---|---|---|---|---|---|
| A1 | Modbus bureautique → automate | Z2 | Z7 | filtered | | | |
| A2 | Balayage du /22 OT | Z2 | Z7 | 0 host up | | | |
| A3 | Écriture Modbus | Z2 | Z7 | timeout | | | |
| B1 | OPC UA métier → DMZ | Z3 | Z5 | succeeded | | | |
| B2 | Modbus SCADA → automate | Z6 | Z7 | lecture OK | | | |
| C1 | DMZ → automate | Z5 | Z7 | filtered | | | |
| D1 | Automate → Internet | Z7 | 8.8.8.8 | timeout | | | |

➡️ Script automatisant l'ensemble : [`scripts/verification/test-segmentation.sh`](scripts/verification/test-segmentation.sh)

---

## 2. Tester les sauvegardes (art. 21(2)(c))

> ⚠️ **La règle de fer** : une sauvegarde non restaurée n'est pas une sauvegarde, c'est une
> intention. Le seul test valable est une **restauration réelle**.

### 2.1 Vérifier la règle 3-2-1

| Exigence | Question à se poser | Preuve attendue |
|---|---|---|
| **3** copies | Ai-je bien 3 exemplaires de la donnée ? | Inventaire des jeux de sauvegarde |
| **2** supports différents | Disque + bande, ou disque + objet distant ? | Description technique |
| **1** copie **hors ligne / hors site** | Un rançongiciel qui a l'AD peut-il l'atteindre ? **Si oui, ce n'est pas hors ligne.** | Bande sortie du robot, ou stockage immuable |

### 2.2 Le test de restauration

```bash
# 1) Verifier l'integrite du dernier point de restauration
sha256sum -c /backup/manifests/2026-09-09.sha256

# 2) Restaurer dans un bac a sable ISOLE (jamais sur la production)
#    puis chronometrer : c'est le RTO reel, pas celui du contrat
date +%s > /tmp/t0
# ... restauration ...
echo "RTO mesure : $(( $(date +%s) - $(cat /tmp/t0) )) secondes"
```

✅ **Critère de réussite** : la configuration du SCADA et les programmes automates sont restaurés
et démarrent, en moins de 4 h (objectif de temps de reprise retenu pour HydroRégie).

📕 *Hypothèse : RTO 4 h pour le SCADA, RPO 24 h pour les données de gestion, RPO 1 h pour
l'historian. À valider par la direction (art. 20).*

---

## 3. Tester les accès distants (art. 21(2)(i) et (j))

| Test | Comment | Attendu |
|---|---|---|
| Le VPN exige le MFA | Se connecter avec seulement le mot de passe | ❌ Refus |
| L'accès intégrateur est temporaire | Vérifier le compte 24 h après la fin de l'intervention | ❌ Compte désactivé |
| La session est enregistrée | Rejouer la session depuis le bastion | ✅ Vidéo / journal disponible |
| L'accès direct hors bastion est bloqué | SSH direct vers le SCADA depuis le VPN | ❌ Refus |
| Les comptes partagés ont disparu | Chercher les comptes génériques | ✅ 0 compte générique actif |

```bash
# Lister les comptes qui ne se sont pas connectes depuis 90 jours (Linux)
lastlog -b 90

# Cote Active Directory (PowerShell) : comptes actifs jamais utilises depuis 90 jours
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly |
    Where-Object { $_.Enabled -eq $true } |
    Select-Object Name, LastLogonDate
```

---

## 4. Tester la détection (art. 21(2)(b))

On simule un comportement anormal et on vérifie que **quelqu'un le voit**.

| Scénario simulé | Ce qui doit se déclencher | Délai cible |
|---|---|---|
| Nouvelle machine inconnue apparaît sur le VLAN OT | Alerte de la sonde + ticket | < 15 min |
| Écriture Modbus depuis une IP non référencée | Alerte critique + appel de l'astreinte | < 5 min |
| 50 échecs d'authentification sur l'AD en 1 min | Alerte + blocage du compte | < 5 min |
| Suppression massive de fichiers sur le serveur | Alerte rançongiciel | < 5 min |
| Coupure de la liaison d'un réservoir | Alerte d'exploitation | Immédiat |

```bash
# Generer un echec d'authentification repetitif pour tester la detection
for i in $(seq 1 50); do
  ssh -o PreferredAuthentications=password -o StrictHostKeyChecking=no \
      testuser@10.110.0.10 exit 2>/dev/null
done
# Puis verifier cote collecteur de journaux que l'alerte est remontee
```

---

## 5. L'exercice de crise (art. 21(2)(c) et art. 23)

C'est le test le plus rentable : il coûte une demi-journée et révèle plus de failles qu'un audit.

### 5.1 Format recommandé : exercice sur table

| Élément | Recommandation |
|---|---|
| Durée | 3 h |
| Participants | DG, DSI, RSSI, responsable exploitation, communication, juridique, astreinte |
| Animateur | Une personne qui **ne joue pas** et distille les événements |
| Support | Une chronologie d'injections préparée à l'avance |
| Interdit | Prévenir les participants du scénario exact |

### 5.2 Les 5 questions auxquelles l'exercice doit répondre

1. **Qui décide** de déclencher la cellule de crise, et sur quel critère ?
2. **Comment communique-t-on** si la messagerie est indisponible ?
3. **Qui rédige** l'alerte précoce des 24 h, et qui la valide avant envoi ?
4. **À quel moment** décide-t-on de basculer l'exploitation en mode dégradé ?
5. **Qui parle aux usagers et à la presse**, et qui n'y parle surtout pas ?

### 5.3 Grille de mesure

| Indicateur | Cible | Mesuré |
|---|---|---|
| Délai détection → qualification | < 1 h | |
| Délai qualification → cellule de crise réunie | < 2 h | |
| Délai décision → alerte précoce envoyée | **< 24 h** (art. 23(4)(a)) | |
| Délai → notification complète | **< 72 h** (art. 23(4)(b)) | |
| Continuité de la distribution d'eau | **100 %** | |

➡️ Le déroulé complet de l'exercice HydroRégie : [`Documentation/job-4-crise-notifications.md`](Documentation/job-4-crise-notifications.md)

---

## 6. Le dossier de preuves

Ce qu'un contrôle (art. 32) demandera. À constituer **au fil de l'eau**, pas la veille.

```
preuves/
├── 2026-09-15_matrice-flux-validee.pdf
├── 2026-09-20_tests-segmentation.md         <- resultats + captures
├── 2026-09-22_wireshark-blocage-modbus.pcap
├── 2026-10-01_pv-comite-securite.pdf        <- art. 20 : la direction a approuve
├── 2026-10-05_restauration-scada-reussie.md <- art. 21(2)(c)
├── 2026-10-12_attestation-formation-dirigeants.pdf  <- art. 20(2)
├── 2026-11-17_exercice-de-crise-compte-rendu.pdf
└── registre-des-incidents.csv               <- art. 21(2)(b)
```

> 💡 **Astuce de terrain** : nommer les fichiers `AAAA-MM-JJ_objet.ext`. Un dossier de preuves qui
> se trie tout seul par date, c'est déjà un demi-point gagné devant un auditeur.

---

## ✅ Vérification de fin de fiche

- [ ] Quelle est la différence entre un port `filtered` et un port `closed` dans un test de segmentation ?
- [ ] Pourquoi teste-t-on aussi les flux **autorisés** ?
- [ ] Que vaut une sauvegarde jamais restaurée ?
- [ ] Quel article impose d'évaluer l'efficacité des mesures ?

---

⬅️ [03 — Mise en conformité](03_mise_en_conformite.md) · ➡️ **Suite** : [05 — Annexes](05_annexes.md)
