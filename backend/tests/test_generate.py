import os
import sys

import torch

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app.generate import generate_answer
from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def test_generate_answer():
    q_sentence = "제가 술을 먹고 운전을 했는데 어떤 처벌을 받을까요?"
    peft_model_id = "YoonSeul/LawBot-level-3-KuLLM-5.8B-tae-2epoch"
    config = PeftConfig.from_pretrained(peft_model_id)
    model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path, device_map={"": 0}, torch_dtype=torch.float16
    )
    model = PeftModel.from_pretrained(model, peft_model_id, torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
    generate_answer(q_sentence=q_sentence, model=model, tokenizer=tokenizer)
