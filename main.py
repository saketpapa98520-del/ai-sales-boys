from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    user_message: str

SYSTEM_PROMPT = """
You are an Indian AI sales executive.
Speak in Hinglish.
Be friendly, persuasive, and practical.
Your job is to close the sale or book a call.
"""

@app.post("/chat")
def chat(msg: Message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg.user_message}
        ]
    )
    return {"reply": response.choices[0].message.content}
