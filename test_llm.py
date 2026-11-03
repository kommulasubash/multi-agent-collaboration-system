
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

response = llm.call(
    [{"role": "user", "content": "Explain MCP in two sentences."}]
)

print("\nLLM Response:")
print(response)
