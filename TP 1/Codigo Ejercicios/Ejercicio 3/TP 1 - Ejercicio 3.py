import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import matplotlib.pyplot as plt
from scipy import optimize

import BusquedaRaicesBiseccion as biseccion
import BusquedaRaicesNewton as newton
import BusquedaRaicesMultiplesNewton as newtonMult
import BusquedaRaicesPuntoFijo as puntoFijo
import BusquedaRaicesSecante as secante

import OrdenDeConvergencia as ordenConvergencia
import ConstanteAsintotica as cteAsintotica
import CrearTablaConDatos as crearTabla


R = 4.25
CANT_DE_INTEGRANTES = 6
CANT_MAX_DE_ITERACIONES = 50

def volumenDelTanqueDeAgua(alturaActual):
    return ( (math.pi * (alturaActual ** 2)* (3*R-alturaActual))/3 )

def sumaDePadrones():
    padrones = ["103026", "102876", "100204", "100635", "102110", "102202"]
    suma = 0
    for padron in padrones:
      suma += int(padron[-1])
    return suma

def porcentajeDeAguaABuscar():
    s = sumaDePadrones()
    n = CANT_DE_INTEGRANTES
    return (s/(n*9.5))

def volumenLlenoAPorcentaje(porcentaje):
  #       VolumenTotal               * porcentaje
  return volumenDelTanqueDeAgua(2*R) * porcentaje


def funcionf1ConVolumenAl40PorCiento(x):
    funcionf1 = sym.simplify ( math.pi * R * (x ** 2) - (math.pi * (x ** 3))/3 - volumenLlenoAPorcentaje(porcentajeDeAguaABuscar()) )
    return funcionf1

def funcionf2ConVolumenLleno(x):
    funcionf2 = sym.simplify ( math.pi * R * (x ** 2) - (math.pi * (x ** 3))/3 - volumenLlenoAPorcentaje(1) )
    return funcionf2

def graficarFuncionesYDerivadas(mostrarLeyenda = False):

    funcionVolumenPorcentajeEnSimbolos = sym.simplify((math.pi * (x ** 2)* (3*R-x))/3)
    funcionVolumenPorcentajeDerivada = sym.simplify(sym.diff(funcionVolumenPorcentajeEnSimbolos,x))

    graficoVolumen = sym.plotting.plot(funcionVolumenPorcentajeEnSimbolos, (x, 0, 2*R), title = "Grafico Volumen y Derivada segun el Radio del Tanque", label = "Funcion Volumen", xlabel = "Radio", ylabel = "Volumen", legend = mostrarLeyenda)
    graficoDerivada = sym.plotting.plot(funcionVolumenPorcentajeDerivada, (x, 0, 2*R),  line_color = 'r', label = "Derivada de Volumen segun el Radio", legend = mostrarLeyenda)
    graficoVolumen.extend(graficoDerivada)
    graficoVolumen.extend(sym.plotting.plot(volumenDelTanqueDeAgua(2*R), (x, 0, 2*R), line_color = 'g', label = "Volumen maximo", legend = mostrarLeyenda))
    graficoVolumen.extend(sym.plotting.plot(0, (x, 0, 2*R), line_color = "Yellow", label = "Derivada Volumen Maximo", legend = mostrarLeyenda))
    graficoVolumen.show()

    funcionf1 = funcionf1ConVolumenAl40PorCiento(x)
    funcionf2 = funcionf2ConVolumenLleno(x)
    graficof1 = sym.plotting.plot(funcionf1, (x, 0, 2*R), title = "Funcion f1 (x)")
    graficof2 = sym.plotting.plot(funcionf2, (x, 0, 2*R), title = "Funcion f2 (x)")

    graficof1.show()
    graficof2.show()
    
    funcionf1Derivada = sym.simplify(sym.diff(funcionf1,x))
    graficoDerivadaDef1 = sym.plotting.plot(funcionf1Derivada, (x, 0, 2*R),  title = "Gráfico de la derivada de f1", line_color = 'r', label = "Derivada de f2", legend = mostrarLeyenda)
    graficoDerivadaDef1.show()
 

    funcionf2Derivada = sym.simplify(sym.diff(funcionf2,x))
    graficoDerivadaDef2 = sym.plotting.plot(funcionf2Derivada, (x, 0, 2*R),  title = "Gráfico de la derivada de f2", line_color = 'r', label = "Derivada de f2", legend = mostrarLeyenda)
    graficoDerivadaDef2.show()


