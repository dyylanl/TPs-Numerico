import math
import sys
import numpy as np

print('\n Ingrese los valores ax^2 + bx +c:')

a = np.float32(input('a: '))
b = np.float32(input('b: '))
c = np.float32(input('c: '))

if (a != 1):   
        b = np.float32(b/a) # hago una reescala de b
        c = np.float32(c/a) # hago una reescala de c
        a = 1   # pongo a en 1
    
# defino mis valores m (punto medio entre las raices)
# y d (distancia desde m a las raices)

m = np.float32((-b)/2)

if (m**2 -c < 0):
    print('\n Las raices son complejas. Intente de nuevo.')
    sys.exit()

d = np.float32(math.sqrt(m**2 - c))

raiz1 = np.float32(m + d)
raiz2 = np.float32(m - d)

print('\n Las raices son: \n')
print('Raiz 1:',raiz1,'Raiz 2:',raiz2)
