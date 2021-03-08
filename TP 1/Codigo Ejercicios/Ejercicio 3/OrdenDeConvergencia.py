import numpy as np

def ordenDeConvergencia (historiaRaiz, cantidadIteraciones):
        alfa = np.zeros((cantidadIteraciones + 1, 2))
        
        n = 2
        
        while (n < cantidadIteraciones - 1):
            error_n_mas_1 = historiaRaiz[n+1][1] - historiaRaiz[n][1]
            error_n = historiaRaiz[n][1] - historiaRaiz[n-1][1]
            error_n_menos_1 = historiaRaiz[n-1][1] - historiaRaiz[n-2][1]
            
            alfa[n] = (n, np.log10(np.abs(error_n_mas_1/error_n)) / np.log10(np.abs(error_n/error_n_menos_1)))
            
            n += 1
            
        return alfa