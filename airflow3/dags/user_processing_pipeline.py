from airflow.sdk import dag, task

## Note: Postgres operator is now depricated and so id mysql operator, now for all sql base query, we can do it using this SQLExecuteQueryOperator
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
    create_table()

    @task.sensor()
    def is_api_available() -> PokeReturnValue:
        import requests

        response = requests.get("XXXXXXXXXXXXXXXXXXXXXXXXXX")
        if response.status_code == 200:
            return PokeReturnValue(is_done=True)
        else:
            return PokeReturnValue(is_done=False)


user_processing()
