from data_preprocessing import Autodata
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def Query_BERT_infer(input):
    model_name = "jhgan/ko-sroberta-multitask"
    model = SentenceTransformer(model_name).to("cuda:0")

    data = Autodata("./data")
    original_data = data.concat_dataset
    vector_data = data.load_vector_data()

    input_vector = model.encode(input)
    input_vector = np.expand_dims(input_vector, axis=0)

    cos_sim = cosine_similarity(input_vector, vector_data)
    data_cosine = np.sort(cos_sim).squeeze()[::-1][:3]
    top_question = np.argsort(cos_sim).squeeze()[::-1][:3]

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
    Query_BERT_infer("제가 자동차를 운전하다 중앙선을 침범하다가 2충 추돌사고를 발생시켰습니다. 이때 무슨 법으로 처벌 받을 수 있나요?")
