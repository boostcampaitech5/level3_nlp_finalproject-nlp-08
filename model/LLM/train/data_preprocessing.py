import pandas as pd
from datasets import concatenate_datasets, Dataset
from datasets import load_dataset
import os


class Autodata():
    def __init__(self, data_folder='./data', max_length=1024, tokenizer=None):
        self.data_foloder = data_folder
        self.max_length = max_length
        self.tokenizer = tokenizer
        self.concat_dataset = self.concat_datasets(self.data_foloder)
        self.tokenizer_dataset = self.tokenizing_dataset(self.concat_dataset)

    def concat_datasets(self, folder_path):
        datasets = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(folder_path, file_name)
                dataset = pd.read_csv(file_path)
                dataframe = dataset[['question', 'answer']]
                dataset = Dataset.from_pandas(dataframe)
                datasets.append(dataset)

        combined_dataset = concatenate_datasets(datasets)

        return combined_dataset

    def tokenizing_dataset(self, dataset):
        data = dataset.map(
            lambda x: {
                "text": f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x['question']}\n\n### 응답:\n{x['answer']}<|endoftext|>"
            }
        )
        data = data.map(lambda samples: self.tokenizer(samples["text"], truncation=True,
                                                       max_length=self.max_length,
                                                       padding=False,
                                                       return_tensors=None, ), batched=True)

        return data.shuffle()


