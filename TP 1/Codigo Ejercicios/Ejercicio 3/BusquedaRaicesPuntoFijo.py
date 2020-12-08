import math
import numpy as np

# g(x) se calcula "a mano" usando que f(x) = g(x) - x

def busqueda_raiz_punto_fijo(semillaPorBiseccion, cota, funcG, cantMaxIteraciones):
    iteraciones = 1
    historia = np.zeros((cantMaxIteraciones, 3))
    dato_viejo = semillaPorBiseccion
    dato = funcG(dato_viejo)
    while (abs(dato - dato_viejo) > cota):
        if (iteraciones == cantMaxIteraciones):
            print("se supero la cantidad maxima de iteraciones")
            break
        else:
            historia[iteraciones - 1] = (iteraciones, dato, abs(dato - dato_viejo) )
            iteraciones += 1
            dato_viejo = dato
            dato = funcG(dato_viejo)
 #           print("Iteraciones (punto fijo): " + str(iteraciones) + "RAIZ: " + str(dato))
#    print(f'Raiz: {dato}\nCantidad de iteraciones: {iteraciones}')
    historia[iteraciones - 1] = (iteraciones, dato, abs(dato - dato_viejo) )
    historia = historia[:iteraciones]
    return (dato, abs(dato - dato_viejo), iteraciones, historia)
