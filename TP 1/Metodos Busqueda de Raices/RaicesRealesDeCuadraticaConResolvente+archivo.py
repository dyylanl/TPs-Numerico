import math
import sys
import numpy  as np

print('Calculo raices ecuacion cuadratica utilizando formula resolvente')
print('\nIngrese los valores ax^2 + bx +c:')

archivo = open('pruebaRaices.txt','a')

a = np.float32(input("a: "))
b = np.float32(input('b: '))
c = np.float32(input('c: '))

print('\n', file=(archivo))
print('a=', a, file=(archivo), end='   ')
print('b=', b, file=(archivo), end='   ')
print('c=', c, file=(archivo))


discriminante = np.float32(b**2 - 4*a*c)

if discriminante < 0:
    print('\nLas raices son complejas. Ingrese nuevos valores de a,b y c.')
    sys.exit()
    
if (discriminante == 0):
    raizDoble = np.float32((-b)/(2*a))
    print('\nRaiz doble:', raizDoble)
    sys.exit()
    
raiz1 = np.float32((-b + math.sqrt(discriminante))/(2*a))
raiz2 = np.float32((-b - math.sqrt(discriminante))/(2*a))

print('\nRaiz1=', raiz1, file=(archivo))
print('Raiz2=', raiz2, file=(archivo), end='\n')

print('\nLas raices son:')

print('\nRaiz 1:',raiz1)
print('Raiz 2:',raiz2)



archivo.close()