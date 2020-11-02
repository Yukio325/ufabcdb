import pandas as pd

racas = {
    "1.0": "branca",
    "2.0": "preta",
    "3.0": "amarela",
    "4.0": "parda",
    "5.0": "indigena",
    "0": "0"
}

df = pd.read_csv("sim2020_filtrado.csv", dtype={"DTOBITO": "string", "SEXO": "string", "RACACOR": "string"},
                 low_memory=False)
df["DTOBITO"] = df["DTOBITO"].str.zfill(8)
df["DTOBITO"] = pd.to_datetime(df["DTOBITO"], format="%d%m%Y").dt.strftime("%d/%m/%Y")
df = df.query("IDADE > 400 and IDADE != 999")
df["IDADE"] = [(age-400.0) for age in df["IDADE"]]
df["SEXO"] = ["male" if sex == "1" else "female" for sex in df["SEXO"]]
df["RACACOR"] = df["RACACOR"].fillna("0")
df["RACACOR"] = [racas[ind] for ind in df["RACACOR"]]
df = df.query("CIRCOBITO == 2.0")
df = df[["DTOBITO", "IDADE", "SEXO", "RACACOR", "CAUSABAS"]]
df.to_csv("sim2020_scd.csv", index=False)
# 01/01/2020-31/08/2020
print(df)
