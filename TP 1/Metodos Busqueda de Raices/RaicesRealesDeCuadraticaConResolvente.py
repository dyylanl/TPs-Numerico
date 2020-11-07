import math
import sys

print('\nIngrese los valores ax^2 + bx +c:')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print('Las raices son complejas. Ingrese nuevos valores de a,b y c.')
    sys.exit()
    
raiz1 = (-b + math.sqrt(discriminante))/(2*a)
raiz2 = (-b - math.sqrt(discriminante))/(2*a)

print('\nLas raices son:')

print('\nRaiz 1:',raiz1)
print('Raiz 2:',raiz2)