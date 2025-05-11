# Airflow Setup

We will be using docker to runt he airflow in single node setup

Docker compose file: docker-compose.yaml

Create an .env file

```env
AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
AIRFLOW_UID=50000
```

Start airflow: `docker compose up -d`

It will start at [local@8080](localhost:8080)

To stop: `docker compose down`
