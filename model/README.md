# LawBot - Model

## 💻 Getting Started
<img src=https://github.com/taemin6697/Paper_Review/assets/96530685/9f94505c-4fda-41ae-9a67-1e4c96c501cc style="max-width: 200px; width: 100%" />

## ⚠️ How To install Requirements
### Cuda install

1. Run the following code on your terminal.

```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
chmod +x cuda_11.8.0_520.61.05_linux.run
sh cuda_11.8.0_520.61.05_linux.run
```
2. Input `accept` to proceed.

<img width="579" alt="Screenshot 2023-07-17 at 9 26 12 PM" src="https://github.com/boostcampaitech5/level2_klue-nlp-08/assets/81630351/7a483729-188e-43ec-ab25-f334549f2bd3">

3. Select the driver and install.

<img width="579" alt="Screenshot 2023-07-17 at 9 26 25 PM" src="https://github.com/boostcampaitech5/level2_klue-nlp-08/assets/81630351/e0405f88-c0b3-4258-8be2-071a0d6518e7">


4. Run the following commands on your terminal.
```bash
$ export PATH=/usr/local/cuda-11.8/bin:$PATH
$ export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH
$ pip install -r requirements.txt
```
## ⌨️ How To Train
### LLM (Large Language Model)
* Before training, place Legal QA data at following directory <br/>
    `model/LLM/train/data` <br/>
    `model/LLM/train/val_data`
* HuggingFace Write Token should be filled at line #38 of the following file
* Run the following command on your terminal
```bash
$ python3 model/LLM/train/train.py
```
### Question Filterering Model (Koelectra)
```bash
$ python3 model/Filter/train.py
```
## ⌨️ How To Infer
### LLM (Large Language Model)
* peft model id should be changed after training at line #27 of the following file
* Run the following command on your terminal

```bash
$ python3 model/LLM/inference/infer.py
```
### Sentence BERT Retrieval
* Before training, place Legal QA data at following directory <br/>
    `model/Retrieval/bert_retrieval/data` <br/>
* Run the following command on your terminal

```bash
$ python3 model/Retrieval/bert_retrieval/retrieval_main.py
```
### BM25 Retrieval
* Before training, place Legal QA data at following directory <br/>
    `model/Retrieval/bm25_retrieval/all_data` <br/>
* Run the following command on your terminal

```bash
$ python3 model/Retrieval/bm25_retrieval/retrieval_main.py
```
### Question Filtering Model (Koelectra)
* Run the following command on your terminal

```bash
$ python3 model/Filter/infer.py
```
## ⌨️ How To Evaluate
### LLM (Large Language Model)
* model name and `use` parmater should be changed if needed
* Run the following command on your terminal
```bash
$ python3 model/LLM/evaluation/evaluate_metrics.py
```
