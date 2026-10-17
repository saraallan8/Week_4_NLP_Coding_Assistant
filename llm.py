import os 
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    timeout=40.0,
)

Model = os.getenv("OPENROUTER_MODEL", "cohere/north-mini-code:free")


def ask_llm(prompt, history=None):
    messages = []

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=Model,
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content
