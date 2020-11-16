import math
import numpy as np


def f(x):
    return math.cos(x) -x

def busqueda_raiz(inicio, fin, epsilon, func):
    N = math.ceil(np.log2((fin-inicio)/epsilon))
    print("Iteraciones: " + str(N))
    return busqueda_raiz_rec(inicio, fin, N, func)
    

   
def busqueda_raiz_rec(inicio, fin, N, func):
    medio = (inicio+fin)/2
    if (func(medio) == 0 or N <= 1):
        return (medio, (fin-inicio)/2)
    
    if (func(medio) * func(inicio) > 0):
        return busqueda_raiz_rec(medio, fin, N-1, func)
    
    else:    # (f(medio) * f(inicio) < 0):
        return busqueda_raiz_rec(inicio, medio, N-1, func)

