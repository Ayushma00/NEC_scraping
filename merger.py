import pandas as pd

df1 = pd.read_excel (r'details.xlsx')
print(df1.columns)
df2=pd.read_excel(r'general_info.xlsx')
print(df2.columns)
mergedDf = df2.merge(df1, how='inner', on='Reg. No.')
mergedDf.to_excel (r'final.xlsx', index = False, header=True)
