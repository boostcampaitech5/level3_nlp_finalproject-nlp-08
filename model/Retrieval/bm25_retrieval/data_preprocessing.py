import pandas as pd
from datasets import concatenate_datasets, Dataset
import os
import json


class Autodata:
    def __init__(self, data_folder="./data"):
        self.data_foloder = data_folder
        self.concat_dataset = self.concat_datasets(self.data_foloder)

    def concat_datasets(self, data_foloder):
        datasets = []
        pd_datasets = []
        for file_name in os.listdir(data_foloder):
            if file_name.endswith(".csv"):
                file_path = os.path.join(data_foloder, file_name)
                dataset = pd.read_csv(file_path)
                dataframe = dataset[["question", "answer"]]
                pd_datasets.append(dataframe)
                dataset = Dataset.from_pandas(dataframe)
                datasets.append(dataset)

        combined_dataset = concatenate_datasets(datasets)
        pd_combiend_dataset = pd.DataFrame(combined_dataset)

        return pd_combiend_dataset

    def make_all_data(self, data, path):
        df = data
        data_dict = {}

        for i in range(len(df)):
            key = str(i)
            data_dict[key] = {
                "question": df.iloc[i]["question"],
                "answer": df.iloc[i]["answer"],
            }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=4)

    def load_json_data(self, path="./all_data/all_data.json"):
        if not os.path.isfile(path):
            self.make_all_data(self.concat_dataset, path)
