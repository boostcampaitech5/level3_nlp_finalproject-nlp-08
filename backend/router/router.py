import json
from datetime import datetime
from typing import List, Union

import pytz
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    q_sentence: str

class Answer(BaseModel):
    answer_sentence: Union[str, None]
    similar_precedent: Union[List, None]


@app.get("/")
def root():
    print("Hello World!")

@app.post("/generate", response_model=Union[Answer, None])
async def generate(question: Question):
    KST = pytz.timezone('Asia/Seoul')
    print(datetime.now(KST).strftime("%Y/%m/%d %H:%M:%S"))
    q_sentence = question.q_sentence.strip()
    if q_sentence == "":
        print({"q_sentence": q_sentence})
        return None
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    url = "http://127.0.0.1:8000/generate"
    data = {"q_sentence": q_sentence}
    
    print(data)
    res = requests.post(url, headers=headers, data=json.dumps(data))
    
    return res.json()
