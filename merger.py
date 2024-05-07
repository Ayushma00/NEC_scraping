import pandas as pd

df1 = pd.read_excel(r"output/details.xlsx")
df2 = pd.read_excel(r"output/general_info.xlsx")
mergedDf = df2.merge(df1, how="inner", on="Reg. No.")
mergedDf.to_excel(r"output/final.xlsx", index=False, header=True)
