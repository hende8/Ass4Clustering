import pandas as pd
import xlrd

data = pd.read_excel("C:\\Users\\HEN\\Downloads\\Data.xlsx",header=0)
data.to_csv("C:\\Users\\HEN\\Downloads\\Data.csv", index=False, quotechar="'")
df = pd.read_csv("C:\\Users\\HEN\\Downloads\\Data.csv")
# print(df)
for col in list(df):
    if(col=='country'):continue
    df[col].fillna(df[col].mean(), inplace=True)

print(df.head(10))

# c = d6tstack.convert_xls.XLStoCSVMultiSheet('C:\\Users\\HEN\\Downloads\\Data.xlsx')
# c.convert_all() # ['multisheet-Sheet1.csv','multisheet-Sheet2.csv']
# print(c)


# xls = xlrd.open_workbook('C:\\Users\\HEN\\Downloads\\Data.xlsx', on_demand=True)
# df = pd.read_excel("C:\\Users\\HEN\\Downloads\\Data.xlsx", sheet_name=xls.sheet_names())
#
# print(df.columns)

# print whole sheet data
# print(df)