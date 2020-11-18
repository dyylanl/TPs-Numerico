import math
import sympy as sym


def busqueda_raiz_secante(funcion, semilla1, semilla2, error, paso_a_paso=False):
    x= sym.Symbol('x')
    y= sym.Symbol('y')
    dato_viejo1 = semilla1
    dato_viejo2 = semilla2
    dato =  dato_viejo1 - (((funcion.subs(x,dato_viejo1)) * (dato_viejo1 - dato_viejo2))/ ((funcion.subs(x, dato_viejo1)) - funcion.subs(x, dato_viejo2) ) )
    iteraciones = 1
    
    while not (abs(dato - dato_viejo1) <= error):
        iteraciones+=1
        if paso_a_paso:
             mostrar_informacion(dato, abs(dato-dato_viejo1), iteraciones)
        dato_viejo2= dato_viejo1
        dato_viejo1 = dato
        dato = dato_viejo1 - (((funcion.subs(x,dato_viejo1)) * (dato_viejo1 - dato_viejo2))/ ((funcion.subs(x, dato_viejo1)) - funcion.subs(x, dato_viejo2) ) )
     
    return (dato, abs(dato- dato_viejo1), iteraciones)

def mostrar_informacion(valor, error, iteracion):
    print("Iteracion: " + str(iteracion))
    print("Valor: "+ str(valor))
    input("Error actual: "+ str(error))
    print("--")
    
def mostrar_resultados(resultados):
    
    print("RESULTADOS:")
    
    print("Iteraciones: "+ str(resultados[2]))
    print("Raiz aproximada: "+ str(resultados))