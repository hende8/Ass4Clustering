import pandas as pd
import numpy as np
import xlrd as xl

from pandas import ExcelWriter
from pandas import ExcelFile


# def preprocessing(data):
df = pd.read_excel("C:\\Users\\shira\\Desktop\\shiran\\Dataset.xlsx", sheet_name=None)
# df = pd.DataFrame(data)
# print(data)
# data = xl.open_workbook("C:\\Users\\shira\\Desktop\\shiran\\Dataset.xlsx",  on_demand=True)
# df = pd.read_excel("C:\\Users\\shira\\Desktop\\shiran\\Dataset.xlsx", sheet_name=data.sheet_names())
# df = pd.DataFrame(df2)
# print(df)
for col in df:
    print(col)
    df[col].fillna((df[col].mean()), inplace=True)

# xls = xlrd.open_workbook('C:\\Users\\HEN\\Downloads\\Data.xlsx', on_demand=True)
# df = pd.read_excel("C:\\Users\\HEN\\Downloads\\Data.xlsx", sheet_name=xls.sheet_names())

