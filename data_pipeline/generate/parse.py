import os
import re

import pandas as pd


def collect_raw_data(path):
    raw_data = [data for data in os.listdir(path) if data.endswith(".csv")]
    collected_data = pd.DataFrame()

    for data in raw_data:
        data_path = os.path.join(path, data)
        df = pd.read_csv(data_path)
        collected_data = pd.concat([collected_data, df], ignore_index=True)

    collected_data = collected_data.drop_duplicates()
    collected_data = collected_data.reset_index()
    return collected_data


def check_output_format(data):
    for idx, datum in enumerate(data):
        pattern = r"\[\s*(질문|답변|Q|A)\s*\d*\]|(질문|답변)\s*:\s*"
        is_fit_format = (re.search(pattern, datum) != None)
        if is_fit_format:
            continue
        else:
            print(f"Index {idx} is out of format")
            return False
    return True


def check_qa_pair(data):
    mismatched_indices = [idx for idx, datum in enumerate(data) if (len(datum) % 2) != 0]
    return mismatched_indices


path = "../data/generated_data/gpt"
raw_data = collect_raw_data(path)
raw_outputs = raw_data.output.tolist()

print(f"Found {len(raw_outputs)} data points.")

assert check_output_format(raw_outputs) == True, "Check the format of the data"

processed_outputs = []

for idx, raw_data in enumerate(raw_outputs):
    pattern = r"\[\s*(질문|답변|Q|A)\s*\d*\]|(질문|답변)\s*:\s*"
    processed_data = re.sub(pattern, "[SEP]", raw_data)
    processed_data = processed_data.split("[SEP]")
    processed_data = [data.strip() for data in processed_data if len(data) > 20]
    processed_data = [re.sub(r"\[\s*예시\s*\d*\]", "", data) for data in processed_data]

    if len(processed_data) % 2 != 0:
        if len(processed_data) == 1: 
            continue
        processed_data = processed_data[:-1] 
    processed_outputs.append(processed_data)

assert len(check_qa_pair(processed_outputs)) == 0, "QA pair mismatched data exists."

q_list = []
a_list = []
for output in processed_outputs:
    while len(output) != 0:
        q_list.append(output.pop(0))
        a_list.append(output.pop(0))

assert len(q_list) == len(a_list), "QA pair mismatch"

processed_data = pd.DataFrame({"question": q_list, "answer": a_list})
processed_data.to_csv(f"./data/generated_qa_data_{len(processed_data)}.csv", index=False)

print(f"Generated {len(processed_data)} pairs of QA data.")