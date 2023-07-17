import pandas as pd
from datasets import concatenate_datasets
from datasets import load_dataset
import os


class PPL_Autodata:
    def __init__(self, data_folder="./eval_data_legal"):
        self.data_foloder = data_folder
        self.concat_dataset = self.concat_datasets(self.data_foloder)
        self.preprocess_data = self.preprocessing_data(self.concat_dataset)

    def concat_datasets(self, folder_path):
        datasets = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(folder_path, file_name)
                dataset = load_dataset("csv", data_files=file_path)
                datasets.append(dataset["train"])

        combined_dataset = concatenate_datasets(datasets)
        if len(combined_dataset.features) > 2:
            data = combined_dataset.remove_columns("title")
        else:
            data = combined_dataset
        return data

    def preprocessing_data(self, dataset):
        data = dataset.map(
            lambda x: {
                "text": f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x['question']}\n\n### 응답:\n{x['answer']}"
            }
        )
        return data
