from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))