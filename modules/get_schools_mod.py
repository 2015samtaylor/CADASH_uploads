import pandas as pd
from datetime import date
import logging

#if using this func, must use .str[7:] on the cds column
def full_cds_code(df, column, table):

    school_ids = {'CHA': '0136119',
                    'ING': '1996586',
                    'LEA': '1996313',
                    'DLH': '0101675',
                    'SLA': '0102434',
                    'VEN': '0106831',
                    'BRW': '0106849',
                    'BUN': '0111575',
                    'ROB': '0111583',
                    'LCK': '0118588',
                    'JMS': '0122481',
                    'WMS': '0122499',
                    'AEO': '0123992',
                    'LGC': '0124016',
                    'MAE': '0129270',
                    'FLO': '0134023',
                    'WAT': '0111625',
                    'JAM': '0124008',
                    'CMP': '0137984'}
                
    # Create a list of school_ids values
    school_ids_values = list(school_ids.values())

    # Search for rows in the DataFrame where the 'school_id' column matches any of the values
    GD = df[df[column].isin(school_ids_values)]

    GD = GD.fillna('')
    GD = GD.replace('*', '')

    school_len = len(GD['cds'].unique())

    logging.info(f'{school_len} schools filtered for {table}')

    return(GD)

