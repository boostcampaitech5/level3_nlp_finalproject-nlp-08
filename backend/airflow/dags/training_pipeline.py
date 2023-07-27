import datetime
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.load_data import load_train_eval_data
from module.train.train_model import train_model

with DAG(
    dag_id="training_pipeline",
    description="train the model periodically",
    start_date=datetime.datetime(2023,07,27),
    schedule_interval="0 0 * * 5",
    tags=["LLM"],
) as dag:

    load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_train_eval_data,
        depends_on_past=True,
        owner="SangwonYoon",
        retries=3,
        retry_delay=datetime.timedelta(minutes=5)
    )

    training_model = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
        depends_on_past=True,
        owner="SangwonYoon",
        retries=3,
        retry_delay=datetime.timedelta(minutes=5)
    )

    load_data >> training_model
