# Gym en Calisthenics Tracker

- Dit project bestaat uit twee delen:
  - De website die je ziet (frontend) — bestanden in de map `frontend`.
  - De kleine server die data geeft (backend) — bestanden in de map `backend`.

## Snel starten (stap-voor-stap)

1) Server (backend) starten:

```powershell
cd backend
pip install -r requirements.txt
python app.py
python -m flask run --port=5001
```

De server draait daarna op `http://127.0.0.1:5001`.

2) Website (frontend) openen:

- Open `frontend/index.html` direct in je browser óf bezoek `http://127.0.0.1:5001` nadat de server draait.

3) Wat je ziet:
- Bovenaan: simpele cijfers (aantal doelen, actieve doelen, aantal workouts).
- Linkerkant: lijst met trainingsdoelen.
- Rechts: formulier om een nieuwe workout toe te voegen.
- Onderaan: een timeline met alle ingevoerde workouts.

## Belangrijke bestanden (kort uitgelegd)
- `backend/app.py`: de server - geeft data aan de website.
- `backend/requirements.txt`: welke Python-pakketten nodig zijn (Flask e.d.).
- `frontend/index.html`: de webpagina.
- `frontend/app.js`: de JavaScript die de pagina laat werken (haalt data op en toont het).
- `frontend/style.css`: hoe de pagina eruitziet.

## API (in eenvoudige woorden)
- `GET /api/goals` — geeft een lijst met doelen terug.
- `GET /api/workouts` — geeft alle workouts terug.
- `POST /api/workouts` — voeg een nieuwe workout toe (wordt door het formulier gebruikt).
- `GET /api/progress` — geeft een paar getallen terug over voortgang.

## Tips voor presenteren
- Vertel stap voor stap: eerst de website, dan de server, dan hoe je iets toevoegt.
- Maak screenshots van de werkende website en van de GitHub-pagina.

## Extra
Zie [UITLEG-TALEN.md](UITLEG-TALEN.md) voor een korte, niet-technische uitleg van de gebruikte talen.
