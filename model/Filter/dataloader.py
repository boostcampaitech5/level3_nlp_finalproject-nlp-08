import pandas as pd
import torch
from tqdm.auto import tqdm
from transformers import AutoTokenizer


class CustomDataset(torch.utils.data.Dataset):
    def __init__(
        self,
        data_file,
        state,
        text_columns,
        target_columns,
        max_length=256,
        model_name="klue/roberta-small",
    ):
        self.state = state
        self.data = data_file
        self.text_columns = text_columns
        self.max_length = max_length
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        if self.state == "test":
            self.inputs = self.preprocessing(self.data)
        else:
            self.target_columns = target_columns if target_columns is not None else []
            self.inputs, self.targets = self.preprocessing(self.data)

    def __getitem__(self, idx):
        if self.state == "test":
            return {"input_ids": torch.tensor(self.inputs[idx], dtype=torch.long)}
        else:
            return {
                "input_ids": torch.tensor(self.inputs[idx], dtype=torch.long),
                "labels": torch.tensor(self.targets[idx], dtype=torch.long),
            }

    def __len__(self):
        return len(self.inputs)

    def tokenizing(self, dataframe: pd.DataFrame) -> list:
        """
        토크나이징
            Args :
                dataframe (DataFrame): 토크나이징할 데이터
            Return :
                data (list) : 학습할 문장 토큰 리스트
        """
        data = []
        for item in tqdm(
            dataframe["question"], desc="Tokenizing", total=len(dataframe["question"])
        ):
            text = item
            # text = [item for text_column in self.text_columns]
            outputs = self.tokenizer(
                text,
                add_special_tokens=True,
                padding="max_length",
                truncation=True,
                max_length=self.max_length,
            )
            data.append(outputs["input_ids"])
        return data

    def preprocessing(self, data):
        inputs = self.tokenizing(data)
        if self.state == "test":
            return inputs
        else:
            try:
                targets = data[self.target_columns]
            except:
                targets = []
            return inputs, targets
