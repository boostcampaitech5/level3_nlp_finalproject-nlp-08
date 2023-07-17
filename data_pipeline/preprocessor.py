import re

import pandas as pd


def remove_escape(raw_text: str) -> str:
    pattern = r"\t|\n|\xa0"
    processed_text = re.sub(pattern, " ", raw_text)
    processed_text_stripped = " ".join(processed_text.split())
    return processed_text_stripped


def remove_phone_number(raw_text: str) -> str:
    pattern = r"\(*\d+\s*-\s*\d+\s*-\s*\d+\)*"
    processed_text = re.sub(pattern, "", raw_text)
    return processed_text


def remove_hyperlink(raw_text: str) -> str:
    pattern = (
        r":*\s*\(*:*\s*https?://[\w\dㄱ-ㅎㅏ-ㅣ가-힣!@#$%^&*(),.?/:;\"'<>{}|+=~_-]+\s*\)*"
    )
    processed_text = re.sub(pattern, "", raw_text)
    return processed_text


def remove_header(raw_text: str) -> str:
    header_pattern = "안녕하십니까. 대한법률구조공단 사이버상담을 이용해 주셔서 감사합니다."
    header_end_idx = re.search(header_pattern, raw_text)
    if header_end_idx != None:
        processed_text = raw_text[header_end_idx.end() :]
        return processed_text
    else:
        return raw_text


def remove_footer(raw_text: str) -> str:
    footer_pattern = "1. 위 답변은 귀하께서 제공해주신 사실관계에 기초한 답변자 개인의 법률적 의견으로서 이와 다른 의견이 있을 수도 있으므로 참고자료로만 활용해주시고,"
    footer_start_idx = re.search(footer_pattern, raw_text)
    if footer_start_idx != None:
        processed_text = raw_text[: footer_start_idx.start()]
        return processed_text
    else:
        return raw_text


def preprocess(raw_text: str) -> str:
    preprocessed_text = raw_text
    preprocess_functions = [
        remove_header,
        remove_footer,
        remove_escape,
        remove_phone_number,
        remove_hyperlink,
    ]
    for preprocess_function in preprocess_functions:
        preprocessed_text = preprocess_function(preprocessed_text)
    return preprocessed_text


if __name__ == "__main__":
    df = pd.read_csv("./data/raw_qa_dataset.csv")
    preprocessed_df = df.assign(
        content=df["content"].apply(preprocess), answer=df["answer"].apply(preprocess)
    )
    preprocessed_df.to_csv("./data/preprocessed_qa_dataset.csv", index=False)
