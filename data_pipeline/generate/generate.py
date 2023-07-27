import os
import pickle
import time

import openai
import pandas as pd
from tqdm.auto import tqdm

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_response(prompt, model="gpt-3.5-turbo", temperature=1.0, max_tokens=1000):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response


def get_price_of_inference(model, input_tokens, output_tokens):
    if model == "gpt-3.5-turbo-0613":
        input_price_per_k = 0.0015
        output_price_per_k = 0.002
        price_dollar = (input_tokens * input_price_per_k + output_tokens * output_price_per_k) / 1000
        price_won = round(price_dollar * 1281.61, 5)
        return [price_dollar, price_won]
    else:
        return None
    
    
with open("prompts.pkl", "rb") as f:
    prompts = pickle.load(f)
    
full_responses = {}
data = []
num_data = 1000
prompt_type = "fewshot"
prompt = prompts["fewshot"]

for i in tqdm(range(num_data)):
    try:
        response = get_response(prompt)
    except:
        time.sleep(5)
        continue
    full_responses[prompt_type] = response
    output = response.choices[0].message.content # GPT output
    model = response.model # Model used
    input_tokens = response.usage.prompt_tokens # Number of tokens of input
    output_tokens = response.usage.completion_tokens # Number of tokens of output
    data.append(
        [
            prompt_type,
            prompt,
            output,
            model,
            input_tokens,
            output_tokens,
            *get_price_of_inference(model, input_tokens, output_tokens)
        ],
    )

generated_df = pd.DataFrame(
    data,
    columns=[
        "prompt_type",
        "prompt",
        "output",
        "model",
        "input_tokens",
        "output_tokens",
        "price_dollar",
        "price_won"
    ])

generated_df.to_csv(f"./data/generated_data/generated_raw_data_{len(generated_df)}.csv", index=False)