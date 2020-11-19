import numpy as np
import sys

tolerancia = 1e-38
numMax = 1e+19      # (1e+19)^2= 1e+38, orden de magnitud a partir del cual puedo tener overflow con 32 bits

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

if np.abs(discriminante) < tolerancia:
    print('\nRaiz doble:',np.float32((-b)/2*a))
    sys.exit()
    
if discriminante < 0:
    print('\nLas raices no son reales.')
    sys.exit()
    
#aca ya habiendo corroborado que discriminante>0, utilizo logica adicional para 
#salvarme en casos de que pueda ocurrir overflow si los coeficientes son muy grandes

if (np.abs(b) >= numMax or np.abs(4*a*c) >= numMax):    
    m = max(np.abs(b), np.sqrt(np.abs(4*a*c)))
    discriminante = (b/m)**2 + (4*a*c)/(m**2)
    x1 = np.float32(-(b + sgn(b)*m*np.sqrt(discriminante))/(2*a))
    x2 = np.float32(c/(a*x1))
    print('\nLas raices son:\n')
    print('Raiz 1:',x1)
    print('\nRaiz 2:',x2)
    sys.exit()



x1 = np.float32(-(b + sgn(b)*np.sqrt(discriminante))/(2*a))
x2 = np.float32(c/(a*x1))

    
print('\nLas raices son:\n')
print('Raiz 1:',x1)
print('\nRaiz 2:',x2)



