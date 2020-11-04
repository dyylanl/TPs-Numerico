import math
import numpy as np


def f(x):
    return math.cos(x) -x

def busqueda_raiz(inicio, fin, epsilon):
    N = math.ceil(np.log2((fin-inicio)/epsilon))
    print("Iteraciones: " + str(N))
    return busqueda_raiz_rec(inicio, fin, N)
    

   
def busqueda_raiz_rec(inicio, fin, N):
    medio = (inicio+fin)/2
    if (f(medio) == 0 or N <= 1):
        return (medio, (fin-inicio)/2)
    
    if (f(medio) * f(inicio) > 0):
        return busqueda_raiz_rec(medio, fin, N-1)
    
    else:    # (f(medio) * f(inicio) < 0):
        return busqueda_raiz_rec(inicio, medio, N-1)


res = busqueda_raiz(0, math.pi/2.0, 0.005)
print("Raiz: "+ str(res[0]) +"; Error: " + str(res[1]))