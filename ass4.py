import pandas as pd
from sklearn.preprocessing import StandardScaler

def preProcessingData(link):
    data = pd.read_excel(link,header=0)
    urlArray= link.split("\\")
    urlArray.pop(len(urlArray)-1)
    url=""
    for partLink in urlArray:
        url+=partLink+"\\"
    data.to_csv(url+"Data.csv", index=False, quotechar="'")
    df = pd.read_csv(url+"Data.csv")

    #completing missing values in mean
    for col in list(df):
        if(col=='country'):continue
        data[col].fillna(data[col].mean(), inplace=True)

    #normalized by Standardization
    standartscalar= StandardScaler()
    df_scaled = pd.DataFrame(standartscalar.fit_transform(df.iloc[:,2:]),columns = df.columns[2:])

    #join columns 'country' and 'year' to one dataframe
    new = df[['country', 'year']].copy()
    finalStandard = new.join(df_scaled)

    #group by country
    finalDf = finalStandard.groupby('country').mean()

    return finalDf

print(preProcessingData("C:\\Users\\shira\\Desktop\\shiran\\Dataset.xlsx"))