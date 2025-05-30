from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.helpers import cross_downstream

from datetime import datetime


with DAG(
    dag_id="pool_party",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    ext_1 = BashOperator(task_id="ext_1", bash_command="echo ext_1 && sleep 10")
    ext_2 = BashOperator(task_id="ext_2", bash_command="echo ext_2 && sleep 10")

    task_a = BashOperator(task_id="task_a", bash_command="echo task_a && sleep 50")

    task_b = BashOperator(
        task_id="task_b", bash_command="echo task_recreated && sleep 50"
    )

    task_c = BashOperator(task_id="task_c", bash_command="echo task_c && sleep 50")

    store = BashOperator(task_id="store", bash_command="echo task_d && sleep 50")

    cross_downstream([ext_1, ext_2], [task_a, task_b, task_c])
    [task_a, task_b, task_c] >> store
