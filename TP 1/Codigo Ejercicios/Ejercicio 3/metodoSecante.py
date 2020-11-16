import math

#ingresar en esta parte la funcion f(x)
def f(x):
    return math.exp(x)-x**3 + math.log(x,math.exp(1)) + math.sin(x)

#utilizamos biseccion para buscar dos semillas de inicio
def biseccion(a,b,tolerancia):
    n = math.ceil(math.log(b-a,2)-math.log(tolerancia,2)) #saco con teorema cantidad de iteraciones
    while (n!=0):
        p = (a + b)/2        
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p     
        n = n - 1
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

semilla1 = biseccion(a,b,tolerancia)

if f(a) * f(semilla1) < 0:
    semilla2 = biseccion(a,semilla1,tolerancia)
else:
    semilla2 = biseccion(semilla1,b,tolerancia)
       


metodoSecante(semilla1,semilla2,tolerancia,numMaxIteraciones)