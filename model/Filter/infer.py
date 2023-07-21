from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import torch.nn.functional as F

def infer():
    #text = '저와 약혼한 사람이 얼마 전 사기죄로 징역 1년형의 선고를 받고 교도소에서 복역 중입니다. 저희 부모님과 친지 분들은 파혼을 하라고 하고, 저도 파혼했으면 하는데 가능한지요?'
    text = "안녕하세요 김주원입니다."
    base_model_name = 'monologg/koelectra-small-v3-discriminator'
    model = AutoModelForSequenceClassification.from_pretrained('kfkas/legal-question-filter-koelectra', num_labels=2, ignore_mismatched_sizes=True)
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits.detach().cpu()
    pr = F.softmax(logits).numpy()
    arg = np.argmax(pr,axis=1)
    print(logits)
    print(pr)
    print(int(arg))
    if int(arg) == 0 and (pr[0][0] >= 0.98).all():
        print('법률입니다')
    else:
        print('법률 질문이 아닙니다(bard,chatgpt 등등 다른 API 호출하면 좋을거 같아용)')
    #0 = 법률 1 = 일반
if __name__ == '__main__':
    infer()