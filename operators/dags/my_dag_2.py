from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime


with DAG(
    dag_id="my_dag_2",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={"owner": "random_owner"},
) as dag:
    task_a = BashOperator(task_id="task_a", bash_command="echo task_a", owner="navi")
    task_b = BashOperator(task_id="task_b", bash_command="echo task_b", owner="navi2")
