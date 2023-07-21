from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from data_preprocessing import Autodata
from datasets import concatenate_datasets
from dataloader import CustomDataset
from sklearn.model_selection import train_test_split
from model.Filter.utils import compute_metrics


def train():
    model_name = 'monologg/koelectra-small-v3-discriminator'
    data = Autodata('./data')
    legal_dataset = data.concat_dataset['question']
    legal_answer_dataset = data.concat_dataset['answer']
    alpaca_dataset = data.load_instruction_dataset("nlpai-lab/kullm-v2")

    legal_data = data.label_indexing(legal_dataset,state=0)
    legal_dataset_answer = data.label_indexing(legal_answer_dataset,state=0)
    alpaca_data = data.label_indexing(alpaca_dataset,state=1)

    total_data = concatenate_datasets([legal_data, alpaca_data,legal_dataset_answer])
    train_dataset, val_dataset = train_test_split(total_data, test_size=0.2, random_state=42)

    train_data = CustomDataset(data_file=train_dataset,model_name=model_name,text_columns='question',target_columns='target',max_length=256,state='train')
    val_data = CustomDataset(data_file=val_dataset,model_name=model_name,text_columns='question',target_columns='target',max_length=256,state='train')

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2, ignore_mismatched_sizes=True)

    args = TrainingArguments(
        output_dir='output_dir',
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=1e-5,
        per_device_train_batch_size=64,
        per_device_eval_batch_size=64,
        num_train_epochs=10,
        weight_decay=0.01,
        load_best_model_at_end=True,
        dataloader_num_workers=4,
        logging_steps=50,
        seed=42,
        group_by_length=True,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_data,
        eval_dataset=val_data,
        compute_metrics=compute_metrics
    )

    trainer.train()







if __name__ == '__main__':
    train()