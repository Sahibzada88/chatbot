import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def call_open_ai(message):
    client = OpenAI()
    response = client.chat.completions.create(
        temperature = 0,
        model = "gpt-4o-mini",
        messages = message,
        
    )
    return response.choices[0].message.content
