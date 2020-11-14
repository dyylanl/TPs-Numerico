import math
import sys
import numpy as np

print('\nIngrese los valores ax^2 + bx +c:')

#el np.int32 es para restringir a 32 bits 

a = np.int32(input("a: "))
b = np.int32(input('b: '))
c = np.int32(input('c: '))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print('Las raices son complejas. Ingrese nuevos valores de a,b y c.')
    sys.exit()
    
raiz1 = (-b + math.sqrt(discriminante))/(2*a)
raiz2 = (-b - math.sqrt(discriminante))/(2*a)

print('\nLas raices son:')

print('\nRaiz 1:',raiz1)
print('Raiz 2:',raiz2)
