from openai import OpenAI

# Initialize the OpenAI client to point to Ollama's API
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama's default local endpoint
    api_key="ollama"  # Dummy key, required but not used by Ollama
)

completion = client.chat.completions.create(
    messages=[],
    model="llama3.2:3b",
)