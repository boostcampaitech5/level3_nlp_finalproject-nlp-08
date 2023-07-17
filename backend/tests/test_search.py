import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import numpy as np
import pandas as pd
from app.search import load_vector_data, search_precedent
from sentence_transformers import SentenceTransformer


def test_search_precedent():
    q_a_sentence = "교통법규 위반으로 벌점을 받았습니다. 이 벌점은 소멸되지 않고 계속 누적되나요?"+"벌점이 소멸되는 것이 아니라 누적되어 관리됩니다. 즉, 벌점이 누적되면 운전면허가 취소되거나 정지될 수 있습니다.    벌점 누적에 따른 운전면허의 취소 또는 정지 기준은 다음과 같습니다(도로교통법 시행규칙 별표 28).  운전면허 취소기준   1. 혈중알콜농도가 0.1% 이상인 사람이 자동차 등을 운전한 경우   2. 음주측정기에 의한 측정결과에 불복하는 사람이 술에 취한 상태에 있다고 인정할 만한 상당한 이유가 있음에도 불구하고 경찰공무원의 측정 요구에 불응하거나 경찰공무원을 폭행 또는 협박한 경우(단, 운전자가 경찰공무원에게 폭행을 가한 경우에는 그 정도가 심하지 않을 때에 한함)   3. 적성검사를 받지 않거나 적성검사에 불합격된 사람이 다시 운전면허를 받고자 하는 경우  4. 자동차를 이용하여 범죄행위를 한 경우  5. 다른 사람의 자동차를 훔치거나 빼앗은 경우  6. 교통사고를 야기하고 도주한 경우  7. 단속경찰공무원 등을 폭행한 경우 8. 정차ㆍ주차위반에 대한 조치"

    model = SentenceTransformer("jhgan/ko-sroberta-multitask")

    print("Load data")
    base_path = os.path.abspath(os.path.dirname(__file__))

    text_data = np.array(pd.read_csv(base_path + "/../data/law_data/law_data.csv"))
    vector_data = load_vector_data(
        base_path + "/../data/law_data/law_data_drop_vector.bin"
    )

    search_precedent(q_a_sentence=q_a_sentence, model=model, text_data=text_data, vector_data=vector_data)
