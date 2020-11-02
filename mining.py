import pandas as pd

df = pd.read_csv("../../../domi2020.csv", sep=";",dtype={"DTOBITO": "string"}, low_memory=False)

df = df[["DTOBITO", "IDADE", "SEXO", "RACACOR", "CAUSABAS", "CIRCOBITO", "CAUSABAS_O"]]
df = df.query("IDADE > 400 and IDADE != 999")
df["DTOBITO"] = pd.to_datetime(df["DTOBITO"], format="%d%m%Y").dt.strftime("%d/%m/%Y")  # 01/01/2020-17/05/2020
df.to_csv("../../../sim2020_filtrado.csv")
df = df.query("CIRCOBITO == 2.0").groupby("SEXO").count()
print(df)