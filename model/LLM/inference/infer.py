from peft import PeftModel, PeftConfig
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def gen(x, model, tokenizer, device):
    prompt = (
        f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x}\n\n### 응답:\n"
    )
    len_prompt = len(prompt)
    gened = model.generate(
        **tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to(
            device
        ),
        max_new_tokens=256,
        early_stopping=True,
        do_sample=True,
        eos_token_id=2,
    )
    return tokenizer.decode(gened[0])[len_prompt:]


def LLM_infer(input):
    device = (
        torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    )
    peft_model_id = "kfkas/LawBot-v1_koalpaca_legalQA_easylaw"
    config = PeftConfig.from_pretrained(peft_model_id)
    model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path, device_map={"": 0},torch_dtype=torch.float16
    )
    model = PeftModel.from_pretrained(model, peft_model_id,torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

    model.eval()
    model.config.use_cache = (
        True  # silence the warnings. Please re-enable for inference!
    )
    model.float()
    tokenizer.pad_token = tokenizer.eos_token
    output = gen(input, model=model, tokenizer=tokenizer, device=device)

    return output


if __name__ == "__main__":
    text = LLM_infer("LLM입력")
