import os
import pickle
import time

import numpy as np
import torch
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Precedent(BaseModel):
    case_name: str
    case_number: str
    case_type: str
    ref_article: str
    url: str


def search_precedent(q_a_sentence: str, model, text_data, vector_data):
    start_time = time.time()
    # model = SentenceTransformer("jhgan/ko-sroberta-multitask") #TODO
    model.to("cuda:0")

    input_vector = model.encode(q_a_sentence)
    input_vecotr = np.expand_dims(input_vector, axis=0)

    cos_sim = cosine_similarity(input_vecotr, vector_data)
    data_cosine = np.sort(cos_sim).squeeze()[::-1][:3]
    top_question = np.argsort(cos_sim).squeeze()[::-1][:3]

    precedent_list = []

    for i, index in enumerate(top_question):
        if data_cosine[i] >= 0.5:
            ref_article = text_data[index][7]
            ref_article_split = str(ref_article).split()
            if len(ref_article_split) >= 2:
                url = f"https://law.go.kr/법령/{ref_article_split[0]}/{ref_article_split[1]}"
            else:
                url = ""
            precedent_list.append(
                Precedent(case_name=text_data[index][3], case_number=text_data[index][0], case_type=text_data[index][6], ref_article=ref_article, url=url)
            )

    # del model
    # torch.cuda.empty_cache()

    print(f"search time: {time.time() - start_time}")

    return precedent_list

def load_vector_data(path):
    if os.path.isfile(path):
        with open(path, "rb") as fr:
            vector_data = pickle.load(fr)
    else:
        print("판례 데이터가 존재하지 않습니다.")
        vector_data = None
    return vector_data
