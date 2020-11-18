import numpy as np
import BusquedaRaicesBiseccion as bb 

def ordenDeConvergencia (historiaRaiz, cantidadIteraciones):
        alfa = np.zeros((cantidadIteraciones - 1, 2))
        
        for n in range (2, cantidadIteraciones - 1):
            
            error_n_mas_1 = historiaRaiz[n+1][1] - historiaRaiz[n][1]
            error_n = historiaRaiz[n][1] - historiaRaiz[n-1][1]
            error_n_menos_1 = historiaRaiz[n-1][1] - historiaRaiz[n-2][1]

            alfa[n] = (n, np.log10(np.abs(error_n_mas_1/error_n)) / np.log10(np.abs(error_n/error_n_menos_1)))
            
        return alfa
    
#historiaBiseccion = bb.busqueda_raiz(1, 2, 1e-12, lambda x: (1/2) * ((10 - (x ** 3)) ** (1/2)))[2]
#cantidadIteracionesBiseccion = len(historiaBiseccion)
#print(historiaBiseccion)
#ordenDeConvergenciaBiseccion = ordenDeConvergencia(historiaBiseccion, cantidadIteracionesBiseccion)
#print("Orden de convergencia:'/n' " + str(ordenDeConvergenciaBiseccion))