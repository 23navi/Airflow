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

Airflow will start on port 8080 with default username and password

Say we want to get auto complete, and we are not getting it

One issue can be the python interpreter mismatch

Click on that buttom python interpreter selector and make sure it is using the correct ./venv interpter

Else run

```bash
which python
```

in current active venv env and use that in interperter
