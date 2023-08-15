from utils import mex
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calcular_nim(x,y):
    valores = []
    
    for i in range(x+1):
        valores.append(i^y)

    for j in range(y+1):
        valores.append(x^j)
    
    valores.append(x^y)
        
    return mex(valores)


n = 20

resultado = np.zeros((n,n))


for x in range(n):
    for y in range(n):
        if(x <= y):
            resultado[x][y] = calcular_nim(x+1,y+1)
        else:
            resultado[x][y] = -1


df = pd.DataFrame(resultado)

df.to_excel("resultado.xlsx", index = False)
