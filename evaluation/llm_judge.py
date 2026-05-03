from groq import Groq
import os
from evaluation.judge_prompt import JUDGE_PROMPT

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def judge_response(question, answer, context):
    
    prompt = f"""
    {JUDGE_PROMPT}

    Context:
    {context}

    User Question:
    {question}

    Model Answer:
    {answer}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content