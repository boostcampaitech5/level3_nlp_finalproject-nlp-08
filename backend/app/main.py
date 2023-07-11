import os

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from generate import generate_answer


class Question(BaseModel):
    q_sentence: str

app = FastAPI()

model = None
tokenizer = None

@app.on_event("startup")
def startup_event():
    global tokenizer, model
    model_id = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "model")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map={"":0})

@app.post("/generate")
async def generate(question: Question):
    return generate_answer(question.q_sentence, model, tokenizer)
