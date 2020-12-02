import numpy as np

def calcularConstanteAsintotica (historiaRaiz, cantidadIteraciones, ordenDeConvergencia):
    
    constanteAsintotica = np.zeros((cantidadIteraciones - 1, 2))
    n = 1
    
    while (n < cantidadIteraciones - 1):
        
        e_n_mas_1 = np.abs(historiaRaiz[n+1][1] - historiaRaiz[n][1])
        e_n_elevado_a_p = np.abs(historiaRaiz[n][1] - historiaRaiz[n-1][1]) ** ordenDeConvergencia
        
        constanteAsintotica[n] = (n, e_n_mas_1 / e_n_elevado_a_p)   
        
        n += 1
    
    return constanteAsintotica
#lambda   
#print(np.abs(3.7001485030767087 - 3.7001499517657974))
#print(np.abs(3.7001499517657974 - 3.6999852142037337))
#print(np.abs(3.7001485030767087 - 3.7001499517657974) / (np.abs(3.7001499517657974 - 3.6999852142037337)) ** 2)

#alfa
#error_n_mas_1 = n+1 - n
#error_n = n - n-1
#error_n_menos_1 = n-1 - n-2
#print(np.log10(np.abs(error_n_mas_1/error_n)) / np.log10(np.abs(error_n/error_n_menos_1)))

#print(np.abs(3.7001485030840335 - 3.7001485030767087 / 3.7001485030767087 - 3.7001499517657974))

#numerador = 3.7001485030840335 - 3.7001485030767087
#denominador = 3.7001485030767087 - 3.7001499517657974
#print(numerador)
#print(denominador)
#print(np.abs(numerador/denominador))

#pero me dice que esrtoy dividiendo por cero wtf
#print(np.log10(np.abs(numerador/denominador)))

#numerador = 
#denominador = 3.7001485030840335 - 3.7001485030767087
#print(denominador)