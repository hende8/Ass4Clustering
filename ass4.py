import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_excel("C:\\Users\\HEN\\Downloads\\Data.xlsx",header=0)
data.to_csv("C:\\Users\\HEN\\Downloads\\Data.csv", index=False, quotechar="'")
df = pd.read_csv("C:\\Users\\HEN\\Downloads\\Data.csv")
# print(df)
def clearna(data):
    for col in list(data):
        if(col=='country'):continue
        data[col].fillna(data[col].mean(), inplace=True)
    return data

df = clearna(df)
standartscalar= StandardScaler()
df_scaled = pd.DataFrame(standartscalar.fit_transform(df.iloc[:,2:]),columns = df.columns[2:])
new = df[['country', 'year']].copy()
finalStandard = new.join(df_scaled)
df3 = finalStandard.groupby('country').mean()

#
# df4 = pd.concat([df.columns[:1], df_scaled.reset_index(drop=True)], axis=1)
# print(df4)

