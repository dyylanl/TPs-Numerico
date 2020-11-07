import math
import sys

print('\n Ingrese los valores ax^2 + bx +c:')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (a != 1):   
        b = b/a # hago una reescala de b
        c = c/a # hago una reescala de c
        a = 1   # pongo a en 1
    
# defino mis valores m (punto medio entre las raices)
# y d (distancia desde m a las raices)

m = (-b)/2

if (m**2 -c < 0):
    print('\n Las raices son complejas. Intente de nuevo.')
    sys.exit()

d = math.sqrt(m**2 - c)

raiz1 = m + d
raiz2 = m - d

print('\n Las raices son: \n')
print('Raiz 1:',raiz1,'Raiz 2:',raiz2)