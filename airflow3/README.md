## How to use airflow running on docker

We will be using a new python package and project manager
[uv](https://docs.astral.sh/uv/)

Before starting the airflow using docker compose, we will start a new virtual environment

```bash
uv venv --python 3.11
```

This will output

```
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

Then to activate the venv

```bash
source .venv/bin/activate
```

Now we can install apache locally to get all auto completes

```bash
uv pip install apache-airflow==3.0.0
```

Now run the docker compose instance

```bash
docker compose up -d
```

Airflow will start on port 3000 with default username and password
