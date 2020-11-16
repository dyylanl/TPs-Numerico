import math

#ingresar en esta parte la funcion f(x)
def f(x):
    return(4**8)*x**2-(6**6)*x + 1


#utilizamos biseccion para buscar dos semillas de inicio
def biseccion(a,b):
        p = (a + b)/2        
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p    
        return p


def metodoSecante(a,b,tolerancia,numMaxIteraciones):
    step = 1
    condition = True
    while condition:
        if f(a) == f(b):
            print('Error de division por cero')
            break
        x2 = a - (b-a)*f(a)/( f(b) - f(a) ) 
        print('\nNumero Iteracion: %d | p = %0.6f | f(p) = %0.6f' % (step, x2, f(x2)))
        a = b
        b = x2
        step = step + 1
        
        if step > numMaxIteraciones:
            print('No Converge')
            break
        
        condition = abs(f(x2)) > tolerancia
    print('\n Aproximacion raiz: %0.8f' % x2)
    print('\n Tolerancia utilizada:',tolerancia)


a = float(input('Ingrese valor de a: '))
b = float(input('Ingrese valor de b: '))

#Descomentar esto para agregar los valores de tolerancia y
#limite de iteraciones por consola 

#tolerancia = float(input('Ingrese tolerancia:'))
#numMaxIteraciones = int(input('Ingrese numero maximo de iteraciones: '))

tolerancia = 0.00001
numMaxIteraciones = 15

#utilizo biseccion para obtener 2 semillas segun el intervalo 
# [a,b] ingresado

semilla1 = biseccion(a,b)

if f(a) * f(semilla1) < 0:
    semilla2 = biseccion(a,semilla1)
else:
    semilla2 = biseccion(semilla1,b)
       


metodoSecante(semilla1,semilla2,tolerancia,numMaxIteraciones)
