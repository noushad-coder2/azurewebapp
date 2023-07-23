import json
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['STATIC_FOLDER'] = 'static'  # Configuring the static folder

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
    return render_template("index.html", slogans=slogans)

@app.route("/results")
def results():
    return render_template("results.html", candidates=candidates)

# Route to serve static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    return send_from_directory(os.path.join(root_dir, app.config['STATIC_FOLDER']), filename)

if __name__ == "__main__":
    app.run()
