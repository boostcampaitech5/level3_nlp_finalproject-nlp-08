import os
from typing import List

import numpy as np
import pandas as pd
from fastapi import FastAPI
from peft import PeftConfig, PeftModel
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer

from generate import generate_answer
from search import Precedent, load_vector_data, search_precedent


class Question(BaseModel):
    q_sentence: str

class Answer(BaseModel):
    answer_sentence: str
    similar_precedent: List[Precedent]


app = FastAPI()

llm = None
tokenizer = None
search_model =  None
text_data = None
vector_data = None

@app.on_event("startup")
def startup_event():
    global tokenizer, llm, search_model, text_data, vector_data

    print("Load LLM")
    peft_model_id = "kfkas/LawBot-level1"
    config = PeftConfig.from_pretrained(peft_model_id)
    llm = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path, device_map={"": 0}
    )
    llm = PeftModel.from_pretrained(llm, peft_model_id)
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

    print("Load search model")
    # search_model = SentenceTransformer("jhgan/ko-sroberta-multitask")

    print("Load data")
    base_path = os.path.abspath(os.path.dirname(__file__))

    text_data = np.array(pd.read_csv(base_path + "/../data/law_data/law_data.csv"))
    vector_data = load_vector_data(
        base_path + "/../data/law_data/law_data_drop_vector.bin"
    )


@app.post("/generate", response_model=Answer)
async def generate(question: Question):
    q_sentence = question.q_sentence
    answer_sentence = generate_answer(q_sentence=q_sentence, model=llm, tokenizer=tokenizer)
    similar_precedent = search_precedent(q_a_sentence=q_sentence+answer_sentence, model=search_model, text_data=text_data, vector_data=vector_data)
    return Answer(answer_sentence=answer_sentence, similar_precedent=similar_precedent)
