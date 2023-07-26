import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from inference import infer
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
from tqdm.auto import tqdm

class LawyerEvaluation:
    def __init__(self, path="lawyer_question.csv", model_name="uomnf97/LawBot-level2-final-preprocessing-v3"):
        self.data = pd.read_csv(f"./eval_data_legal/{path}")
        self.model_name = model_name
        self.answer = False

    def generate_answer(self):
        answer_list = [0]*20
        
        device = (
            torch.device("cuda:0") if torch.cuda.is_available(
            ) else torch.device("cpu")
        )
        peft_model_id = self.model_name
        config = PeftConfig.from_pretrained(peft_model_id)
        model = AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path, device_map={"": 0}, torch_dtype=torch.float16
        )
        model = PeftModel.from_pretrained(
            model, peft_model_id, torch_dtype=torch.float16)
        tokenizer = AutoTokenizer.from_pretrained(
            config.base_model_name_or_path
        )
        model.eval()
        model.config.use_cache = (
            True  # silence the warnings. Please re-enable for inference!
        )
        model.float()
        tokenizer.pad_token = tokenizer.eos_token

        for i in tqdm(range(len(self.data)), desc="processing evaluation data"):
            if i == 0 : 
                break
            data = self.data.iloc[i]["question"]
            answer_list.append(infer.gen(data, model=model,
                           tokenizer=tokenizer, device=device))


        self.data["answer"] = answer_list
        self.answer = True

    def to_csv(self):
        if self.answer == True:
            self.data.to_csv(f"./eval_data_legal/lawyer_val_with_answer.csv")
        else:
            print("답안을 생성해주세요!")


if __name__ == "__main__":
    lawyer_evaluation = LawyerEvaluation()
    lawyer_evaluation.generate_answer()
    lawyer_evaluation.to_csv()
