import math
import sympy as sym
import numpy as np


def busqueda_raiz_secante(funcion, semilla1, semilla2, error, paso_a_paso=False, iteracionesForzadas = None):
    x= sym.Symbol('x')
    y= sym.Symbol('y')
    dato_viejo1 = semilla1
    dato_viejo2 = semilla2
    
    #si tiene mas de 50 iteraciones no va a funcionar
    historia = np.zeros((50, 3))
    historia[0] = (0, dato_viejo1, None)
    historia[1] = (1, dato_viejo2, None)
    iteraciones = 2
    
    dato =  dato_viejo1 - (((funcion.subs(x,dato_viejo1)) * (dato_viejo1 - dato_viejo2))/ ((funcion.subs(x, dato_viejo1)) - funcion.subs(x, dato_viejo2) ) )
    if (iteracionesForzadas == None):
        while not (abs(dato - dato_viejo1) <= error):
            historia[iteraciones] = (iteraciones, dato, abs(dato-dato_viejo1))
            iteraciones+=1
            if paso_a_paso:
                mostrar_informacion(dato, abs(dato-dato_viejo1), iteraciones)
            dato_viejo2= dato_viejo1
            dato_viejo1 = dato
            dato = dato_viejo1 - (((funcion.subs(x,dato_viejo1)) * (dato_viejo1 - dato_viejo2))/ ((funcion.subs(x, dato_viejo1)) - funcion.subs(x, dato_viejo2) ))
    else:
        
        while (iteraciones < iteracionesForzadas):
            historia[iteraciones] = (iteraciones, dato, abs(dato-dato_viejo1))
            iteraciones+=1
            if paso_a_paso:
                mostrar_informacion(dato, abs(dato-dato_viejo1), iteraciones)           
            dato_viejo2= dato_viejo1
            dato_viejo1 = dato
            dato = dato_viejo1 - (((funcion.subs(x,dato_viejo1)) * (dato_viejo1 - dato_viejo2))/ ((funcion.subs(x, dato_viejo1)) - funcion.subs(x, dato_viejo2) ))
           
    historia[iteraciones] = (iteraciones, dato, abs(dato-dato_viejo1))
    historia = historia[:iteraciones + 1]
    return (dato, abs(dato- dato_viejo1), iteraciones - 1, historia)

def mostrar_informacion(valor, error, iteracion):
    print("Iteracion: " + str(iteracion))
    print("Valor: "+ str(valor))
    #input("Error actual: "+ str(error))
    print("Error actual: "+ str(error))
    print("--")
    
def mostrar_resultados(resultados):
    
    print("RESULTADOS:")
    
    print("Iteraciones: "+ str(resultados[2]))
    print("Raiz aproximada: "+ str(resultados))