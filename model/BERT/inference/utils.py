import os
import pickle


def load_vector_data(path):
    if os.path.isfile(path):
        with open(path, "rb") as fr:
            vector_data = pickle.load(fr)
    else:
        print("판례 데이터가 존재하지 않습니다.")
        vector_data = None
    return vector_data
