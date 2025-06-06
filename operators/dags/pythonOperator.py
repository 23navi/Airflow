from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


def _my_callback_with_context(**context):
    print(context)


def _my_callback_with_custom_kwargs(my_arg, **kwargs):
    print(my_arg)
    print(kwargs["dag"])
    print(kwargs)


with DAG(
    dag_id="pythonOperator",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task_a = PythonOperator(task_id="task_a", python_callable=lambda: print("task_a"))
    task_b = PythonOperator(task_id="task_b", python_callable=_my_callback_with_context)
    task_c = PythonOperator(
        task_id="task_c",
        python_callable=_my_callback_with_custom_kwargs,
        op_kwargs={"my_arg": "task_c"},
    )
