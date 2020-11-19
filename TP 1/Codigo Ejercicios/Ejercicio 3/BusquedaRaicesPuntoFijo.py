import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import matplotlib.pyplot as plt

# g(x) se calcula "a mano" usando que f(x) = g(x) - x

def busqueda_raiz_punto_fijo(semillaPorBiseccion, cota, funcG, cantMaxIteraciones):
    iteraciones = 1
    dato_viejo = semillaPorBiseccion
    dato = funcG(dato_viejo)
    while (abs(dato - dato_viejo) > cota):
        if (iteraciones == cantMaxIteraciones):
            print("se supero la cantidad maxima de iteraciones")
            break
        else:
            iteraciones += 1
            dato_viejo = dato
            dato = funcG(dato_viejo)
            print("Iteraciones (punto fijo): " + str(iteraciones) + "RAIZ: " + str(dato))
    print(f'Raiz: {dato}\nCantidad de iteraciones: {iteraciones}')
    return (dato)
