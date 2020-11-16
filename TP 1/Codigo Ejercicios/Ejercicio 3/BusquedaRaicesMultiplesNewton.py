import math
import sympy as sym



# Este metodo solo se usa si f'(p) == 0 (siendo p la raiz de la funcion f)
# (Solo para funciones con raices multiples)
# En el caso que f'(p) != 0, usar metodo de Newton para raices simples
def f(x):
    return x**3

def busqueda_raiz_newton(funcion, semilla, error, paso_a_paso=False):
    
    # Pn = x- f(x)*f'(x) / [ (f'(x) ^2) - f(x)*f''(x)]
    sucesion = sym.simplify( x - ((funcion*sym.diff(funcion)) / (sym.diff(funcion,x)**2 -funcion * sym.diff(funcion,x,2))) )
    dato_viejo = semilla
    dato = sucesion.subs(x, dato_viejo)
    iteraciones = 1
    
    while not abs( dato - dato_viejo) <= error:
        iteraciones +=1
        if paso_a_paso:
            mostrar_informacion(dato, abs(dato-dato_viejo), iteraciones)
        dato_viejo = dato
        dato = sucesion.subs(x, dato_viejo)
         
     
    return (dato, abs(dato- dato_viejo), iteraciones)


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
        

x= sym.Symbol('x')

# Si se quiere paso a paso, agregar True como parametro al final
resultados = busqueda_raiz_newton(f(x), 1,  0.0001, True)

mostrar_resultados(resultados)
