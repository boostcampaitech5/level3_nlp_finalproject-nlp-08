import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import os

model_name = "jhgan/ko-sroberta-multitask"
model = SentenceTransformer(model_name)
model.to("cuda:0")

df = pd.read_csv("./data/law_data.csv")
df = df.dropna(
    subset=["caseName", "judgementAbstract", "precedentText", "judgementNote"]
)
np_df = np.array(df)

Ab_list = []
for i in tqdm(range(len(np_df))):
    Ab = np_df[i][4]
    Ab_query = model.encode(Ab)
    Ab_list.append(list(Ab_query))

df["Ab_vector"] = Ab_list
df.to_csv("Ab_vector_law_data_sroberta.csv", index=False)
