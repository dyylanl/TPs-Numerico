import math
import sympy as sym
import numpy as np


# Este metodo solo se usa si f'(p) != 0 (siendo p la raiz de la funcion f)
# (Solo para funciones con raices simples)
# En el caso que f'(p) == 0, usar metodo de Newton para raices multiples
def f(x):
    return x**2 -1

def busqueda_raiz_newton(funcion, semilla, error, paso_a_paso=False, iteracionesForzadas = None):
    x= sym.Symbol('x')
    sucesion = sym.simplify( x - (funcion / sym.diff(funcion)) )
    dato_viejo = semilla
    dato = sucesion.subs(x, dato_viejo)
    iteraciones = 1
    #si hago más de 50 iteraciones no va a funcionar esto
    historia = np.zeros((50, 3))
    
    if (iteracionesForzadas == None):
        while not (abs(dato - dato_viejo) <= error):
            historia[iteraciones - 1] = (iteraciones, dato, abs(dato-dato_viejo))
            iteraciones+=1
            if paso_a_paso:
                mostrar_informacion(dato, abs(dato-dato_viejo), iteraciones)
            dato_viejo = dato
            dato = sucesion.subs(x, dato_viejo)
            
    else:
        while(iteraciones < iteracionesForzadas):
            historia[iteraciones - 1] = (iteraciones, dato, abs(dato-dato_viejo))
            iteraciones+=1
            if paso_a_paso:
                mostrar_informacion(dato, abs(dato-dato_viejo), iteraciones)
            dato_viejo = dato
            dato = sucesion.subs(x, dato_viejo)
    
    historia[iteraciones - 1] = (iteraciones, dato, abs(dato-dato_viejo))
    historia = historia [:iteraciones]
    
    return (dato, abs(dato- dato_viejo), iteraciones, historia)

def mostrar_informacion(valor, error, iteracion):
    print("Iteracion: " + str(iteracion))
    print("Valor: "+ str(valor))
    input("Error actual: "+ str(error))
    print("--")
    
def mostrar_resultados(resultados):
    
    print("RESULTADOS:")
    
    print("Iteraciones: "+ str(resultados[2]))
    print("Raiz aproximada: "+ str(resultados[0]))
    print("Error: " + str(resultados[1]))

