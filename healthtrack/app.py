from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simulated in-memory data (replaces MongoDB)
def get_today_data():
    return {
        "username": "Faizan",
        "today": datetime.now().strftime("%A, %B %d, %Y"),
        "water_intake": 2.5,
        "habits_done": 3,
        "total_habits": 5,
        "stress_level": "Low",
        "habits": [
            {"emoji": "☀️", "name": "Morning Walk", "desc": "30 mins • Outdoors", "completed": True},
            {"emoji": "💧", "name": "Hydration", "desc": "2.5L target", "completed": False},
            {"emoji": "🧘", "name": "Meditation", "desc": "10 mins • Calm app", "completed": True}
        ],
        "stress_chart": [3, 2, 4, 1, 2, 3, 2]
    }

@app.route("/")
@app.route("/dashboard")
def dashboard():
    data = get_today_data()
    return render_template("dashboard.html",
                           username=data["username"],
                           today=data["today"],
                           water_intake=data["water_intake"],
                           habits_done=data["habits_done"],
                           total_habits=data["total_habits"],
                           stress_level=data["stress_level"],
                           chart_data=data["stress_chart"],
                           habits=data["habits"])

@app.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        # Future logic to save log
        return redirect(url_for('dashboard'))
    return "<h2>Habit Logging Form Coming Soon!</h2>"

if __name__ == "__main__":
    app.run(debug=True)