from transformers import AutoTokenizer
from retrieval_bm25 import run_sparse_retrieval
from data_preprocessing import Autodata


def infer(input):
    data_path = "./all_data"
    data = Autodata(data_path)
    data.load_json_data(path="./all_data/all_data.json")
    tokenizer = AutoTokenizer.from_pretrained("nlpai-lab/kullm-polyglot-5.8b-v2")

    datasets = run_sparse_retrieval(
        tokenize_fn=tokenizer.tokenize, data_path=data_path, datasets=input, bm25="plus"
    )  # bm25 => None(TF-IDF), Okapi, L, plus

    print("유사도", datasets[0])
    print("인덱스", datasets[1])
    print("실제 질문", input)

    for question, answer in zip(datasets[2], datasets[3]):
        print("유사 질문")
        print(question)
        print("유사 답변")
        print(answer)
        print("-" * 200)


if __name__ == "__main__":
    infer(
        "저는 중소기업을 운영하고 있는데, 평소 저희 회사의 품질과 신용을 좋게 평가해온 동일업종의 사업가가 저희 회사의 상호(商號)를 사겠다고 합니다. 상호를 팔 수 있는지요?"
    )
