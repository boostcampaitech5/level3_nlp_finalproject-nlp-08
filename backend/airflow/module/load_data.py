import os

import pandas as pd
from datasets import load_dataset
from dotenv import load_dotenv

load_dotenv()
huggingface_read_token = os.getenv("HUGGINGFACE_READ_TOKEN")

def load_train_data():
    data = load_dataset("YoonSeul/legal-GPT-BARD-train_v3", use_auth_token=huggingface_read_token)
    df = pd.DataFrame(data)

    questions = []
    answers = []

    for i in df.iterrows():
        questions.append(i[1]["train"]["instruction"])
        answers.append(i[1]["train"]["output"])

    train_datasets = {
        "question": questions,
        "answer": answers
    }

    train_df = pd.DataFrame(train_datasets)
    BASE_PATH = os.path.join(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))), "data")
    SAVE_PATH = os.path.join(BASE_PATH, "train_data.csv")
    os.makedirs(BASE_PATH, exist_ok=True)
    train_df.to_csv(SAVE_PATH)

def load_eval_data():
    data = load_dataset("YoonSeul/legal-GPT-BARD-val_v3", use_auth_token=huggingface_read_token)
    df = pd.DataFrame(data)

    questions = []
    answers = []

    for i in df.iterrows():
        questions.append(i[1]["train"]["instruction"])
        answers.append(i[1]["train"]["output"])

    train_datasets = {
        "question": questions,
        "answer": answers
    }

    train_df = pd.DataFrame(train_datasets)
    BASE_PATH = os.path.join(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))), "data")
    SAVE_PATH = os.path.join(BASE_PATH, "eval_data.csv")
    os.makedirs(BASE_PATH, exist_ok=True)
    train_df.to_csv(SAVE_PATH)

def load_train_eval_data():
    load_train_data()
    load_eval_data()

if __name__ == "__main__":
    load_train_eval_data()
