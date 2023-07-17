import pandas as pd
from datasets import concatenate_datasets, Dataset
from datasets import load_dataset
import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


class Autodata:
    def __init__(self, data_folder="./data"):
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

    def load_vector_data(self, path="./data/query_vector.bin"):
        if os.path.isfile(path):
            with open(path, "rb") as fr:
                vector_data = pickle.load(fr)
        else:
            vector_data = self.build_vector_dataset(self.concat_dataset, path)
        return vector_data
