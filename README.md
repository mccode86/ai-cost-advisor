AI Cost Advisor

Interactive CLI chatbot that analyzes your LLM API call logs and advises on model
selection and spending.

What it does

- Loads your API call logs from a JSON file
- Uses Claude as an AI cost advisor with your log data as context
- Maintains conversation history so you can ask follow-up questions
- Streams responses in real-time

Requirements

- Python 3.9+
- Anthropic API key

Setup

pip install anthropic python-dotenv

Create a .env file:

ANTHROPIC_API_KEY=your_key_here

Usage

python main.py

Type your question and press Enter. Type quit to exit.

Log format

The advisor expects a calls.json file with this structure:

[
{
"call_id": "abc-001",
"model": "claude-sonnet-4-6",
"input_tokens": 500,
"output_tokens": 1200,
"cost_usd": 0.05,
"latency_ms": 1800,
"prompt_excerpt": "...",
"response_excerpt": "...",
"tags": ["production"],
"timestamp": "2026-05-31T01:48:48"
}
]

Example questions

- "Which model did I use the most?"
- "What was my most expensive API call?"
- "How much did I spend in total?"
- "Which model should I use for summarization tasks?"