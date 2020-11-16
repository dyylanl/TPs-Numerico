import math
import numpy as np

# g(x) se calcula "a mano" usando que f(x) = g(x) - x




def g(x):
    return math.cos(x)

def f(x):
    return g(x) -x


# BusquedaRaicesBiseccion aproxima a la raiz de f(x) con un error epsilon.
def busqueda_raiz_biseccion(inicio, fin, epsilon):
    N = math.ceil(np.log2((fin-inicio)/epsilon))
    print("Iteraciones (biseccion): " + str(N))
    return busqueda_raiz_rec(inicio, fin, N)
    

   
def busqueda_raiz_rec(inicio, fin, N):
    medio = (inicio+fin)/2
    if (f(medio) == 0 or N <= 1):
        return (medio, (fin-inicio)/2)
    
    if (f(medio) * f(inicio) > 0):
        return busqueda_raiz_rec(medio, fin, N-1)
    
    else:    # (f(medio) * f(inicio) < 0):
        return busqueda_raiz_rec(inicio, medio, N-1)


# La semilla se calcula usando BusquedaRaicesBiseccion, el error es el pedido.
def busqueda_raiz_punto_fijo(semilla, error):
    dato_viejo = semilla
    dato = g(dato_viejo)
    iteracion = 1
    while not abs(dato - dato_viejo) <= error:
        iteracion += 1
        dato_viejo= dato
        dato = g(dato_viejo)
    print("Iteraciones (punto fijo): " + str(iteracion))
    return (dato, abs(dato - dato_viejo))


aproximacion_biseccion = busqueda_raiz_biseccion(0, math.pi/2.0, 0.01)
print(aproximacion_biseccion)

res= busqueda_raiz_punto_fijo(aproximacion_biseccion[0], 0.001)

print(res)
