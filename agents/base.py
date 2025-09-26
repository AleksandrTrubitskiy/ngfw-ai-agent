class BaseAgent:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Agent must implement generate()")
