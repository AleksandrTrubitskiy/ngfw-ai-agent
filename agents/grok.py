import requests
import os

class GrokAgent(BaseAgent):
    def __init__(self):
        self.endpoint = os.getenv("GROK_ENDPOINT")
        self.api_key = os.getenv("GROK_API_KEY")

    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt}
        )
        return response.json().get("text", "")
