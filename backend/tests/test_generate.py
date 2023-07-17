import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app.generate import generate_answer
from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def test_generate_answer():
    q_sentence = "건강하게 살 수 있는 방법은?"
    peft_model_id = "kfkas/LawBot-level1-2000iter"
    config = PeftConfig.from_pretrained(peft_model_id)
    model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path, device_map={"": 0}
    )
    model = PeftModel.from_pretrained(model, peft_model_id)
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
    generate_answer(q_sentence=q_sentence, model=model, tokenizer=tokenizer)
