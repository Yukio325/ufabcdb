import pandas as pd

total_suicid = 0

for chunk in pd.read_csv("../../../sim2019.csv", sep=";",dtype={"DTOBITO": "string"}, chunksize=10000):
    chunk = chunk[["DTOBITO", "IDADE", "SEXO", "RACACOR", "CAUSABAS", "CIRCOBITO", "CAUSABAS_O"]]
    df = chunk.query("CIRCOBITO == 2.0").count()
    total_suicid += df.loc["DTOBITO"]
    #print(df)
    print(chunk)
#df = pd.read_csv("../../../sim2019.csv", sep=";",dtype={"DTOBITO": "string"}, nrows=10000)
print(total_suicid)
'''df = df[["DTOBITO", "IDADE", "SEXO", "RACACOR", "CAUSABAS", "CIRCOBITO", "CAUSABAS_O"]]
df = df.dropna().query("IDADE > 400 and IDADE != 999")
df["DTOBITO"] = pd.to_datetime(df["DTOBITO"], format="%d%m%Y").dt.strftime("%d/%m/%Y")  # 01/01/2020-17/05/2020
df = df.query("CIRCOBITO == 2.0").groupby("SEXO").count()
print(df)'''
