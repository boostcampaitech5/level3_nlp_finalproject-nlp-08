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
        max_new_tokens=1024,
        early_stopping=True,
        do_sample=True,
        top_k=20,
        top_p=0.92,
        no_repeat_ngram_size=3,
        eos_token_id=2,
        repetition_penalty=1.2,
        num_beams=3,
    )
    return tokenizer.decode(gened[0])[len_prompt:]


def LLM_infer(input, model_type):
    device = (
        torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    )
    if model_type == "kullm":
        peft_model_id = "YoonSeul/LawBot-level-3-KuLLM-5.8B-tae-2epoch"
        config = PeftConfig.from_pretrained(peft_model_id)
        model = AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path,
            device_map={"": 0},
            torch_dtype=torch.float16,
        )
        model = PeftModel.from_pretrained(
            model, peft_model_id, torch_dtype=torch.float16
        )
        tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

        model.eval()
        model.config.use_cache = (
            True  # silence the warnings. Please re-enable for inference!
        )
        tokenizer.pad_token = tokenizer.eos_token
    else:
        model_id = "kfkas/Legal-Llama-2-ko-7b-Chat"
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map={"": 0},
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
        )
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model.eval()
        model.config.use_cache = True
        tokenizer.pad_token = tokenizer.eos_token
    output = gen(input, model=model, tokenizer=tokenizer, device=device)

    return output


if __name__ == "__main__":
    model_type = "kullm"  # llama, kullm
    input = "음주운전을하면 어떤 법으로 처벌 되나요?"
    text = LLM_infer(input, model_type)
