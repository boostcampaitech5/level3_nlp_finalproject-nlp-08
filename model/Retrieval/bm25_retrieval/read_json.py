import json
import pandas as pd


with open("./all_data/wikipedia_documents.json", "r") as f:
    data = json.load(f)
print(data["0"].keys())

df = pd.read_csv("./all_data/legal_QA.csv")

# 딕셔너리 초기화
data_dict = {}

# 행 번호를 키로 사용하여 딕셔너리에 데이터 추가
for i in range(len(df)):
    key = str(i)
    data_dict[key] = {
        "question": df.iloc[i]["question"],
        "answer": df.iloc[i]["answer"],
    }

# 결과 출력
print(data_dict["0"])
with open("./all_data/legal_QA.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)