def funcionParaBiseccion(x):
    funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))
    return funcionAltura.subs(h,x)


def funcionGParaPuntoFijo(y):
    GdeXParaPuntoFijo = lambda x: ( (( (x**3)/(3*R) ) + (volumenAHallar/(R*math.pi) ))**(1/2))
    return (GdeXParaPuntoFijo(y))


def funcionParaBiseccionDeF2(x):
    funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenLlenoAPorcentaje(1)/ math.pi))
    return funcionAltura.subs(h,x)


def funcionGParaPuntoFijoDeF2(y):
    GdeXParaPuntoFijo = lambda x: ( (( (x**3)/(3*R) ) + (volumenLlenoAPorcentaje(1)/(R*math.pi) ))**(1/2))
    return (GdeXParaPuntoFijo(y))

def graficar(funcion, Label, xLabel, yLabel, title):

    plt.figure()
    plt.plot(funcion[:,0], funcion[:,1], '-', lw = 2, label = Label)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(True)
    plt.title(title)
    plt.show()



def buscarRaicesConDistintosMetodosYCota(cota, volumenDelTanque):       

    print("\n Usando la cota de error: " + str(cota)+ "\n ")

    print("===========================================" + "\n")
    print ("\t \t \t BISECCION \n")
    print("===========================================" + "\n")


    if (volumenDelTanque == volumenLlenoAPorcentaje(1)):
        resultadoBiseccion = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccionDeF2)
    else:
        resultadoBiseccion = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion)
        
    print("El resultado por Bisección es: "+ str(resultadoBiseccion[:3]) + "\n")

    convergenciaBiseccion = ordenConvergencia.ordenDeConvergencia(resultadoBiseccion[3], resultadoBiseccion[2])
    graficar(convergenciaBiseccion[2:-2],'Biseccion', "Iteracion", "Orden de convergencia", "Orden de convergencia Biseccion")


    cteAsintoticaBiseccion = cteAsintotica.calcularConstanteAsintotica(resultadoBiseccion[3], resultadoBiseccion[2], 1)
    graficar(cteAsintoticaBiseccion[1:-2],'Biseccion', "Iteracion", "Constante Asintotica", "Constante asintotica Biseccion")

    crearTabla.crearTabla(resultadoBiseccion[3], convergenciaBiseccion, cteAsintoticaBiseccion)
    x= sym.Symbol('x')
    y= sym.Symbol('y')
    
    iteracionesSemillaPuntoFijo = 3
    iteracionesSemillaNewton = 5
    iteracionesSemillaAux = 4
    
    if (volumenDelTanque == volumenLlenoAPorcentaje(1)):
        
       if(cota == 1e-13):
           iteracionesSemillaPuntoFijo = 10
       
       semillaPuntoFijo = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccionDeF2, iteracionesSemillaPuntoFijo)[0]
       semillaNewton = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccionDeF2, iteracionesSemillaNewton)[0]
       semillaAux = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccionDeF2, iteracionesSemillaAux)[0] # Solo para secante

    else:
       semillaPuntoFijo = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, iteracionesSemillaPuntoFijo)[0]
       semillaNewton = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, iteracionesSemillaNewton)[0]
       semillaAux = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, iteracionesSemillaAux)[0] # Solo para secante


    print ("\n--------------- SEMILLAS ----------------- \n")

    print("Semilla elegida con " + str(iteracionesSemillaPuntoFijo) +" iteraciones de biseccion: "+ str(semillaPuntoFijo))
    print("Semilla elegida con " + str(iteracionesSemillaNewton) +" iteraciones de biseccion: "+ str(semillaNewton))
    print("Semilla auxiliar elegida con " + str(iteracionesSemillaAux) +" iteraciones de biseccion: "+ str(semillaAux) + "\n")


    
    print("===========================================" + "\n")
    print ("\t \t \t PUNTO FIJO \n")
    print("===========================================" + "\n")
    
    if (volumenDelTanque == volumenLlenoAPorcentaje(1)):
        resultadoPuntoFijo = puntoFijo.busqueda_raiz_punto_fijo(semillaPuntoFijo, cota, funcionGParaPuntoFijoDeF2, CANT_MAX_DE_ITERACIONES)
    
    else:
        resultadoPuntoFijo = puntoFijo.busqueda_raiz_punto_fijo(semillaPuntoFijo, cota, funcionGParaPuntoFijo, CANT_MAX_DE_ITERACIONES)
    
 
    
    print("El resultado por Punto Fijo es: "+ str(resultadoPuntoFijo[:3]) + "\n")

    convergenciaPuntoFijo = ordenConvergencia.ordenDeConvergencia(resultadoPuntoFijo[3], resultadoPuntoFijo[2] + 1)
    graficar(convergenciaPuntoFijo[2:-2], 'Punto Fijo', "Iteracion", "Orden de convergencia", "Orden de convergencia Punto Fijo")

    cteAsintoticaPuntoFijo = cteAsintotica.calcularConstanteAsintotica(resultadoPuntoFijo[3], resultadoPuntoFijo[2] + 1, 1)
    graficar(cteAsintoticaPuntoFijo[1:-2], 'Punto Fijo', "Iteracion", "Constante Asintotica", "Constante Asintotica Punto Fijo")

    crearTabla.crearTabla(resultadoPuntoFijo[3], convergenciaPuntoFijo, cteAsintoticaPuntoFijo)


    funcionNewton = sym.simplify((-1* (x**3)) + 3*R*(x**2) - (3 * volumenDelTanque/ math.pi))
        
    if (volumenDelTanque == volumenLlenoAPorcentaje(volumenAHallar) and (cota == 10**(-5))):
        resultadoSecante = secante.busqueda_raiz_secante(funcionNewton,\
                                                         semillaNewton, semillaAux,  cota, False, 4)
    else:
        resultadoSecante = secante.busqueda_raiz_secante(funcionNewton,\
                                                     semillaNewton, semillaAux,  cota)
        
       

    print("===========================================" + "\n")
    print ("\t \t \t SECANTE \n")
    print("===========================================" + "\n")
    print("El resultado por Secante es: "+ str(resultadoSecante[:3]) + "\n")

    convergenciaSecante = ordenConvergencia.ordenDeConvergencia(resultadoSecante[3], resultadoSecante[2] + 2)
    graficar(convergenciaSecante[2:-2], 'Secante', "Iteracion", "Orden de convergencia", "Orden de convegencia Secante")

    cteAsintoticaSecante = cteAsintotica.calcularConstanteAsintotica(resultadoSecante[3], resultadoSecante[2] + 2, 1)
    graficar(cteAsintoticaSecante[1:-2], 'Secante', "Iteracion", "Constante Asintotica", "Constante Asintotica Secante")


    crearTabla.crearTabla(resultadoSecante[3], convergenciaSecante, cteAsintoticaSecante)

    if (volumenDelTanque == volumenLlenoAPorcentaje(volumenAHallar) and (cota == 10**(-5))):
        resultadoNewton = newton.busqueda_raiz_newton(funcionNewton, semillaNewton, cota, False, 4)
    else:
        resultadoNewton = newton.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)

    print("\n===========================================" + "\n")
    print ("\t \t \t NEWTON \n")
    print("===========================================" + "\n")
    print("El resultado por Newton es: "+ str(resultadoNewton[:3]) + "\n")

    convergenciaNewton = ordenConvergencia.ordenDeConvergencia(resultadoNewton[3], resultadoNewton[2] + 1)
    graficar(convergenciaNewton[2:-2], 'Newton', "Iteracion", "Orden de convergencia", "Orden de convergencia Newton")


    cteAsintoticaNewton = cteAsintotica.calcularConstanteAsintotica(resultadoNewton[3], resultadoNewton[2] + 1, 2)
    graficar(cteAsintoticaNewton[1:-2], 'Newton', "Iteracion", "Constante Asintotica", "Constante Asintotica Newton")

    crearTabla.crearTabla(resultadoNewton[3], convergenciaNewton, cteAsintoticaNewton)

    if (volumenDelTanque == volumenLlenoAPorcentaje(volumenAHallar) and (cota == 10**(-5))):
        resultadoNewtonMult = newtonMult.busqueda_raiz_newton(funcionNewton, semillaNewton, cota, False, 4)

    else:
        resultadoNewtonMult = newtonMult.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)

    print("\n===========================================" + "\n")
    print ("\t \t \t NEWTON MULTIPLE \n")
    print("===========================================" + "\n")
    print("El resultado por Newton Mult es: "+ str(resultadoNewtonMult[:3]))

    convergenciaNewtonMult = ordenConvergencia.ordenDeConvergencia(resultadoNewtonMult[3], resultadoNewtonMult[2] + 1)

    graficar(convergenciaNewtonMult[2:-2], 'Newtorn Multiple', "Iteracion", "Orden de convergencia", "Orden de convergencia Newton Multiple")

    cteAsintoticaNewtonMult = cteAsintotica.calcularConstanteAsintotica(resultadoNewtonMult[3], resultadoNewtonMult[2] + 1, 2)
    graficar(cteAsintoticaNewtonMult[1:-2], 'Newton Multiple', "Iteracion", "Constante Asintotica", "Constante Asintotica Newton Multiple")

    crearTabla.crearTabla(resultadoNewtonMult[3], convergenciaNewtonMult, cteAsintoticaNewtonMult)

    print("\n")


