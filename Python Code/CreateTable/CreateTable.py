import sys
sys.path.append(r"K:\HR Project\Python Code")
 
from CreateTable.models.base import Base

from CreateTable.models.HR_Data_Table import HR_table

from CreateTable.database_connection.connection import get_connection

from Exceptions_Files.CustomException import *


def creat_all_tables () :
    engine=get_connection("HR_Project")

    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    print("All tables created successfully  ")