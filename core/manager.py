import os
from agents.chatgpt import ChatGPTAgent
from agents.grok import GrokAgent
from agents.copilot import CopilotAgent

def get_active_agent():
    agent = os.getenv("ACTIVE_AGENT", "chatgpt")
    if agent == "chatgpt":
        return ChatGPTAgent()
    elif agent == "grok":
        return GrokAgent()
    elif agent == "copilot":
        return CopilotAgent()
    else:
        raise ValueError("Unknown agent")
