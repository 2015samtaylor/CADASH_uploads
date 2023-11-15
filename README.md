# CADASH Data Processing

This script retrieves and processes California Dashboard (CADASH) data for various subjects, such as ELA, Math, Chronic Absenteeism, Graduation Rates, and Suspensions. It filters the data based on specific criteria, sends the processed data to a SQL database, and logs the process details.

As of 2022 files
ELA has 19 schools
Math has 19 schools
Chronic Absenteeism has 9 schools
Graduation has 11 schools
Suspension has 19 schools

## Prerequisites
- Python (3.x)
- Pipenv

Before running the script, install Pipenv using:
```bash
pip install pipenv
```
Create a virtual environment and install dependencies:
```bash
pipenv install
```
Activate the virtual environment:
```bash
pipenv shell
```

## Usage
1. Run the script to fetch and process CADASH data for different subjects:
   ```bash
   python CADASH_upload.py
   ```

2. The processed data is sent to a SQL database with relevant table names (`CADash_ELA`, `CADash_Math`, etc.).

3. Check the log file (`CADASH_logging.log`) for detailed information about the process.

Note: Locke College Preparatory Academy is excluded from the Chronic Absenteeism data.

## Logging
A log file (`CADASH_logging.log`) is generated, providing a detailed history of the script's execution.

## Author
- Sam Taylor
