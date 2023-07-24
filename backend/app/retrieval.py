import json
import os
import time
from typing import Callable, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from datasets import Dataset, DatasetDict, concatenate_datasets
from rank_bm25 import BM25L, BM25Okapi, BM25Plus
from transformers import AutoTokenizer


def infer(q_sentence):
    start_time = time.time()

    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    data_path = os.path.join(BASE_DIR, "data/all_data")
    data = Autodata(data_path)
    data.load_json_data(path=os.path.join(data_path, "all_data.json"))
    tokenizer = AutoTokenizer.from_pretrained("nlpai-lab/kullm-polyglot-5.8b-v2")

    datasets = run_sparse_retrieval(
        tokenize_fn=tokenizer.tokenize, data_path=data_path, datasets=q_sentence, bm25="plus"
    )

    print(f"retrieve time: {time.time() - start_time}")
    print(f"retrieve_question: {datasets[2][0]}")

    return datasets[3][0]


class Autodata:
    def __init__(self, data_folder="./data"):
        self.data_foloder = data_folder
        self.concat_dataset = self.concat_datasets(self.data_foloder)

    def concat_datasets(self, data_foloder):
        datasets = []
        pd_datasets = []
        for file_name in os.listdir(data_foloder):
            if file_name.endswith(".csv"):
                file_path = os.path.join(data_foloder, file_name)
                dataset = pd.read_csv(file_path)
                dataframe = dataset[["question", "answer"]]
                pd_datasets.append(dataframe)
                dataset = Dataset.from_pandas(dataframe)
                datasets.append(dataset)

        combined_dataset = concatenate_datasets(datasets)
        pd_combiend_dataset = pd.DataFrame(combined_dataset)

        return pd_combiend_dataset


    def make_all_data(self, data, path):
        df = data
        data_dict = {}

        for i in range(len(df)):
            key = str(i)
            data_dict[key] = {
                "question": df.iloc[i]["question"],
                "answer": df.iloc[i]["answer"],
            }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=4)

    def load_json_data(self, path="./all_data/all_data.json"):
        if not os.path.isfile(path):
            self.make_all_data(self.concat_dataset, path)


def setup_bm25(parent_class):
    class CustomBM25(parent_class):
        def __init__(self, corpus, tokenizer):
            super().__init__(corpus, tokenizer)

        def get_relevant_doc(self, query, k):
            query_vec = self.tokenizer(query)
            result = self.get_scores(query_vec)
            sorted_result = np.argsort(result.squeeze())[::-1]
            doc_score = result.squeeze()[sorted_result].tolist()[:k]
            doc_indices = sorted_result.tolist()[:k]
            return doc_score, doc_indices

        def get_relevant_doc_bulk(self, queries, k):
            doc_scores = []
            doc_indices = []
            for query in queries:
                doc_score, doc_indice = self.get_relevant_doc(query, k)
                doc_scores.append(doc_score)
                doc_indices.append(doc_indice)
            return doc_scores, doc_indices

    return CustomBM25


class SparseRetrievalBM25:
    def __init__(
        self,
        tokenize_fn,
        data_path: Optional[str] = "./csv_data/",
        context_path: Optional[str] = "all_data.json",
        bm25_type: Optional[str] = "",
    ) -> None:
        self.data_path = data_path
        with open(os.path.join(data_path, context_path), "r", encoding="utf-8") as f:
            wiki = json.load(f)

        self.contexts = list(([v["question"] for v in wiki.values()]))
        self.contexts_answer = list(([v["answer"] for v in wiki.values()]))

        if bm25_type == "Okapi":
            bm25_class = setup_bm25(BM25Okapi)
            self.bm25 = bm25_class(self.contexts, tokenize_fn)
        elif bm25_type == "L":
            bm25_class = setup_bm25(BM25L)
            self.bm25 = bm25_class(self.contexts, tokenize_fn)
        elif bm25_type == "plus":
            bm25_class = setup_bm25(BM25Plus)
            self.bm25 = bm25_class(self.contexts, tokenize_fn)

    def retrieve(
        self, query_or_dataset: Union[str, pd.DataFrame], topk: Optional[int] = 1
    ) -> Union[Tuple[List, List], pd.DataFrame]:
        if isinstance(query_or_dataset, str):
            doc_scores, doc_indices = self.bm25.get_relevant_doc(
                query_or_dataset, k=topk
            )
            return (
                doc_scores,
                doc_indices,
                [self.contexts[doc_indices[i]] for i in range(topk)],
                [self.contexts_answer[doc_indices[i]] for i in range(topk)],
            )


def run_sparse_retrieval(
    tokenize_fn: Callable[[str], List[str]],
    datasets: pd.DataFrame,
    data_path: str = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "csv_data"
    ),
    context_path: str = "all_data.json",
    bm25: str = None,
    ) -> DatasetDict:
    assert bm25 in ["Okapi", "L", "plus"], "Invalid type for BM25 has been passed."

    retriever = SparseRetrievalBM25(
        tokenize_fn=tokenize_fn,
        data_path=data_path,
        context_path=context_path,
        bm25_type=bm25,
    )

    df = retriever.retrieve(datasets, topk=3)
    return df
