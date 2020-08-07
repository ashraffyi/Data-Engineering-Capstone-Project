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
    'owner': 'udacity',
    'start_date': datetime(2019, 1, 12),
	#'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('setup',
          default_args=default_args,
          description='only run this once',
          #schedule_interval='0 * * * *',
		  max_active_runs=1,
          catchup=False
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

#Drop Tables

drop_tables_operator = DummyOperator(task_id='drop_tables',  dag=dag)

drop_table_covidcases_stage = DropTablesOperator(
    task_id='drop_table_covidcases_stage',
    dag=dag,
    target_table="covidcases_stage"
)

drop_table_masternode_stage = DropTablesOperator(
    task_id='drop_table_masternode_stage',
    dag=dag,
    target_table="masternode_stage"
)

drop_table_hospital_stage = DropTablesOperator(
    task_id='drop_table_hospital_stage',
    dag=dag,
    target_table="hospital_stage"
)

drop_table_covidcases = DropTablesOperator(
    task_id='drop_table_covidcases',
    dag=dag,
    target_table="covidcases"
)

drop_table_masternode = DropTablesOperator(
    task_id='drop_table_masternode',
    dag=dag,
    target_table="masternode"
)

drop_table_hospital = DropTablesOperator(
    task_id='drop_table_hospital',
    dag=dag,
    target_table="hospital"
)


#create_tables
create_tables_operator = DummyOperator(task_id='create_tables',  dag=dag)

create_tables_covidcases_stage = CreateTablesOperator(
    task_id='create_tables_covidcases_stage',
    dag=dag,
    sql=SqlQueries.table_create_covidcases_stage,
    table = 'table_create_covidcases_stage'
)

create_tables_masternode_stage = CreateTablesOperator(
    task_id='create_tables_masternode_stage',
    dag=dag,
    sql=SqlQueries.table_create_masternode_stage,
    table = 'table_create_masternode_stage'
)

create_tables_hospital_stage = CreateTablesOperator(
    task_id='create_tables_hospital_stage',
    dag=dag,
    sql=SqlQueries.table_create_hospital_stage,
    table = 'table_create_hospital_stage'
)

create_tables_covidcases = CreateTablesOperator(
    task_id='create_tables_covidcases',
    dag=dag,
    sql=SqlQueries.table_create_covidcases,
    table = 'table_create_covidcases'
)

create_tables_masternode = CreateTablesOperator(
    task_id='create_tables_masternode',
    dag=dag,
    sql=SqlQueries.table_create_masternode,
    table = 'table_create_masternode'
)

create_tables_hospital = CreateTablesOperator(
    task_id='create_tables_hospital',
    dag=dag,
    sql=SqlQueries.table_create_hospital,
    table = 'table_create_hospital'
)


end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> drop_tables_operator                

drop_tables_operator >> drop_table_covidcases_stage
drop_tables_operator >> drop_table_masternode_stage
drop_tables_operator >> drop_table_hospital_stage
drop_tables_operator >> drop_table_covidcases                
drop_tables_operator >> drop_table_masternode
drop_tables_operator >> drop_table_hospital     
                
drop_table_covidcases_stage >> create_tables_operator
drop_table_masternode_stage >> create_tables_operator
drop_table_hospital_stage >> create_tables_operator
drop_table_covidcases >> create_tables_operator                 
drop_table_masternode >> create_tables_operator
drop_table_hospital >> create_tables_operator

create_tables_operator >> create_tables_covidcases_stage
create_tables_operator >> create_tables_masternode_stage
create_tables_operator >> create_tables_hospital_stage
create_tables_operator >> create_tables_covidcases
create_tables_operator >> create_tables_masternode
create_tables_operator >> create_tables_hospital

create_tables_covidcases_stage >> end_operator
create_tables_masternode_stage >> end_operator
create_tables_hospital_stage >> end_operator
create_tables_covidcases >> end_operator
create_tables_masternode >> end_operator
create_tables_hospital >> end_operator