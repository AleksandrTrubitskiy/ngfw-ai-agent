from flask import Flask, render_template, request
from generator import build_prompt, generate_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    if request.method == "POST":
        task_type = request.form["task_type"]
        level = request.form["level"]
        description = request.form["description"]

        prompt = build_prompt(task_type, level, description)
        code = generate_code(prompt)

    return render_template("index.html", code=code)
