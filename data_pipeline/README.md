# LawBot - Data Pipeline
* All commands in this instruction should be run in the following directory. <br/>
    `/data_pipeline`
## ⚠️ How To install Requirements
* Run the following command on your terminal.

```bash
$ pip install -r requirments.txt
```

## ⌨️ How To Execute
### Web Crawling
```bash
$ python3 crawler.py
$ python3 qa_crawler.py
```
### Data Generation
```bash
$ python3 generate_gpt.py
$ python3 parse.py
```
* To generate data using the GPT model, you need to [obtain an API key](https://platform.openai.com/account/api-keys) from OpenAI first. <br>
Depending on the model used, usage fees might be charged.

* If you want to modify the prompts, follow these steps.
1. Add the prompts in the `backup_prompts.py` file.
2. Run the following command in your terminal.

```bash
$ python3 backup_prompts.py
```
3. New pickle file will be overlapped to existing `prompts.pkl`
4. After that, you can proceed with the stpes mentioned earlier.

### Preprocessing
* Run the following commands in your terminal.
```bash
$ python3 spellchecker.py
$ python3 preprocessor_v2.py
```
