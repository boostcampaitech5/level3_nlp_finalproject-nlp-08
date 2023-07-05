import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def generate_answer(q_sentence: str):
    model_id = "nlpai-lab/kullm-polyglot-5.8b-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map={"":0})

    model.eval()
    model.config.use_cache = True  # silence the warnings. Please re-enable for inference!
    model.float()
    tokenizer.pad_token = tokenizer.eos_token

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

    gened = model.generate(
        **tokenizer(
            f"### 질문: {q_sentence}\n\n### 답변:",
            return_tensors='pt',
            return_token_type_ids=False
        ).to(device),
        max_new_tokens=256,
        early_stopping=True,
        do_sample=True,
        eos_token_id=2,
    )
    return tokenizer.decode(gened[0])
