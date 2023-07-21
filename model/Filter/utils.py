import evaluate
import numpy as np
def compute_metrics(eval_pred):
    accuracy = evaluate.load("f1")
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)