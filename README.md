# gym-calisthenics-tracker
Een gym tracker met JavaScript, Vue, Python en Flask
# Gym en Calisthenics Tracker

Een klein project voor je opdracht. Dit project toont hoe een website en een server samenwerken.

## Wat doet het?
De applicatie helpt je trainingsdoelen en workouts bij te houden. Je kunt doelen zien, nieuwe workouts toevoegen en alles terugzien.

## Wat wordt gebruikt?
- **JavaScript** om de pagina interactief te maken.
- **Vue.js** om de pagina netjes op te bouwen.
- **Python en Flask** om de server en data te regelen.
- **Git/GitHub** om je werk op te slaan en te tonen.

## Projectstructuur
```text
keuzedeel/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/a
│   ├── index.html
│   ├── app.js
│   └── style.css
└── README.md
```

## Starten van de backend
1. Ga naar de map `backend`.
2. Installeer de pakketten:
   ```bash
   pip install -r requirements.txt
   ```
3. Start de server:
   ```bash
   python app.py
   ```
4. De API draait standaard op `http://127.0.0.1:5000`.

## Starten van de frontend
Open `frontend/index.html` in je browser.

## Hoe werkt het?
1. Je opent de pagina.
2. De pagina vraagt data van de server.
3. De server stuurt de data terug.
4. De pagina laat alles zien.

## API-endpoints
- `GET /api/goals` geeft de trainingsdoelen terug.
- `GET /api/workouts` geeft de workouts terug.
- `POST /api/workouts` voegt een nieuwe workout toe.
- `GET /api/progress` geeft een korte samenvatting van de voortgang.

## Git/GitHub
Voor je bewijs kun je in GitHub commits tonen zoals:
- `Initial project structure`
- `Add Flask API`
- `Build Vue frontend`
- `Improve styling and documentation`

## Extra uitleg
Als je wilt laten zien wat de talen doen, open dan [UITLEG-TALEN.md](UITLEG-TALEN.md).

## Wat kun je zeggen?
- Dit is de voorkant (wat je ziet).
- Dit is de achterkant (de server).
- Dit is hoe ik het heb bijgehouden (Git/GitHub).

## Tip voor inleveren
Maak voordat je inlevert screenshots van:
- de werkende frontend;
- de API in de browser of via Postman;
- je GitHub repository met commits.
