import os
import pickle
import time

import numpy as np
import pandas as pd
from datasets import Dataset, concatenate_datasets
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm


class Autodata:
    def __init__(self, data_folder):
        self.data_foloder = data_folder
        self.concat_dataset = self.concat_datasets(self.data_foloder)

    def concat_datasets(self, data_foloder):
        datasets = []
        for file_name in os.listdir(data_foloder):
            if file_name.endswith(".csv"):
                file_path = os.path.join(data_foloder, file_name)
                dataset = pd.read_csv(file_path)
                dataframe = dataset[["question", "answer"]]
                dataset = Dataset.from_pandas(dataframe)
                datasets.append(dataset)

        combined_dataset = concatenate_datasets(datasets)
        pd_combiend_dataset = pd.DataFrame(combined_dataset)
        return pd_combiend_dataset

    def build_vector_dataset(self, dataset, path):
        dataset = np.array(dataset)
        model_name = "jhgan/ko-sroberta-multitask"
        model = SentenceTransformer(model_name).to("cuda:0")

        query_vector_list = []

        for i in tqdm(range(len(dataset))):
            question = dataset[i][0]
            query_vector = model.encode(question)
            query_vector_list.append(list(query_vector))

        with open(path, "wb") as fw:
            pickle.dump(query_vector_list, fw)

        with open(path, "rb") as fr:
            vector_data = pickle.load(fr)

        return vector_data

    def load_vector_data(self, path):
        if os.path.isfile(path):
            with open(path, "rb") as fr:
                vector_data = pickle.load(fr)
        else:
            vector_data = self.build_vector_dataset(self.concat_dataset, path)
        return vector_data


def bert_retrieve_QA(q_sentence, model, data, vector_data):
    start_time = time.time()
    model = model.to("cuda:0")

    original_data = data.concat_dataset

    input_vector = model.encode(q_sentence)
    input_vector = np.expand_dims(input_vector, axis=0)

    cos_sim = cosine_similarity(input_vector, vector_data)
    data_cosine = np.sort(cos_sim).squeeze()[::-1][0]
    top_question_idx = np.argsort(cos_sim).squeeze()[::-1][0]

    similar_answer = ""

    if data_cosine >= 0.75:
        similar_question = original_data["question"][top_question_idx]
        similar_answer = original_data["answer"][top_question_idx]
        print(f"retrieve_question: {similar_question}\n")
        print(f"retrieve_answer: {similar_answer}\n")

    print(f"retrieve time: {time.time() - start_time}")

    return similar_answer


def retrieve_debugging(q_sentence):
    model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    model = model.to("cuda:0")

    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "data/bert_retrieval_data")
    data = Autodata(DATA_DIR)
    original_data = data.concat_dataset
    vector_data = data.load_vector_data(os.path.join(DATA_DIR, "query_vector.bin"))

    input_vector = model.encode(q_sentence)
    input_vector = np.expand_dims(input_vector, axis=0)

    cos_sim = cosine_similarity(input_vector, vector_data)
    data_cosine = np.sort(cos_sim).squeeze()[::-1][:3]  # array([0.79316866, 0.7515925 , 0.72607714])
    top_question = np.argsort(cos_sim).squeeze()[::-1][:3]  # array([9285, 9217, 3223])

    print("유사도 : ", data_cosine)

    question_list = []
    answer_list = []

    for i, index in enumerate(top_question):
        if data_cosine[i] >= 0.6:
            question_list.append(original_data["question"][index])
            answer_list.append(original_data["answer"][index])
    count = 0
    for question, answer in zip(question_list, answer_list):
        print(f"유사 상담 사례 질문 {count} : {question}")
        print(f"유사 상담 사례 답변 {count} : {answer}")
        print()
        count += 1


if __name__ == "__main__":
    retrieve_debugging("제가 자동차를 운전하다 중앙선을 침범하다가 2충 추돌사고를 발생시켰습니다. 이때 무슨 법으로 처벌 받을 수 있나요?")
