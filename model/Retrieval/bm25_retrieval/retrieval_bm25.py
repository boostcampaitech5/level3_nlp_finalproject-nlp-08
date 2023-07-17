import os
from typing import Callable, List

import pandas as pd
from datasets import (
    DatasetDict,
)
from retrieval import SparseRetrievalBM25


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
