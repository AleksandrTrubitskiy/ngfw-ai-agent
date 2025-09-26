class BaseAgent:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Must implement generate()")
