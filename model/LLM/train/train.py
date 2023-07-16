from load_model import load_model
from data_preprocessing import Autodata
import transformers
def train():

    model_id = 'nlpai-lab/kullm-polyglot-5.8b-v2'
    model,tokenizer = load_model(model_id)
    tokenizer.pad_token = tokenizer.eos_token
    train_data = Autodata(data_folder='./data',tokenizer=tokenizer).tokenizer_dataset
    val_data = Autodata(data_folder='./val_data',tokenizer=tokenizer).tokenizer_dataset
    trainer = transformers.Trainer(
        model=model,
        train_dataset= train_data,
        eval_dataset = val_data,
        args=transformers.TrainingArguments(
            per_device_train_batch_size=16,
            gradient_accumulation_steps=1,
            num_train_epochs=6,
            learning_rate=1e-4,
            fp16=True,
            logging_steps=10,
            save_strategy="epoch",
            evaluation_strategy="epoch",
            output_dir="./model_outputs",
            optim="paged_adamw_8bit",
        ),
        data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
    )
    model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
    trainer.train()

    push_model_id = 'kfkas/LawBot-level2-5.8B_FIX'
    huggingface_write_token = ''# Huggingface Write Token 작성

    model.push_to_hub(
        push_model_id,
        use_temp_dir=True,
        use_auth_token=huggingface_write_token
    )
    print(f'{push_model_id} 모델 업로드 완료!')
if __name__ == '__main__':
    train()