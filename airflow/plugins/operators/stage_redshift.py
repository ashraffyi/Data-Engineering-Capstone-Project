from airflow.hooks.postgres_hook import PostgresHook
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable
from airflow.hooks.S3_hook import S3Hook
from airflow.models import Variable
from helpers import SqlQueries
import airflow.macros
import datetime

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = 'redshift',
                 aws_conn_id = 'aws_credentials',
                 table = '',
                 option ='',
                 delimiter=',',
                 ignore_headers=1,
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id =redshift_conn_id
        self.aws_conn_id = aws_conn_id
        self.table = table
        self.option = option
        self.copy_format = 'csv'
        self.ignore_headers = ignore_headers
        self.delimiter = delimiter

    def execute(self, context):
        ## AWS setup
        aws_hook = AwsHook(self.aws_conn_id)
        credentials = aws_hook.get_credentials()
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        format_type = "IGNOREHEADER 1 delimiter ',' CSV"

        if self.option == "cases":
            file_name = str(context['execution_date'].strftime("%m-%d-%Y")) + ".csv"
            bucket = 'sahussain-covid-data'
            prefix = 'csse_covid_19_data/csse_covid_19_daily_reports_us/'
            temp_rendered_key = prefix + file_name
            rendered_key = temp_rendered_key.format(**context)
            s3_path = "s3://{}/{}".format(bucket, rendered_key)
            self.log.info(f'Preparing to stage data from {s3_path} to {self.table} table')
            copy_sql = SqlQueries.copy_sql.format(
                self.table,
                s3_path,
                credentials.access_key,
                credentials.secret_key
            )
            self.log.info(f'running sql {copy_sql}')
            redshift_hook.run(copy_sql)
            self.log.info(f'Copy successful to stage data from {s3_path} to {self.table} table')
        elif self.option == "hospital":
            bucket = 'sahussain-covid-data'
            prefix = 'usa-hospital-beds/dataset/usa-hospital-beds.csv'
            rendered_key = prefix.format(**context)
            s3_path = "s3://{}/{}".format(bucket, rendered_key)
            self.log.info(f'Preparing to stage data from {s3_path} to {self.table} table')
            copy_sql = SqlQueries.copy_sql.format(
                self.table,
                s3_path,
                credentials.access_key,
                credentials.secret_key,
                self.ignore_headers,
                self.delimiter
            )
            self.log.info(f'Coping data from {s3_path} to {self.table} table')
            redshift_hook.run(copy_sql)
            self.log.info(f'Copy successful to stage data from {s3_path} to {self.table} table')
        elif self.option == "masternode":
            bucket = 'sahussain-covid-data'
            prefix = 'csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
            rendered_key = prefix.format(**context)
            s3_path = "s3://{}/{}".format(bucket, rendered_key)
            self.log.info(f'Preparing to stage data from {s3_path} to {self.table} table')
            copy_sql = SqlQueries.copy_sql.format(
                self.table,
                s3_path,
                credentials.access_key,
                credentials.secret_key,
                self.ignore_headers,
                self.delimiter
            )
            self.log.info(f'Coping data from {s3_path} to {self.table} table')
            redshift_hook.run(copy_sql)
            self.log.info(f'Copy successful to stage data from {s3_path} to {self.table} table')
        else:
            self.log.info('StageToRedshiftOperator nothing to import')
        self.log.info(f'Copy successful of all s3_bucket')




