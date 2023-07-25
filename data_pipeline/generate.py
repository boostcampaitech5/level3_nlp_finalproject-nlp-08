import os
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
    
prompts = {
    "zeroshot": "임의의 법률 분쟁 상황을 가정하고, 그에 대한 내용을 질문의 형식으로 만들어주세요. 그리고 해당 질문에 대한 답변을 함께 출력해주세요.",
    "zeroshot2": "법률 분쟁 상황을 가정하고, 해당 상황의 가해자 또는 피해자가 의뢰할 만한 상담 내용을 작성해주세요. 출력에는 해당 상담 내용에 대한 답변을 포함해주세요.",
    "oneshot": """
아래 예시의 형식을 참고하여, 임의의 법률 분쟁 상황에 대한 질의 응답 데이터를 생성해주세요.

[예시]
질문: 남편이 가출하여 연락이 되지 않다가 3년 6개월 뒤 ‘실종자 찾아주기’ 운동의 일환으로 DNA검사를 했더니 남편은 3년 전에 이미 교통사고로 사망하였고, 신원미상자로 처리되었다고 합니다. 가출 전 남편이 들어놓은 사망보험금을 청구했더니 보험회사는 사망 후 3년이 경과하였기 때문에 소멸시효 완성을 주장하고 있습니다. 보험금은 못 받는건가요?

답변: 보험금청구권의 소멸시효는 특별한 다른 사정이 없는 한 보험사고가 발생한 때부터 진행하는 것이 원칙입니다. 그러나 객관적으로 보험사고가 발생한 사실을 확인할 수 없는 사정이 있는 경우에는 보험금청구권자가 보험사고의 발생을 알았거나 알 수 있었던 때부터 보험금청구권의 소멸시효가 진행합니다. 따라서 사례의 경우에는 보험금 청구가 가능합니다.
""",
    "fewshot": """
아래 예시의 형식을 참고하여, 임의의 법률 분쟁 상황에 대한 질의 응답 데이터를 생성해주세요.

[예시 1]
질문: 남편이 가출하여 연락이 되지 않다가 3년 6개월 뒤 ‘실종자 찾아주기’ 운동의 일환으로 DNA검사를 했더니 남편은 3년 전에 이미 교통사고로 사망하였고, 신원미상자로 처리되었다고 합니다. 가출 전 남편이 들어놓은 사망보험금을 청구했더니 보험회사는 사망 후 3년이 경과하였기 때문에 소멸시효 완성을 주장하고 있습니다. 보험금은 못 받는건가요?

답변: 보험금청구권의 소멸시효는 특별한 다른 사정이 없는 한 보험사고가 발생한 때부터 진행하는 것이 원칙입니다. 그러나 객관적으로 보험사고가 발생한 사실을 확인할 수 없는 사정이 있는 경우에는 보험금청구권자가 보험사고의 발생을 알았거나 알 수 있었던 때부터 보험금청구권의 소멸시효가 진행합니다. 따라서 사례의 경우에는 보험금 청구가 가능합니다.

[예시 2]
질문: 아는 사람에게 500만원을 빌려줬는데 갚지 않습니다. 소송을 해야 할 것 같은데 비용이며, 시간이 꽤 들 것 같네요. 방법이 없을까요?

답변: 소송의 당사자가 소송으로 청구하는 금액이나 물건의 가치가 3천만원을 넘지 않는 사건은 시간이나 비용에 있어서 민사소송보다 간편한 절차로 진행할 수 있는 소액사건재판 제도를 이용할 수 있습니다. 소액사건재판 외에도 민사조정이나 지급명령(독촉절차)을 이용할 수도 있습니다.
""",
    "fewshot_with_constraints": """
아래 예시의 형식을 참고하여, 임의의 법률 분쟁 상황에 대한 새로운 질의 응답 데이터를 생성해주세요. 답변을 생성할 때는 다음 조건에 맞게 생성해주세요.

[조건]
- 제시된 예시와는 다른 사레를 바탕으로 질문을 생성해줘
- 대한민국의 법률에 근거하여 법적 분쟁 상황에 대한 답변을 생성해줘
- 대한민국 법률에 실제로 존재하는 조항과, 입력과 유사한 상황에 대한 판례를 답변 내용에 포함해줘

[예시 1]
질문: 남편이 가출하여 연락이 되지 않다가 3년 6개월 뒤 ‘실종자 찾아주기’ 운동의 일환으로 DNA검사를 했더니 남편은 3년 전에 이미 교통사고로 사망하였고, 신원미상자로 처리되었다고 합니다. 가출 전 남편이 들어놓은 사망보험금을 청구했더니 보험회사는 사망 후 3년이 경과하였기 때문에 소멸시효 완성을 주장하고 있습니다. 보험금은 못 받는건가요?

답변: 보험금청구권의 소멸시효는 특별한 다른 사정이 없는 한 보험사고가 발생한 때부터 진행하는 것이 원칙입니다. 그러나 객관적으로 보험사고가 발생한 사실을 확인할 수 없는 사정이 있는 경우에는 보험금청구권자가 보험사고의 발생을 알았거나 알 수 있었던 때부터 보험금청구권의 소멸시효가 진행합니다. 따라서 사례의 경우에는 보험금 청구가 가능합니다.

[예시 2]
질문: 아는 사람에게 500만원을 빌려줬는데 갚지 않습니다. 소송을 해야 할 것 같은데 비용이며, 시간이 꽤 들 것 같네요. 방법이 없을까요?

답변: 소송의 당사자가 소송으로 청구하는 금액이나 물건의 가치가 3천만원을 넘지 않는 사건은 시간이나 비용에 있어서 민사소송보다 간편한 절차로 진행할 수 있는 소액사건재판 제도를 이용할 수 있습니다. 소액사건재판 외에도 민사조정이나 지급명령(독촉절차)을 이용할 수도 있습니다.
""",
}

    
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