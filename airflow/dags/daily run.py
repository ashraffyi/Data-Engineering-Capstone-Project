from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator,
                                DropTablesOperator, CreateTablesOperator)
from helpers import SqlQueries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
  # for more info see https://airflow.apache.org/docs/stable/_api/airflow/models/index.html#airflow.models.BaseOperator
    'owner': 'sahussain',
    'start_date': datetime(2020, 4, 12),
  # 'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
	'sla':timedelta(minutes=30)
}

dag = DAG('daily_run',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
		  schedule_interval='* * * * *',
		  #schedule_interval='0 7 * * *',
          catchup=True
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_to_redshift_operator = DummyOperator(task_id='stage_to_redshift_operator',  dag=dag)


stage_covid_cases_to_redshift = StageToRedshiftOperator(
    task_id='stage_covid_cases_to_redshift',
    dag=dag,
    table='covidcases_stage',
    option="cases",
    provide_context=True,
    #file_name = str({{ macros.ds_format(macros.ds_add(ds, 1), "%Y-%m-%d", "%Y%m%d") }}) + ".csv"
)

stage_hospital_to_redshift = StageToRedshiftOperator(
    task_id='stage_hospital_to_redshift',
    dag=dag,
    table='hospital_stage',
    option="hospital"
)

stage_masternode_to_redshift = StageToRedshiftOperator(
    task_id='stage_masternode_to_redshift',
    dag=dag,
    table='masternode_stage',
    option="masternode"
)


create_tables__operator  = DummyOperator(task_id='create_tables__operator',  dag=dag)

# Create table place holder
create_tables__covidcases = DummyOperator(task_id='create_tables__covidcases',  dag=dag)
create_tables__hospital  = DummyOperator(task_id='create_tables__hospital',  dag=dag)
create_tables__masternode  = DummyOperator(task_id='create_tables__masternode',  dag=dag)



quality_checks__operator  = DummyOperator(task_id='quality_checks__operator',  dag=dag)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    tableNames=['covidcases','masternode', 'hospital']
)




end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> stage_to_redshift_operator                

stage_to_redshift_operator >> stage_covid_cases_to_redshift
stage_to_redshift_operator >> stage_hospital_to_redshift
stage_to_redshift_operator >> stage_masternode_to_redshift

stage_covid_cases_to_redshift >> create_tables__operator
stage_hospital_to_redshift >> create_tables__operator
stage_masternode_to_redshift >> create_tables__operator

create_tables__operator >> create_tables__covidcases
create_tables__operator >> create_tables__hospital 
create_tables__operator >> create_tables__masternode

create_tables__covidcases >> quality_checks__operator
create_tables__hospital >> quality_checks__operator
create_tables__masternode >> quality_checks__operator

quality_checks__operator >> run_quality_checks
                 
run_quality_checks >> end_operator
