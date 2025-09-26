from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def format_prompt(level, task):
    return f"""
Ты — AI-агент NGFW. Уровень сложности: {level}.
Сгенерируй Java-класс, который выполняет задачу:
{task}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    if request.method == "POST":
        task = request.form["task"]
        level = request.form["level"]
        prompt = format_prompt(level, task)

        response = openai.ChatCompletion.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}]
        )
        code = response['choices'][0]['message']['content']
    return render_template("index.html", code=code)
