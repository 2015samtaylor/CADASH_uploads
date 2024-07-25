import logging
logging.basicConfig(filename='CADASH_logging.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)

import pandas as pd
from datetime import date
from modules import get_schools_mod
from modules import send_to_sql_mod
today = date.today().strftime("%m/%d/%Y")
logging.info('\n\nNew logging instance')


def get_subject(year, subject, table):
    year_string = year[5:]
    # print(f'https://www3.cde.ca.gov/researchfiles/cadashboard/{subject+year_string}.txt')
    df = pd.read_table(f'https://www3.cde.ca.gov/researchfiles/cadashboard/{subject+year_string}.txt', encoding='latin1')
    df['cds'] = df['cds'].astype(str)
    df['cds'] = df['cds'].str[7:]
    df['cds'] = df['cds'].astype(str).str.lstrip('0')
    df['reportingyear'] = year
    df = get_schools_mod.full_cds_code(df, 'cds', table)
    get_schools_mod.confirm_GD_schools(df, table, year)

    #Exception to drop LCK from chronic download file
    if subject == 'chronicdownload':
        df = df.loc[df['schoolname'] != 'Alain Leroy Locke College Preparatory Academy']
    else:
        pass

    #query dtypes from 90 server and send to sql
    dtypes_, col_names = send_to_sql_mod.get_dtypes('SingleSource', table)

    df['last_update'] = today

    #insert missing columns, and get correct ordering
    df = get_schools_mod.insert_missing_cols(df, col_names, table)

    send_to_sql_mod.send(GD, table, dtypes_)

    return(df)
   

GD_ela= get_subject('2021-2022', 'eladownload', 'CADash_ELA')    #19 schools
GD_math = get_subject('2021-2022', 'mathdownload', 'CADash_Math')  #19 schools
GD_absenteeism = get_subject('2021-2022', 'chronicdownload', 'CADash_Chronic')  #8 schools
GD_grad = get_subject('2021-2022', 'graddownload', 'CADash_Grad')      #11 schools
GD_susp = get_subject('2021-2022', 'suspdownload', 'CADash_Suspension')        #19 schools

GD_ela = get_subject('2022-2023', 'eladownload', 'CADash_ELA')    #18 schools
GD_math = get_subject('2022-2023', 'mathdownload', 'CADash_Math')  #18 schools
GD_absenteeism  = get_subject('2022-2023', 'chronicdownload', 'CADash_Chronic')  #7 schools
GD_grad = get_subject('2022-2023', 'graddownload', 'CADash_Grad')      #11 schools
GD_susp = get_subject('2022-2023', 'suspdownload', 'CADash_Suspension')        #18 schools
logging.info('Process complete')

#Locke is dropped from GD_absenteeism. 
#Comp Schools include districtname of 'State of California'
# & countyname of Los Angeles
#cds column should be changed to SchoolCode