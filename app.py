import os
import json
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Get the absolute path to the Flask app's root directory
app_root = os.path.abspath(os.path.dirname(__file__))

# Specify the path to the slogans.json file using the app_root
slogans_file_path = os.path.join(app_root, "slogans.json")

candidates = {
    "Noushad": 0,
    "Sahana": 0,
}

# Load slogans from JSON file
with open(slogans_file_path, "r") as f:
    slogans = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "voted" not in session:
            candidate = request.form["candidate"]
            if candidate in candidates:
                candidates[candidate] += 1
                session["voted"] = True
        return redirect(url_for("results"))
    return render_template("index.html", slogans=slogans)

@app.route("/results")
def results():
    return render_template("results.html", candidates=candidates)

if __name__ == "__main__":
    app.run()
