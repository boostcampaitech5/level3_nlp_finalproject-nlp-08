import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app.bm25_retrieval import retrieve_QA


def test_retrieve_QA():
    retrieve_QA("제가 술을 먹고 운전을 했는데 어떤 처벌을 받을까요?")
