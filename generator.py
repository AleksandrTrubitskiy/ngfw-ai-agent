import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(task_type, level, description):
    return f"""
Ты — AI-агент, работающий над NGFW-платформой ultra-os-ngfw.
Тип задачи: {task_type}
Уровень сложности: {level}
Описание задачи: {description}

Сгенерируй Java-код, соответствующий задаче. Если требуется — создай несколько классов, интерфейсы, тесты, и предложи изменения в архитектуре. Структурируй код так, чтобы он был готов к интеграции в прод.
"""

def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
