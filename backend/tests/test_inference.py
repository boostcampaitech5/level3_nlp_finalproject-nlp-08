import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app.generate import generate_answer


def test_generate_answer():
    generate_answer("건강하게 살 수 있는 방법은?")
