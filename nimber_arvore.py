from utils import mex
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
PARA ÁRVORES COM 2 RAMOS


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
'''

####################################################################


#PARA ÁRVORES COM 3 RAMOS
def calcular_nim(x,y,z):
    valores = []

    for i in range(x+1):
        valores.append(i^y^z)
    
    for j in range(y+1):
        valores.append(x^j^z)
    
    for k in range(z+1):
        valores.append(x^y^k)

    valores.append(x^y^z)
    
    return mex(valores)

n = 10

qtde_ramos = []
resultado = []

'''
for x in range(n):
    for y in range(n):
        for z in range(n):
                if(x <= y and y <= z):
                     qtde_ramos.append((x+1,y+1,z+1))
                     resultado.append(calcular_nim(x+1,y+1,z+1))
'''

#TAMANHO FIXO PARA UM DOS RAMOS
x = 2
for y in range(x,n):
    for z in range(x,n):
        if(y <= z):
            qtde_ramos.append((x+1, y+1, z+1))
            resultado.append(calcular_nim(x+1,y+1,z+1))


for i in range(len(qtde_ramos)):
    print("Para ", qtde_ramos[i], ": ", resultado[i])


df = pd.DataFrame(resultado)

df.to_excel("resultado.xlsx", index = False)