from airflow import DAG, Dataset
from datetime import datetime
from airflow.operators.bash import BashOperator


myDataSet1 = Dataset("/tmp/myDataSet1.txt")

with DAG(
    dag_id="consumer_dag",
    schedule=[myDataSet1],
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    reader_task = BashOperator(
        task_id="reader_task",
        bash_command="cat /tmp/myDataSet1.txt",
    )
