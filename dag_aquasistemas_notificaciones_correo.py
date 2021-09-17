from airflow import DAG
from core_notifications import NotificationTasks
from airflow.utils.dates import days_ago
from datetime import timedelta

cliente = 'aquasistemas'
conn_id = cliente.replace(' ', '_')+'_postgres'

default_args = {
    'owner': 'airflow',
    'email': ['kevin@kemok.io'],
    'email_on_success':  True,
    'email_on_failure': True,
    'retries': 0   
}

with DAG(
    dag_id='envio_de_correo_de_recordatorio_de_pago_aquasistemas',
    description="Activación asincrona del envío de recordatorios y alertas de pago para Aquasistemas.",
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    max_active_runs=1,
    tags=['aquasistemas', 'comunicación', 'kontact'],
) as DAG:

    nt1 = NotificationTasks(conn_id=conn_id)
    t1 = nt1.tasks(5)
