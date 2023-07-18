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
    answer_sentence: str
    similar_precedent: List


# @app.get("/model_api", response_class=HTMLResponse)
# def docs():
#     url = "http://127.0.0.1:8000/docs"
#     res = requests.get(url)

#     # print(res)
#     return HTMLResponse(content=res.text, status_code=200)

@app.post("/generate", response_model=Union[Answer, None])
async def generate(question: Question):
    KST = pytz.timezone('Asia/Seoul')
    print(datetime.today(KST).strftime("%Y/%m/%d %H:%M:%S"))
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
