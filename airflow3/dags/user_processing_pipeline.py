from airflow.sdk import dag, task

## Note: Postgres operator is now depricated and so did mysql operator, now for all sql base query, we can do it using this SQLExecuteQueryOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


## API available sensor
from airflow.sdk.bases.sensor import PokeReturnValue


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

    is_api_available()

    ## To test the task: airflow tasks test user_processing is_api_available (in scheduler container)


user_processing()
