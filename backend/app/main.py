import os
from datetime import datetime
from typing import List, Union

import numpy as np
import pandas as pd
import pytz
import torch
from fastapi import FastAPI
from peft import PeftConfig, PeftModel
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer

from bert_retrieval import Autodata, bert_retrieve_QA
from bm25_retrieval import retrieve_QA
from filter import is_legal_question
from generate import generate_answer
from search import Precedent, load_vector_data, search_precedent


class Question(BaseModel):
    q_sentence: str

class Answer(BaseModel):
    answer_sentence: Union[str, None]
    similar_precedent: Union[List[Precedent], None]

os.environ["TOKENIZERS_PARALLELISM"] = "false"
app = FastAPI()

llm = None
tokenizer = None
search_model =  None
retrieve_model = None
retrieve_data = None
retrieve_vector_data = None
text_data = None
vector_data = None

@app.on_event("startup")
def startup_event():
    global tokenizer, llm, search_model, retrieve_model, retrieve_data, retrieve_vector_data, text_data, vector_data

    print("Load LLM")
    model_id = "kfkas/Legal-Llama-2-ko-7b-Chat"
    # config = PeftConfig.from_pretrained(peft_model_id)
    llm = AutoModelForCausalLM.from_pretrained(
        model_id, device_map={"": 0}, torch_dtype=torch.float16
    )
    # llm = PeftModel.from_pretrained(llm, peft_model_id, torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    print("Load search model")
    search_model = SentenceTransformer("jhgan/ko-sroberta-multitask")

    print("Load retrieve model and data")
    retrieve_model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "data/bert_retrieval_data")
    retrieve_data = Autodata(DATA_DIR)
    retrieve_vector_data = retrieve_data.load_vector_data(os.path.join(DATA_DIR, "query_vector.bin"))

    print("Load data")
    base_path = os.path.abspath(os.path.dirname(__file__))

    text_data = np.array(pd.read_csv(base_path + "/../data/law_data/law_data_drop.csv"))
    vector_data = load_vector_data(
        base_path + "/../data/law_data/law_data_drop_vector.bin"
    )


@app.post("/generate", response_model=Answer)
async def generate(question: Question):
    KST = pytz.timezone('Asia/Seoul')
    print(datetime.now(KST).strftime("%Y/%m/%d %H:%M:%S"))

    q_sentence = question.q_sentence
    print(f"q_sentence: {q_sentence}")

    if not is_legal_question(q_sentence=q_sentence):
        return Answer(answer_sentence=None, similar_precedent=None)

    # retrieve_answer = retrieve_QA(q_sentence=q_sentence)
    retrieve_answer = bert_retrieve_QA(q_sentence=q_sentence, model=retrieve_model, data=retrieve_data, vector_data=retrieve_vector_data)

    answer_sentence = generate_answer(q_sentence=q_sentence, model=llm, tokenizer=tokenizer)

    similar_precedent = search_precedent(q_a_sentence=q_sentence+retrieve_answer+answer_sentence, model=search_model, text_data=text_data, vector_data=vector_data)

    return Answer(answer_sentence=answer_sentence, similar_precedent=similar_precedent)
