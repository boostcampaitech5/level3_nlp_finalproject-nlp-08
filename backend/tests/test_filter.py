import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app.filter import is_legal_question


def test_is_legal_question():
    assert not is_legal_question("안녕하세요.")
    assert is_legal_question("제가 술을 먹고 운전을 했는데 어떤 처벌을 받을까요?")
