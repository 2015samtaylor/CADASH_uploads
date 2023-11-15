import pyodbc
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import urllib
import logging


def SQL_query_90(query):
    odbc_name = 'GD_DW'
    conn = pyodbc.connect(f'DSN={odbc_name};')
    df_SQL = pd.read_sql_query(query, con = conn)
    return(df_SQL)


def get_dtypes(db , table_name):

    out = SQL_query_90('''
    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
    FROM {}.information_schema.columns
    WHERE table_name = '{}'
    '''.format(db, table_name))

    dtypes = {}
    
    #gets column name, data type, char length into a dict
    for _, row in out.iterrows():
        column_name = row['COLUMN_NAME']
        data_type = row['DATA_TYPE']
        length = row['CHARACTER_MAXIMUM_LENGTH']
        if data_type == 'varchar' or data_type == 'nvarchar':
            dtypes[column_name] = sqlalchemy.types.VARCHAR(length=int(length))
        elif data_type == 'int':
            dtypes[column_name] = sqlalchemy.types.Integer()
        elif data_type == 'float':
            dtypes[column_name] = sqlalchemy.types.Float()
        elif data_type == 'datetime':
            dtypes[column_name] = sqlalchemy.types.DateTime()
        
    return(dtypes)


def send(frame, table, dtypes_):

    quoted = urllib.parse.quote_plus("Driver={SQL Server Native Client 11.0};"
                     "Server=10.0.0.89;"
                     "Database=DataTeamSandbox;"
                     "Trusted_Connection=yes;")

    engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

    try:
        frame.to_sql(table, schema='dbo', con = engine, if_exists = 'replace', index = False, dtype = dtypes_)
        logging.info(f"Data written to {table} successfully.")

    except Exception as e:
        logging.info(f"Error writing data to {table}: {str(e)}")

   


