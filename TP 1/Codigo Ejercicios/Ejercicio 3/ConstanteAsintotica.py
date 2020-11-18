import numpy as np

def calcularConstanteAsintotica (historiaRaiz, cantidadIteraciones, ordenDeConvergencia):
    
    constanteAsintotica = np.zeros((cantidadIteraciones - 1, 2))
    
    for n in range (1, cantidadIteraciones - 1):
        
        e_n_mas_1 = np.abs(historiaRaiz[n+1][1] - historiaRaiz[n][1])
        e_n_elevado_a_p = np.abs(historiaRaiz[n][1] - historiaRaiz[n-1][1]) ** ordenDeConvergencia
        
        constanteAsintotica[n] = (n, e_n_mas_1 / e_n_elevado_a_p)
    
    return constanteAsintotica
    
    