from airflow import DAG, Dataset
from datetime import datetime
from airflow.operators.bash import BashOperator


myDataSet1 = Dataset("/tmp/myDataSet1.txt")

with DAG(
    dag_id="producer_dag",
    schedule="* * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    writer_task = BashOperator(
        task_id="writer_task",
        bash_command="echo 'Hello World' > /tmp/myDataSet1.txt",
        outlets=[myDataSet1],
    )
