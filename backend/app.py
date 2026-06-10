
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# Maak de Flask-app en vertel waar de front-end bestanden staan.
app = Flask(
    __name__, static_folder=os.path.join(os.path.dirname(__file__), "../frontend")
)
CORS(app)

# Dit zijn de trainingsdoelen die we laten zien.
training_goals = [
    {
        "title": "Condition verbeteren",
        "description": "Ik wil mijn uithoudingsvermogen opbouwen met vaste training en slimme rustmomenten.",
        "status": "In progress",
    },
    {
        "title": "Calisthenics skills leren",
        "description": "Ik wil sterker worden in push-ups, pull-ups, dips en core-oefeningen.",
        "status": "In progress",
    },
    {
        "title": "Voeding en herstel volgen",
        "description": "Ik wil beter letten op voeding, slaap en herstel na trainingen.",
        "status": "Not started",
    },
    {
        "title": "Git en GitHub gebruiken",
        "description": "Ik wil commits, branches en versiebeheer goed gebruiken voor dit project.",
        "status": "In progress",
    },
]

# Dit zijn de workouts die we bewaren. Wanneer iemand een workout toevoegt, komt die hier.
workouts = [
    {
        "week": 1,
        "topic": "Upper body basis",
        "reflection": "Ik heb gewerkt aan push-ups en rustige techniek om sterker te worden.",
    },
    {
        "week": 2,
        "topic": "Core training",
        "reflection": "Ik heb core-oefeningen gedaan zoals plank, hollow hold en leg raises.",
    },
    {
        "week": 3,
        "topic": "Pull training",
        "reflection": "Ik heb pull-up progressies en rows geoefend om mijn rug sterker te maken.",
    },
]


@app.get("/")
def home():
    # Voor iemand zonder technische kennis:
    # Als je de server opent in een browser, laat deze route de startpagina van de website zien.
    # Het laadt het bestand `frontend/index.html`.
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/goals")
def get_goals():
    # Geeft een lijst met trainingsdoelen terug in simpel tekstformaat (JSON).
    # In gewone woorden: "Hier zijn de doelen die de gebruiker heeft opgegeven."
    return jsonify(training_goals)


@app.get("/api/workouts")
def get_workouts():
    # Geeft de opgeslagen workouts terug.
    # Een workout bevat: week, onderwerp en een korte notitie (reflection).
    return jsonify(workouts)


@app.post("/api/workouts")
def add_workout_item():
    # Voeg een nieuwe workout toe.
    # Verwachte data (vanuit de website): { week: number, topic: string, reflection: string }
    # In gewone taal: de gebruiker vult een formulier in en die informatie komt hier terecht.
    # Lees wat de website stuurt.
    data = request.get_json(silent=True) or {}
    week = data.get("week")
    topic = str(data.get("topic", "")).strip()
    reflection = str(data.get("reflection", "")).strip()

    # Controleer of de ingevulde gegevens logisch zijn.
    if not isinstance(week, int) or week <= 0:
        return jsonify({"error": "Week must be a positive number."}), 400
    if not topic or not reflection:
        return jsonify({"error": "Topic and reflection are required."}), 400

    # Sla de nieuwe workout op in het tijdelijke geheugen van deze server (lijsten).
    # Let op: dit wacht alleen in het geheugen van deze draaiende server en wordt niet bewaard als
    # de server stopt. Voor schoolopdracht is dit vaak voldoende.
    new_item = {
        "week": week,
        "topic": topic,
        "reflection": reflection,
    }
    workouts.append(new_item)
    return jsonify(new_item), 201


@app.get("/api/progress")
def get_progress():
    # Bereken een kleine samenvatting van de voortgang.
    # Deze informatie wordt bovenaan de pagina getoond als simpele cijfers.
    total_goals = len(training_goals)
    completed_goals = sum(1 for goal in training_goals if goal["status"] == "Done")
    in_progress_goals = sum(
        1 for goal in training_goals if goal["status"] == "In progress"
    )

    # Stuur deze getallen naar de website.
    return jsonify(
        {
            "totalGoals": total_goals,
            "completedGoals": completed_goals,
            "inProgressGoals": in_progress_goals,
            "workoutEntries": len(workouts),
            "summary": "Dit project laat een eenvoudige full-stack gym en calisthenics tracker zien.",
        }
    )


@app.route("/<path:path>")
def serve_static(path):
    # Serve alle statische bestanden
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    # Start de server.
    app.run(debug=True, port=5001)
