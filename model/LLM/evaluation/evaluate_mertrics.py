from data_preprocessing import PPL_Autodata
from petf_ppl import Perplexity_Petf
import dataset as dataset
import evaluate


data = PPL_Autodata("./eval_data_legal").preprocess_data
petf_model_id = "kfkas/LawBot-v1_koalpaca_legalQA_easylaw_train"
normal_model_id = "nlpai-lab/kullm-polyglot-5.8b-v2"

use = "petf"  # petf or normal

if use == "petf":
    perplexity = Perplexity_Petf()
    results = perplexity.compute(
        model_id=petf_model_id,
        add_start_token=False,
        predictions=data["text"],
        max_length=256,
        batch_size=4,
    )
    print(list(results.keys()))
    print(round(results["mean_perplexity"], 2))
    print(round(results["perplexities"][0], 2))
else:
    perplexity = evaluate.load("perplexity", module_type="metric")
    results = perplexity.compute(
        model_id=normal_model_id,
        add_start_token=False,
        predictions=data["text"],
        max_length=256,
        batch_size=4,
    )
    print(list(results.keys()))
    print(round(results["mean_perplexity"], 2))
    print(round(results["perplexities"][0], 2))
