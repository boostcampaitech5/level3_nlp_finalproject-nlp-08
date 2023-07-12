import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import pickle

model_name = "jhgan/ko-sroberta-multitask"
model = SentenceTransformer(model_name)
model.to("cuda:0")

df = pd.read_csv("../data/law_data/law_data.csv", encoding="UTF-8")
df = df.dropna(
    subset=["caseName", "judgementAbstract", "precedentText", "judgementNote"]
)
df.to_csv("../data/law_data/law_data_drop.csv", index=False)
np_df = np.array(df)

vector_list = []
for i in tqdm(range(len(np_df))):
    judgementAbstract = np_df[i][4]
    judgementNote = np_df[i][9]

    judgementNote_vector = model.encode(judgementAbstract + judgementNote)
    vector_list.append(list(judgementNote_vector))

with open("../data/law_data/law_data_drop_vector.bin", "wb") as fw:
    pickle.dump(vector_list, fw)
