from datetime import datetime, timedelta
from airflow import DAG
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 10, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id = 'spark_job',
    default_args = default_args,
    description = 'A DAG to run a Spark job',
    catchup = False,
)

submit_spark_task = BashOperator(
    task_id = 'run_spark_job',
    bash_command = 'spark-submit /opt/airflow/dags/spark_code.py',
    dag = dag,
)

submit_spark_task