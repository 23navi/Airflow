from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.helpers import cross_downstream

from datetime import datetime


with DAG(
    dag_id="pool_vs_Parallelism",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    ext_1 = BashOperator(
        task_id="ext_1", bash_command="echo ext_1 && sleep 10", priority_weight=10
    )
    ext_2 = BashOperator(
        task_id="ext_2", bash_command="echo ext_2 && sleep 10", priority_weight=50
    )

    store = BashOperator(task_id="store", bash_command="echo task_d && sleep 50")

    [ext_1, ext_2] >> store


## So in the above setup, I have 50 tasks and I have not touched any config


# The amount of parallelism as a setting to the executor. This defines
# the max number of task instances that should run simultaneously
# on this airflow installation
parallelism = 32

# The number of task instances allowed to run concurrently by the scheduler
# in one DAG. Can be overridden by ``concurrency`` on DAG level.
dag_concurrency = 16

# The maximum number of active DAG runs per DAG
max_active_runs_per_dag = 16


## Now that I ran the tasks in parallel using [list] and in the default pool, I see only 16 running slot at a time and rest others are in Scheduled Slots
