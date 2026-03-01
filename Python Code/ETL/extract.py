import pandas as pd
import numpy as np


def read_data (file_path=None,sheet_name=None,):
     

    df=pd.read_excel(file_path,sheet_name=sheet_name)
    return df


 