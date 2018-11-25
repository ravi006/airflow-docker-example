"""Simple DAG that uses a few python operators."""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 09, 09),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
}


def get_callable_function(**kwargs):
    Printnl("Hello !!  Python Operator")
    return 'Success!!! Execution time = {}'.format(kwargs['execution_date'])


dag = DAG(
    'pipeline_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1),
    catchup=False,
)

fetch_users_data = PythonOperator(
    task_id='data_fetch',
    provide_context=True,
    python_callable=get_callable_function,
    dag=dag
)

end_task = DummyOperator(
    task_id='dummy_task',
    dag=dag
)

end_task << fetch_users_data
