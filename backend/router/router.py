import json
from typing import List

import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    q_sentence: str

class Answer(BaseModel):
    answer_sentence: str
    similar_precedent: List


# @app.get("/model_api", response_class=HTMLResponse)
# def docs():
#     url = "http://127.0.0.1:8000/docs"
#     res = requests.get(url)

#     # print(res)
#     return HTMLResponse(content=res.text, status_code=200)

@app.post("/generate", response_model=Answer)
async def generate(question: Question):
    q_sentence = question.q_sentence
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    url = "http://127.0.0.1:8000/generate"
    data = {"q_sentence": q_sentence}
    print(data)

    res = requests.post(url, headers=headers, data=json.dumps(data))
    
    return res.json()
