import math
import numpy as np


def f(x):
    return math.cos(x) -x

def busqueda_raiz(inicio, fin, epsilon, func, iteraciones = None):
    N = iteraciones
    if(iteraciones == None):
        N = math.ceil(np.log2((fin-inicio)/epsilon))
    historia = np.zeros((N, 2))
    i = 0
    #print("Iteraciones: " + str(N))
    resultado = busqueda_raiz_rec(inicio, fin, N, func, historia, i)
    resultado[2] = N
    return resultado
    

   
def busqueda_raiz_rec(inicio, fin, N, func, historia, i):
    medio = (inicio+fin)/2
    if (func(medio) == 0 or N <= 1):
        historia = historia[:i]
        return [medio, (fin-inicio)/2, 0, historia]
    
    historia[i] = (i+1, medio)
    i = i + 1
    
    if (func(medio) * func(inicio) > 0):
        return busqueda_raiz_rec(medio, fin, N-1, func, historia, i)
    
    else:    # (f(medio) * f(inicio) < 0):
        return busqueda_raiz_rec(inicio, medio, N-1, func, historia, i)
