from flask import Flask, render_template, request
from core.manager import get_active_agent
from core.prompt import build_prompt
from core.renderer import render_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    if request.method == "POST":
        task_type = request.form["task_type"]
        level = request.form["level"]
        description = request.form["description"]

        prompt = build_prompt(task_type, level, description)
        agent = get_active_agent()
        code = agent.generate(prompt)

    return render_template("index.html", code=render_code(code))
