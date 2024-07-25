import pandas as pd
import logging
import pytest
import os 
import sys

# Adjust the path to make the 'project' directory the root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from modules.get_schools_mod import school_ids

def read_in(year, subject, table):
    year_string = year[5:]
    df = pd.read_table(f'https://www3.cde.ca.gov/researchfiles/cadashboard/{subject+year_string}.txt', encoding='latin1')
    df['cds'] = df['cds'].astype(str)
    df['cds'] = df['cds'].str[7:]
    df['cds'] = df['cds'].astype(str).str.lstrip('0')
    df['reportingyear'] = year
    return df



@pytest.mark.parametrize("year, subject, table", [
    ('2021-2022', 'eladownload', 'CADash_ELA'),
    ('2021-2022', 'mathdownload', 'CADash_Math')
])

def test_GD_schools_in_raw_frame(year, subject, table):
    df = read_in(year, subject, table)
    
    # Ensure school_ids is defined or imported from the relevant module
    school_ids_values = list(school_ids.values())
    
    num_unique = df.loc[df['cds'].isin(school_ids_values)]['cds'].nunique()
    
    assert num_unique == 19, f'Expected 19 unique schools, but found {num_unique} for {table} in {year}'
    
    print(f'{num_unique} Green Dot Schools Present in {table} for {year}')

# Direct call for debugging purposes
