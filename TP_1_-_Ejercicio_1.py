import numpy as np
import matplotlib.pyplot as plt



def generarClaveRandom(cantidadDigitos):    
    digitos = np.random.randint(0, 10, cantidadDigitos)
    
    numeroRandom = ""
    for digito in digitos:
        numeroRandom += str(digito)
    
    # Si lo necesitamos con los 0s adelante,
    # devolver directamente numeroRandom sin 
    # convertirlo a int
    return int(numeroRandom) 

def encontrarClaveFuerzaBruta(claveElegida):
    i=0
    while (i != claveElegida):
        i+=1
    #print("La clave encontrada es: " + str(i))
    return i
    
def graficarHistograma(intentos): 
 
    # Uso cantidadDeExperimentos/10 para que me queden
    # rangos de (0,10), (10,20), ...
    n, bins, patches = plt.hist(intentos, bins=(int(len(intentos)/10)) )
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Intentos')
    plt.ylabel('Experimentos')
    plt.title('Experimentos realizados')
    maxfreq = n.max()
    
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    



def intentarEncontrarClave(veces):
    intentos = []
    for i in range(veces):
        clave = generarClaveRandom(4)
        intentos.append(encontrarClaveFuerzaBruta(clave))
    
    return intentos



cantidadDeExperimentos = 100000
intentos = intentarEncontrarClave(cantidadDeExperimentos)
graficarHistograma(intentos)
