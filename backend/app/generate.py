import time

import torch


def generate_answer(q_sentence: str, model, tokenizer):
    model.eval()
    model.config.use_cache = True  # silence the warnings. Please re-enable for inference!
    # model.float()
    tokenizer.pad_token = tokenizer.eos_token

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
    # prompt = f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{q_sentence}\n\n### 응답:\n"
    prompt = f"다음은 법률 QA입니다. 질문에 맞는 적절한 응답을 작성하세요.\n\n### 질문:\n{q_sentence}\n\n### 응답:\n"
    # prompt = f"다음은 폭행 관련 법률 QA입니다. 질문과 관련된 자료를 가져온 다음 해당 내용을 요약하여 응답을 작성하세요.\n\n### 질문:\n{q_sentence}\n\n### 응답:\n"
    # prompt = f"다음은 폭행 관련 법률 QA입니다. 상황을 읽고 질문에 맞는 적절한 응답을 작성하세요.\n\n### 상황:\n혁준이가 술을 마시고 아내를 폭행했어. 근데 아내는 외도를 했던 상황이야\n\n### 질문:\n감형이 가능할까?\n\n### 응답:\n"
    len_prompt = len(prompt)

    start_time = time.time()

    gened = model.generate(
        **tokenizer(
            prompt,
            return_tensors='pt',
            return_token_type_ids=False
        ).to(device),
        max_new_tokens=1024,
        early_stopping=True,
        do_sample=True,
        eos_token_id=2,
        # temperature=1e-5,
        top_k=5,
        top_p=0.95,
        no_repeat_ngram_size=2,
        num_beams=3,
        # force_words_ids = tokenizer("폭행", add_special_tokens=False).input_ids,
    )

    print(f"generate time: {time.time() - start_time}")
    answer = tokenizer.decode(gened[0])[len_prompt:].replace("<|endoftext|>", "").replace("\n\n", "\n")
    return answer
