import dataset as dataset
import evaluate
from datasets import load_dataset

from petf_ppl import Perplexity_Petf
import pandas as pd


# perplexity = evaluate.load("perplexity", module_type="metric")
perplexity = Perplexity_Petf()

path = "../train/data/easy_law.csv"
db = pd.read_csv(path)
dataset = load_dataset("csv", data_files=path)["train"]

data = dataset.map(
    lambda x: {
        "text": f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x['question']}\n\n### 응답:\n{x['answer']}"
    }
)

results = perplexity.compute(
    model_id="kfkas/LawBot-v1_koalpaca_legalQA_easylaw",
    add_start_token=False,
    predictions=data["text"],
    max_length=256,
    batch_size=4,
)
# results = perplexity.compute(model_id='nlpai-lab/kullm-polyglot-5.8b-v2',add_start_token=False,predictions=data['text'],max_length=256,batch_size=4)
print(list(results.keys()))
print(round(results["mean_perplexity"], 2))
print(round(results["perplexities"][0], 2))
