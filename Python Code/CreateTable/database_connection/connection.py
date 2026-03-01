from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


from Exceptions_Files.CustomException import *


def get_connection(database):

    try:
        print ("Start To get Connection")
        server = r'DESKTOP-HVROBDM\SQLEXPRESS'
        database = database 
        username = 'MyUser'
        password = 'MyUser'

        engine = create_engine(
            f"mssql+pyodbc://{username}:{password}@{server}/{database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )
        # Test the connection immediately
        conn = engine.connect()
        conn.close()
        return engine
    
    
    except Exception as e:
        # Wrap ANY exception in your custom exception
        raise Custom_Exception(e)

