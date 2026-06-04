# Git en GitHub - Stap voor stap

Dit bestand laat zien hoe je dit project op GitHub zet zodat je docent ziet wat je hebt gedaan.

## Wat doen Git en GitHub?
- **Git** bewaart je wijzigingen op je computer.
- **GitHub** laat je project online zien.

Zo kan je docent zien hoe je hebt gewerkt, stap voor stap.

---

## Stap 1: GitHub account maken

1. Ga naar https://github.com
2. Klik op "Sign up"
3. Vul je e-mail in
4. Maak een wachtwoord
5. Kies een gebruikersnaam (bijv. `abdimohamednl` of je naam)
6. Vul het puzzeltje in
7. Klik op "Create account"

**Je krijgt nu een account. Onthoud je gebruikersnaam!**

---

## Stap 2: Git installeren op je computer

1. Ga naar https://git-scm.com/download/win
2. Download het programma (klik op de grote groene knop)
3. Open het gedownloade bestand
4. Klik steeds "Next" tot je "Install" ziet
5. Klik "Install"
6. Klik "Finish"

**Git is nu geïnstalleerd.**

---

## Stap 3: PowerShell openen in je projectmap

1. Open je projectmap (de map `keuzedeel`)
2. Klik in de adresbalk bovenaan en maak hem leeg
3. Typ: `powershell`
4. Druk op Enter

**PowerShell opent nu in deze map.**

---

## Stap 4: Git configureren (eenmalig)

Voer dit in PowerShell uit (vervang de namen):

```bash
git config --global user.name "Jouw Volledige Naam"
git config --global user.email "jouw@email.com"
```

Voorbeeld:
```bash
git config --global user.name "Abdi Mohamed"
git config --global user.email "abdi@example.com"
```

**Druk op Enter na elke regel.**

---

## Stap 5: Git lokaal starten

Voer dit uit in PowerShell:

```bash
git init
```

Dit maakt Git klaar in deze map.

---

## Stap 6: Alles toevoegen aan Git

Voer dit uit:

```bash
git add .
```

Dit zegt tegen Git: "Sla alles op wat in deze map staat."

---

## Stap 7: Je eerste commit maken

Voer dit uit:

```bash
git commit -m "Initial project structure"
```

Dit geeft een naam aan wat je hebt opgeslagen. Later zie je dit als een stap op GitHub.

**Meldingen:**
- `git config` - hoeft niet uit te voeren als je het al gedaan hebt
- `git init` - hoeft niet uit te voeren als je het al gedaan hebt

---

## Stap 8: Nieuwe repository op GitHub maken

1. Log in op GitHub (met je account dat je zojuist hebt gemaakt)
2. Klik rechtsboven op "+" 
3. Klik op "New repository"
4. Vul in:
   - **Repository name**: `gym-calisthenics-tracker`
   - **Description**: `Een gym tracker met JavaScript, Vue, Python en Flask`
   - **Public**: Zet dit aan (vink het aan)
5. Klik "Create repository"

**Je repository is nu gemaakt op GitHub.**

---

## Stap 9: Je code uploaden naar GitHub

GitHub laat nu een apart scherm zien. Kopieer de commando's die daar staan.

Meestal ziet het er zo uit:

```bash
git branch -M main
git remote add origin https://github.com/JOUWNAAM/gym-calisthenics-tracker.git
git push -u origin main
```

(Vervang `JOUWNAAM` met jouw GitHub-gebruikersnaam)

Voer deze twee regels achtereenvolgens in PowerShell uit:

1. Voer in:
```bash
git branch -M main
```

2. Voer in (met jouw gebruikersnaam):
```bash
git remote add origin https://github.com/JOUWNAAM/gym-calisthenics-tracker.git
```

3. Voer in:
```bash
git push -u origin main
```

Dit vraagt om je GitHub-gebruikersnaam en wachtwoord. Vul die in.

**Je code staat nu op GitHub!**

---

## Stap 10: Controleer of alles klopt

1. Ga naar GitHub in je browser
2. Ga naar je repository: `github.com/JOUWNAAM/gym-calisthenics-tracker`
3. Je ziet nu al je bestanden staan!

---

## Later: Meer commits maken

Als je later iets verandert en dat wilt opslaan, doe je dit:

```bash
git add .
git commit -m "Add Flask API"
git push
```

Voorbeelden van goede commitberichten die je nu kunt gebruiken:
- "Voeg Flask API toe"
- "Maak frontend met Vue"
- "Verbeter styling van de pagina"
- "Pas comments aan"
- "Voeg README toe"
- "Koppel frontend aan backend"

Zo schrijf je ze:
- Begin met een werkwoord
- Schrijf kort en duidelijk wat je hebt gedaan
- Gebruik Engels of Nederlands, maar blijf consistent

---

## Wat ziet je docent?

Je docent gaat naar `github.com/JOUWNAAM/gym-calisthenics-tracker` en ziet:
- Al je bestanden
- Al je commits (stappen)
- Hoe lang je eraan gewerkt hebt
- Dat je structureel hebt gewerkt

Dit is heel goed bewijs dat je IT-vaardigheden hebt!

---

## Snelle checklist

- [ ] GitHub account gemaakt
- [ ] Git geïnstalleerd
- [ ] Git geïnstalleerd op je computer geverifieerd
- [ ] `git init` gedaan in je projectmap
- [ ] `git config` ingesteld met je naam en e-mail
- [ ] `git add .` gedaan
- [ ] `git commit -m "Initial project structure"` gedaan
- [ ] Repository op GitHub gemaakt (public)
- [ ] `git remote add origin...` gedaan
- [ ] `git push -u origin main` gedaan
- [ ] Code staat nu online op GitHub

---

## Problemen?

**Git commando's geven fout:**
- Zorg dat je in PowerShell bent in de map `keuzedeel`
- Zorg dat je Git hebt geïnstalleerd

**Kan niet uploaden:**
- Zorg dat je GitHub-account klopt
- Zorg dat de repository public is (niet private)

**Weet niet meer wat mijn commit was:**
- Voer in: `git log`
- Dit toont al je commits!
