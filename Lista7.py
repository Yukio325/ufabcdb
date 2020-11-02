import pandas as pd
'''
# Ex. 1
def media_colunas(df, *args):
    mean = [df[col].mean() for col in args]
    val = []
    for mn in mean:
        if mn>6.8:
            val.append(mn)
    if len(val) == 1:
        return mean, f"Apenas Media {val[0]} eh maior que 6.8"
    if len(val) == 2:
        return mean, "As duas Medias sao maiores que 6.8"
    if len(val) == 0:
        return mean, "Nenhuma media eh maior que 6.8"

df = pd.read_csv("fake-classrooms30.csv")
col_1, col_2 = [input(), input()]
[m1, m2], txt = media_colunas(df, col_1, col_2)
print("Media %s = %.2f\nMedia %s = %.2f\n%s" % (col_1, m1, col_2, m2, txt))

# Ex. 2
def result_aluno(df, indice_aluno):
    nome, prova1, prova2, trabalho = df[["Nome", "Prova 1", "Prova 2", "Trabalho"]].loc[indice_aluno]
    mean = (prova1+prova2+trabalho)/3
    if mean>6.4:
        result = "Aprovado"
    else:
        result = "Reprovado"
    return print("Nome: %s\nProva 1: %.1f\nProva 2: %.1f\nTrabalho: %.1f\nMedia: %.2f\nResultado: %s"
                 % (nome, prova1, prova2, trabalho, mean, result))

df = pd.read_csv("fake-classrooms12.csv")
result_aluno(df, int(input()))
'''
# Ex. 3
import numpy as np
df = pd.read_csv("fake-classrooms-correl03.csv")
a, b = np.polyfit(x=df["Horas Estudo"], y=df["Nota Final"], deg=1)
print(df["Horas Estudo"].corr(df["Nota Final"]))
print("y = %.2fx + %.2f" % (a,b))
print("%.2f" % (a*8+b))

