from fastapi import FastAPI
from pydantic import BaseModel

from generate import generate_answer


class Question(BaseModel):
    q_sentence: str

app = FastAPI()

@app.post("/generate")
async def generate(question: Question):
    return generate_answer(question.q_sentence)
