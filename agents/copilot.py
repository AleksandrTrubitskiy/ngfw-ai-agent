from agents.base import BaseAgent

class CopilotAgent(BaseAgent):
    def generate(self, prompt: str) -> str:
        return "// Copilot работает в IDE. Генерация недоступна через API."
