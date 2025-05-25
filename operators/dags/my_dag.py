from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime


with DAG(
    dag_id="my_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task_a = BashOperator(task_id="task_a", bash_command="echo task_a")

    task_b = BashOperator(task_id="task_b", bash_command="echo task_recreated")

    task_c = BashOperator(task_id="task_c", bash_command="echo task_c")

    task_d = BashOperator(task_id="task_d", bash_command="echo task_d")

    task_a >> task_b >> task_c >> task_d
