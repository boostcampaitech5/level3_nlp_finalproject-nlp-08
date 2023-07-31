import time

import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def is_legal_question(q_sentence):
    start_time = time.time()
    base_model_name = "monologg/koelectra-small-v3-discriminator"
    model = AutoModelForSequenceClassification.from_pretrained(
        "kfkas/legal-question-filter-koelectra",
        num_labels=2,
        ignore_mismatched_sizes=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    inputs = tokenizer(q_sentence, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits.detach().cpu()
    pr = F.softmax(logits, dim=1).numpy()
    # arg = np.argmax(pr, axis=1)
    # print(logits)
    # print(pr)
    # print(int(arg))

    print(f"filter time: {time.time() - start_time}")
    
    if pr[0][0] >= 0.98:
        return True
    return False
