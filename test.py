import json
import requests
from ollama import Client

# -------------------------
# Web Agent Framework
# -------------------------

class WebAgent:
    def __init__(self, model="llama3", host="http://localhost:11434"):
        self.client = Client(host=host)
        self.model = model

    # --- Tool function ---
    def open_url(self, url: str):
        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            return res.text[:15000]  # limit to avoid overflow
        except Exception as e:
            return f"Error: {e}"

    # --- Main query ---
    def ask(self, prompt: str):
        # Tell LLM how tools work
        system_prompt = """
You are a web-browsing agent. 
If the user asks to open or read a URL, respond ONLY with:
{"tool": "open_url", "url": "<the url>"}
Otherwise answer normally.
"""

        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        message = response["message"]["content"]

        # Check if it is a tool-call JSON
        try:
            data = json.loads(message)
            if data.get("tool") == "open_url":
                result = self.open_url(data["url"])

                # send page content back for reasoning
                follow = self.client.chat(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You read webpage content and summarize it."},
                        {"role": "assistant", "content": message},
                        {"role": "tool", "content": result},
                    ]
                )
                return follow["message"]["content"]

        except Exception:
            pass  # not a tool call

        return message


# -------------------------------------
# Example Usage
# -------------------------------------

if __name__ == "__main__":
    agent = WebAgent(model="llama3")   # <--- change to qwen, mistral, etc.

    out = agent.ask("Open https://example.com and summarize it.")
    print(out)
