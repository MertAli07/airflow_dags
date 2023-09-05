from airflow import DAG

from datetime import datetime

with DAG('user_processing', start_date=datetime(2022, 9, 5), 
        schedule_interval='@daily', catchup=False) as dag:
    None