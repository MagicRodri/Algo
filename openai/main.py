import os

from dotenv import load_dotenv

import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="davinci",
    prompt="Correct this to standard English:\n\nShe no went to the market.",
    temperature=0.9,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
print(response)