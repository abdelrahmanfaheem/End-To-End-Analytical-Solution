
from CreateTable.database_connection.connection import get_connection


from Exceptions_Files.CustomException import *

def send_data(df, column_type=None,batch_size=1000,table_name=None,database=None):
    try:
        print ("Start establish Connection ")
        engine = get_connection(database)
        print(f"Engine is open: {engine}")
        print("Start uploading data...")

        print (f" the  Data frame Size is {len(df)}")

        df.to_sql(
                name=table_name,
                con=engine,
                if_exists='append',
                chunksize=1000,
                dtype=column_type,
                index=False
                # method="multi",
            )
         
        # for start in range (0,len(df),batch_size):

        #     df.iloc[start :start+batch_size].to_sql(
        #         name='HR_Data',
        #         con=engine,
        #         if_exists='append',
        #         # chunksize=1000,
        #         dtype=column_type,
        #         # method="multi"
        #     )

        #     print (f"{start+batch_size} now is upload")

        print("Data uploaded successfully!")
    except Exception as e:
        # Wrap any error in your custom exception and print JSON
        exc = Custom_Exception(e)
        print("Error (JSON):", exc.to_json())
