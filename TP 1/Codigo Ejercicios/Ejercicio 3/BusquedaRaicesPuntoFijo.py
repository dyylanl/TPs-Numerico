import math
import numpy as np

# g(x) se calcula "a mano" usando que f(x) = g(x) - x

def busqueda_raiz_punto_fijo(semillaPorBiseccion, cota, funcF, funcG):
    dato_viejo = semillaPorBiseccion
    dato = funcG(dato_viejo)
    iteracion = 1
    while not abs(dato - dato_viejo) <= cota:
        iteracion += 1
        dato_viejo= dato
        dato = funcG(dato_viejo)
    print("Iteraciones (punto fijo): " + str(iteracion))
    return (dato, abs(dato - dato_viejo))


#res = busqueda_raiz_punto_fijo(aproximacion_biseccion[0], 0.001)
#res = busqueda_raiz_punto_fijo(semillaPuntoFijo, cota, funcionFParaPuntoFijo,funcionGParaPuntoFijo)

#print(res)
