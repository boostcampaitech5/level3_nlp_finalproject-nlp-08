import time

import torch


def generate_answer(q_sentence: str, model, tokenizer):
    model.eval()
    model.config.use_cache = True  # silence the warnings. Please re-enable for inference!
    model.half()
    tokenizer.pad_token = tokenizer.eos_token

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
    prompt = f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{q_sentence}\n\n### 응답:\n"
    len_prompt = len(prompt)

    start_time = time.time()

    gened = model.generate(
        **tokenizer(
            prompt,
            return_tensors='pt',
            return_token_type_ids=False
        ).to(device),
        max_new_tokens=512,
        early_stopping=True,
        do_sample=True,
        eos_token_id=2,
    )

    print(f"generate time: {time.time() - start_time}")
    return tokenizer.decode(gened[0])[len_prompt:].replace("<|endoftext|>", "")
