import numpy as np
import sys


print('\n Ingrese los valores ax^2 + bx +c:')

a = np.float32(input("a: "))
b = np.float32(input('b: '))
c = np.float32(input('c: '))

discriminante = b**2-4*a*c

if discriminante == 0:
    print('\nRaiz doble:',np.float32((-b)/2*a))
    sys.exit()
    
if discriminante < 0:
    print('\nLas raices no son reales.')
    sys.exit()
    
if b >= 0:
    raiz1 = np.float32((-b - np.sqrt(discriminante))/(2*a))
    raiz2 = np.float32((2*c)/(-b - np.sqrt(discriminante)))
    
if b < 0:
    raiz1 = np.float32((2*c)/(-b + np.sqrt(discriminante)))
    raiz2 = np.float32((-b + np.sqrt(discriminante))/(2*a))
    
print('\nLas raices son:\n')
print('Raiz 1:',raiz1)
print('\nRaiz 2:',raiz2)


