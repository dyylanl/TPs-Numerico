import numpy as np
import sys

print('\n Ingrese los valores ax^2 + bx +c:')

a = np.float32(input("a: "))
b = np.float32(input('b: '))
c = np.float32(input('c: '))

def sgn(b):
    if b < 0:
        return -1
    else:
        return 1

discriminante = np.float32(b**2-4*a*c)

if discriminante == 0:
    print('\nRaiz doble:',np.float32((-b)/2*a))
    sys.exit()
    
if discriminante < 0:
    print('\nLas raices no son reales.')
    sys.exit()


x1 = np.float32(-(b + sgn(b)*np.sqrt(discriminante))/(2*a))
x2 = np.float32(c/(a*x1))

    
print('\nLas raices son:\n')
print('Raiz 1:',x1)
print('\nRaiz 2:',x2)



