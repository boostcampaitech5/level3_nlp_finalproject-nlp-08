import pandas as pd
from datasets import concatenate_datasets, Dataset, load_dataset
import os


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

        return combined_dataset

    def load_instruction_dataset(self, dataset_id):
        koalpaca_data = load_dataset(dataset_id)
        data = koalpaca_data["train"]
        data = data.rename_column("instruction", "question")
        question = data["question"]
        return question

    def label_indexing(self, data, state):
        if state == 1:
            answer = 1
        else:
            answer = 0
        answer_list = [answer] * len(data)

        return Dataset.from_dict({"question": data, "target": answer_list})
