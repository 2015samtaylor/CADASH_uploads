import pandas as pd
from modules import get_schools_mod
from modules import send_to_sql_mod
import logging

import importlib
importlib.reload(get_schools_mod)

logging.basicConfig(filename='CADASH_logging.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)
logging.info('\n\nNew logging instance')


def get_subject(year, subject, table):
    year_string = year[5:]
    # print(f'https://www3.cde.ca.gov/researchfiles/cadashboard/{subject+year_string}.txt')
    df = pd.read_table(f'https://www3.cde.ca.gov/researchfiles/cadashboard/{subject+year_string}.txt', encoding='latin1')
    df['cds'] = df['cds'].astype(str)
    df['cds'] = df['cds'].str[7:]
    df['reportingyear'] = year
    GD = get_schools_mod.full_cds_code(df, 'cds', table)

    #Exception to drop LCK from chronic download file
    if subject == 'chronicdownload':
        GD = GD.loc[GD['schoolname'] != 'Alain Leroy Locke College Preparatory Academy']
    else:
        pass

    #query dtypes from 90 server and send to sql
    dtypes_ = send_to_sql_mod.get_dtypes('SingleSource', table)

    send_to_sql_mod.send(GD, table, dtypes_)

    return(GD)

GD_ela = get_subject('2021-2022', 'eladownload', 'CADash_ELA')    #19 schools
GD_math = get_subject('2021-2022', 'mathdownload', 'CADash_Math')  #19 schools
GD_absenteeism = get_subject('2021-2022', 'chronicdownload', 'CADash_Chronic')  #9 schools
GD_grad = get_subject('2021-2022', 'graddownload', 'CADash_Grad')      #11 schools
GD_susp = get_subject('2021-2022', 'suspdownload', 'CADash_Suspension')        #19 schools
logging.info('Process complete')

#Locke is dropped from GD_absenteeism. 