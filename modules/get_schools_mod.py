import pandas as pd
from datetime import date
import logging
import re

school_ids = {'CHA': '136119',
                'ING': '1996586',
                'LEA': '1996313',
                'DLH': '101675',
                'SLA': '102434',
                'VEN': '106831',
                'BRW': '106849',
                'BUN': '111575',
                'ROB': '111583',
                'LCK': '118588',
                'JMS': '122481',
                'WMS': '122499',
                'AEO': '123992',
                'LGC': '124016',
                'MAE': '129270',
                'FLO': '134023',
                'WAT': '111625',
                'JAM': '124008',
                'CMP': '137984'}

#if using this func, must use .str[7:] on the cds column
def full_cds_code(df, column, table):
                
    # Create a list of school_ids values
    school_ids_values = list(school_ids.values())

    # Search for rows in the DataFrame where the 'school_id' column matches any of the values, or LA Angeles School District, 

    df = df[(df['districtname'].str.contains('State of California', case=False)) | 
            (df['countyname'].str.contains('Los Angeles', case=False)) | 
            (df[column]).isin(school_ids_values)]

    df = df.fillna('')
    df = df.replace('*', '')

    school_len = len(df['cds'].unique())

    logging.info(f'{school_len} schools filtered for {table}')

    return(df)


def insert_missing_cols(frame, col_names, table):
    
    try:
        # Attempt to access the specified columns
        subset_df = frame[col_names]
    except KeyError as e:
        try:
            # Extract the missing column names using regular expression
            missing_cols_str = re.search(r"\['(.*?)'\]", str(e)).group(1)
            missing_cols = [col.strip() for col in missing_cols_str.split(',')]
            missing_cols = [item.strip("'") for item in missing_cols]

            # Insert missing columns
            for col_name in missing_cols:
                if col_name not in frame.columns:
                    print(f'{col_name} inserted as blank for {table}')
                    logging.info(f'{col_name} inserted as blank for {table}')
                    frame[col_name] = pd.Series(dtype='object')  # Insert blank columns with dtype 'object' or the appropriate dtype

            try:
                # Attempt to access the specified columns again
                subset_df = frame[col_names]
            except KeyError as e:
                print(f"First exception raised Error: {e}")
                # Optionally, raise the exception again if you want to propagate the error
                # raise
        except AttributeError as ae:
            print(f"Send exception raised Error: {ae}")
            # Optionally, raise the exception again if you want to propagate the error
            # raise

    return(subset_df)
                        

def confirm_GD_schools(frame, table, year):
                
    # Create a list of school_ids values
    school_ids_values = list(school_ids.values())

    num_unique = frame.loc[frame['cds'].isin(school_ids_values)]['cds'].nunique()

    logging.info(f'\n\n{num_unique} Green Dot Schools Present in {table} for {year}')
    print(f'{num_unique} Green Dot Schools Present in {table} for {year}')


