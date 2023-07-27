# LawBot - Backend

## 1. environtment
* FastAPI
* python 3.8.x (tested on 3.8.5)

## 2. install

* Create your own virtual envorionment.
```bash
$ pip install virtualenv
$ virtualenv <your-virtual-env-name>
$ source <your-virtual-env-name>/bin/activate
```

* Install modules on your virtual environment.
```bash
$ pip install -r requirements.txt
```

## 3. Execute

### Model Server
```bash
$ cd app
$ uvicorn main:app --host=0.0.0.0 --reload
```
### Test
```bash
$ pytest
```
### Airflow
```bash
$ cd airflow
$ airflow db init
$ airflow scheduler
```
## 4. Document
1. Execute server(local)
2. Goto http://localhost:8000/docs
