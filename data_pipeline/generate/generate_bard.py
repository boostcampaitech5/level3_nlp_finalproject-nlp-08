import os
import pickle
import time

import pandas as pd
from bardapi import Bard
from tqdm.auto import tqdm

bard = Bard(token_from_browser=True)

def get_response(prompt):
    response = bard.get_answer(prompt)
    return response

with open("prompts.pkl", "rb") as f:
    prompts = pickle.load(f)

data = []
num_data = 1
prompt_name = "fewshot"
prompt = prompts["fewshot"]

for i in tqdm(range(num_data)):
    try:
        response = get_response(prompt)
    except:
        time.sleep(5)
        continue
    data.append(
        [
            prompt_name,
            prompt,
            *[response["choices"][i]["content"][0] for i in range(len(response["choices"]))]
        ]
    )

generated_df = pd.DataFrame(
    data,
    columns=[
        "prompt_type",
        "prompt",
        "result_1",
        "result_2",
        "result_3"
    ])

os.makedirs("../data/generated_data/bard", exist_ok=True)
generated_df.to_csv(f"../data/generated_data/bard/generated_data_bard_{len(generated_df)}.csv", index=False)