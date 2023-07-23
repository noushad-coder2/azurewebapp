import json
from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

candidates = {
    "Noushad": 0,
    "Sahana": 0,
}

# Load slogans from JSON file
with open("slogans.json", "r") as f:
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
    return render_template("index.html", candidates=candidates, slogans=slogans)

@app.route("/results")
def results():
    return render_template("results.html", candidates=candidates)

if __name__ == "__main__":
    app.run()
