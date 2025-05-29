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
    task_a = BashOperator(
        task_id="task_a", retries=5, bash_command="echo task_a", owner="navi"
    )

    ## This task will fail as the return is exit code 1
    task_b = BashOperator(
        task_id="task_b",
        retries=5,
        retry_delay=10,
        bash_command="echo 'task_b' && exit 1",
        owner="navi2",
    )
