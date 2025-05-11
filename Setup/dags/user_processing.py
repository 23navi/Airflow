from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="user_processing",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    pass
