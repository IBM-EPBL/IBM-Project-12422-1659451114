import pandas as pd
data = pd.read_excel('C:\Temp\Sample Dataset.xlsx')
#print(data)
data.drop_duplicates()
NewData = data.dropna(how='all', inplace=True)