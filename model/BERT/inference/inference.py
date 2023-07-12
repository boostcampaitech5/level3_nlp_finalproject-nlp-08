import os

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from .utils import load_vector_data


def BERT_infer(input):
    model_name = "jhgan/ko-sroberta-multitask"
    model = SentenceTransformer(model_name)
    model.to("cuda:0")

    input_vector = model.encode(input)
    input_vecotr = np.expand_dims(input_vector, axis=0)

    base_path = os.path.join(os.path.dirname(__file__))

    text_data = np.array(pd.read_csv(base_path + "/../data/law_data/law_data_drop.csv"))
    vector_data = load_vector_data(
        base_path + "/../data/law_data/law_data_drop_vector.bin"
    )

    cos_sim = cosine_similarity(input_vecotr, vector_data)
    data_cosine = np.sort(cos_sim).squeeze()[::-1][:3]
    top_question = np.argsort(cos_sim).squeeze()[::-1][:3]

    pan_list = []

    for i, index in enumerate(top_question):
        if data_cosine[i] >= 0.5:
            pan_list.append(
                f"case Number : {text_data[index][0]} judgementAbstract : {text_data[index][4]} judgementNote :{text_data[index][9]}"
            )

    return pan_list


if __name__ == "__main__":
    BERT_infer("상원이형과 이혼을 하는것은 중죄이고 죄질이 나쁘기 떄문에 징역 10년입니다.")
