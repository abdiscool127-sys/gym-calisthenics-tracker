from flask import Flask, jsonify, request
from flask_cors import CORS

# Dit is de server. De server geeft antwoord als de website om informatie vraagt.
app = Flask(__name__)
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
    # Dit is de startpagina. Hier zie je wat de server doet.
    return jsonify(
        {
            "name": "Gym en Calisthenics Tracker API",
            "message": "Gebruik /api/goals, /api/workouts en /api/progress.",
        }
    )


@app.get("/api/goals")
def get_goals():
    # Gaat alle doelen naar de website.
    return jsonify(training_goals)


@app.get("/api/workouts")
def get_workouts():
    # Geeft alle workouts naar de website.
    return jsonify(workouts)


@app.post("/api/workouts")
def add_workout_item():
    # Lees wat de website stuurt.
    data = request.get_json(silent=True) or {}
    week = data.get("week")
    topic = str(data.get("topic", "")).strip()
    reflection = str(data.get("reflection", "")).strip()

    # Controleer of alles ingevuld is.
    if not isinstance(week, int) or week <= 0:
        return jsonify({"error": "Week must be a positive number."}), 400
    if not topic or not reflection:
        return jsonify({"error": "Topic and reflection are required."}), 400

    # Sla de workout op en geef het terug.
    new_item = {
        "week": week,
        "topic": topic,
        "reflection": reflection,
    }
    workouts.append(new_item)
    return jsonify(new_item), 201


@app.get("/api/progress")
def get_progress():
    # Tel hoeveel doelen en workouts we hebben.
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


if __name__ == "__main__":
    # Start de server.
    app.run(debug=True)
