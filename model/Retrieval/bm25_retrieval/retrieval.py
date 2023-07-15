import json
import os
import pickle
import time
from contextlib import contextmanager
from typing import List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from rank_bm25 import BM25L, BM25Okapi, BM25Plus
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm.auto import tqdm


@contextmanager
def timer(name):
    t0 = time.time()
    yield
    print(f"[{name}] done in {time.time() - t0:.3f} s")


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
