from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
import json

load_dotenv()
client = Anthropic()

def load_logs(path: Path) -> str:
    with open(path, "r") as f:
        data = json.load(f)
    return json.dumps(data, indent=2)

history = []

def chat(message: str, logs: str):
    history.append({"role": "user", "content": message})
    with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=256,
            system=f"""
                   You are an AI cost advisor.
                   You help users understand their LLM spending and choose the right model for each task.
                   Here are the user's API call logs: {logs}
                   """,
            messages=history
    ) as stream:
        print("Claude: ", end="", flush=True)
        for text in stream.text_stream:
            print(text, end="", flush=True)
        print()
        reply = stream.get_final_text()
    history.append({"role": "assistant", "content": reply})

system_logs = load_logs("../project_1_api_logger/calls.json")

while True:
    command = input(">> ").strip().lower()
    if command == "quit":
        print("Goodbye!")
        break
    chat(command, system_logs)
