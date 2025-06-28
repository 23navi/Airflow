from airflow.sdk import dag, task

## Note: Postgres operator is now depricated and so did mysql operator, now for all sql base query, we can do it using this SQLExecuteQueryOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

# from airflow.providers.standard.operators.python import PythonOperator


## To use this postgres provider, we must install it as it is not part of default providers that airflow ships with: uv pip install apache-airflow-providers-postgres==6.1.3
from airflow.providers.postgres.hooks.postgres import PostgresHook


from airflow.sdk.bases.sensor import PokeReturnValue


## Note: Here we were using xcom to communicate the fake user from is_api_available() task, but with task decorator, we won't have to do it
# def _extract_user(ti):
#     fake_user= ti.xcom_pull(task_ids="is_api_available")
#     print(fake_user)


@dag
def user_processing():

    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="postgres_user_processing",
        sql="""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                email VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """,
    )
    # create_table() ## Not sure why is this not working.

    ## Create a new connection, type: postgres, connection id: postgres_user_processing, host: postgres, password: postgres, port: 5432

    @task.sensor(
        poke_interval=30,  ## The sensor will poke every 30 sec
        timeout=3600,  ## The task will fail if the poke doesn't return True within 3600 sec (1hr)
        mode="poke",  ## The sensor will poke the task to check if it is done or not
    )
    def is_api_available() -> PokeReturnValue:
        import requests

        response = requests.get(
            "https://raw.githubusercontent.com/marclamberti/datasets/refs/heads/main/fakeuser.json"
        )
        if response.status_code == 200:
            return PokeReturnValue(is_done=True, xcom_value=response.json())
        else:
            return PokeReturnValue(is_done=False, xcom_value=None)
        
    # extract_user= PythonOperator(
    #     task_id="extract_user",
    #     python_callable=_extract_user
    # )


    @task
    def extract_user(fake_user):
        return {
            "id":fake_user["id"]
        }

    fake_user= is_api_available()
    print(fake_user)
    extract_user(fake_user)


    ## To test the task: airflow tasks test user_processing is_api_available (in scheduler container)


user_processing()
