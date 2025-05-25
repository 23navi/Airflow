from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime


myDataSet1 = Dataset("/tmp/myDataSet1.txt")

with DAG(
    dag_id="consumer_with_decoration_dag",
    schedule=[myDataSet1],
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    @task(outlets=[myDataSet1])
    def update_dataset():
        with open(myDataSet1.uri, "a") as f:
            f.write("consumer_with_decoration_dag updated")

    updated_dataset = update_dataset()
