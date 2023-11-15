"""
Module: get_schools_mod

This module provides a function for filtering a DataFrame based on a specified column containing California Department of Education (CDE) school codes. The filtering is done using a predefined dictionary of Green Dot school codes for our specific schools.

Functions:
    - full_cds_code(df, column, table):
        Filters a DataFrame based on the values in a specified column containing CDE school codes.
        
        Parameters:
            - df (DataFrame): The input DataFrame to be filtered.
            - column (str): The name of the column containing CDE school codes.
            - table (str): A string identifier for the table or dataset being filtered.

        Returns:
            - DataFrame: A new DataFrame containing rows where the specified column's values match predefined school codes.
            
      

"""
Module: send_to_sql_mod

This module facilitates the transfer of data between a SQL Server database and a Pandas DataFrame. It provides functions for executing SQL queries and sending Pandas DataFrames to a SQL Server table.

Functions:
    - SQL_query_90(query):
        Executes a SQL query using an ODBC connection named 'GD_DW' and returns the result as a Pandas DataFrame.

        Parameters:
            - query (str): The SQL query to be executed.

        Returns:
            - DataFrame: Result of the SQL query as a Pandas DataFrame.

    - get_dtypes(db, table_name):
        Retrieves the data types of columns in a specified SQL Server table and returns a dictionary suitable for specifying dtypes in Pandas.

        Parameters:
            - db (str): The database name.
            - table_name (str): The name of the SQL Server table.

        Returns:
            - dict: A dictionary containing column names and corresponding SQLAlchemy data types.

    - send(frame, table, dtypes_):
        Sends a Pandas DataFrame to a specified SQL Server table using SQLAlchemy. Logs success or failure.

        Parameters:
            - frame (DataFrame): The Pandas DataFrame to be sent.
            - table (str): The name of the SQL Server table.
            - dtypes_ (dict): Dictionary containing column names and corresponding SQLAlchemy data types.