x= sym.Symbol('x')

h= sym.Symbol('h')

graficarFuncionesYDerivadas()

volumenTotalDeAgua = volumenDelTanqueDeAgua(2*R)
porcentajePedido = porcentajeDeAguaABuscar()

volumenAHallar = volumenLlenoAPorcentaje(porcentajePedido)

funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))


print("a) Volumen del tanque lleno al "+ str(porcentajePedido*100) +  "% calculado: " + str(volumenAHallar) + "\n")
print("b) El volumen total del tanque es: " + str(volumenLlenoAPorcentaje(1)))

print("\nc) \n")

print("***************************************************************" + "\n")
print ("\t \t FUNCION F1: VOLUMEN LLENO APROX. AL 40% \n")
print("***************************************************************" + "\n")
buscarRaicesConDistintosMetodosYCota(10**(-5), volumenAHallar)
buscarRaicesConDistintosMetodosYCota(10**(-13), volumenAHallar)

print("\n\n\n")

print("***************************************************************" + "\n")
print ("\t \t FUNCION F2: VOLUMEN LLENO AL 100% \n")
print("***************************************************************" + "\n")
buscarRaicesConDistintosMetodosYCota(10**(-5), volumenTotalDeAgua)
buscarRaicesConDistintosMetodosYCota(10**(-13), volumenTotalDeAgua)


raizScipy = optimize.brentq(lambda x: (math.pi * x ** 2 * (3 * R - x)) / 3, 1, 15)

print("f) Raiz encontrada con función de búsqueda de raíces Scipy: " + str(raizScipy))
