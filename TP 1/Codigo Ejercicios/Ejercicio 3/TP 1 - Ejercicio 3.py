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


def funcionParaBiseccion(x):
    funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))
    return funcionAltura.subs(h,x)


def funcionGParaPuntoFijo(y):
    GdeXParaPuntoFijo = lambda x: ( (( (x**3)/(3*R) ) + (volumenAHallar/(R*math.pi) ))**(1/2))
    return (GdeXParaPuntoFijo(y))

def graficar(funcion, Label, xLabel, yLabel, title):

    plt.figure()
    plt.plot(funcion[:,0], funcion[:,1], '-', lw = 2, label = Label)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(True)
    plt.title(title)
    plt.show()



def buscarRaicesConDistintosMetodosYCota(cota):

    print("\n Usando la cota de error: " + str(cota)+ "\n ")

    print("===========================================" + "\n")
    print ("\t \t \t BISECCION \n")
    print("===========================================" + "\n")

    resultadoBiseccion = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion)
    print("El resultado por Bisección es: "+ str(resultadoBiseccion[:3]) + "\n")

    convergenciaBiseccion = ordenConvergencia.ordenDeConvergencia(resultadoBiseccion[3], resultadoBiseccion[2])
    graficar(convergenciaBiseccion,'Biseccion', "Iteracion", "Orden de convergencia", "Orden de convergencia Biseccion")


    cteAsintoticaBiseccion = cteAsintotica.calcularConstanteAsintotica(resultadoBiseccion[3], resultadoBiseccion[2], 1)
    graficar(cteAsintoticaBiseccion,'Biseccion', "Iteracion", "Constante Asintotica", "Constante asintotica Biseccion")

    crearTabla.crearTabla(resultadoBiseccion[3], convergenciaBiseccion, cteAsintoticaBiseccion)
    x= sym.Symbol('x')
    y= sym.Symbol('y')
    semillaPuntoFijo = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, 3)[0]
    semillaNewton = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, 5)[0]
    semillaAux = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, 4)[0] # Solo para secante


    print ("\n--------------- SEMILLAS ----------------- \n")

    print("Semilla elegida con 3 iteraciones de biseccion: "+ str(semillaPuntoFijo))
    print("Semilla elegida con 5 iteraciones de biseccion: "+ str(semillaNewton))
    print("Semilla auxiliar elegida con 4 iteraciones de biseccion: "+ str(semillaAux) + "\n")


#    GdeXParaPuntoFijo = lambda x: ( (( (x**3)/(3*R) ) + (volumenAHallar/(R*math.pi) ))**(1/2))
    resultadoPuntoFijo = puntoFijo.busqueda_raiz_punto_fijo(semillaPuntoFijo, cota, funcionGParaPuntoFijo, CANT_MAX_DE_ITERACIONES)
    print("===========================================" + "\n")
    print ("\t \t \t PUNTO FIJO \n")
    print("===========================================" + "\n")
    print("El resultado por Punto Fijo es: "+ str(resultadoPuntoFijo[:3]) + "\n")

    convergenciaPuntoFijo = ordenConvergencia.ordenDeConvergencia(resultadoPuntoFijo[3], resultadoPuntoFijo[2])
    graficar(convergenciaPuntoFijo, 'Punto Fijo', "Iteracion", "Orden de convergencia", "Orden de convergencia Punto Fijo")

    cteAsintoticaPuntoFijo = cteAsintotica.calcularConstanteAsintotica(resultadoPuntoFijo[3], resultadoPuntoFijo[2], 1)
    graficar(cteAsintoticaPuntoFijo, 'Punto Fijo', "Iteracion", "Constante Asintotica", "Constante Asintotica Punto Fijo")


    crearTabla.crearTabla(resultadoPuntoFijo[3], convergenciaPuntoFijo, cteAsintoticaPuntoFijo)

    funcionNewton = sym.simplify((-1* (x**3)) + 3*R*(x**2) - (3 * volumenAHallar/ math.pi))

    if (cota == 10**(-5)):
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
    graficar(convergenciaSecante, 'Secante', "Iteracion", "Orden de convergencia", "Orden de convergencia Secante")


    cteAsintoticaSecante = cteAsintotica.calcularConstanteAsintotica(resultadoSecante[3], resultadoSecante[2] + 2, 2)
    graficar(cteAsintoticaSecante, 'Secante', "Iteracion", "Constante Asintotica", "Constante Asintotica Secante")


    crearTabla.crearTabla(resultadoSecante[3], convergenciaSecante, cteAsintoticaSecante)

    if(cota == 10**(-5)):
        resultadoNewton = newton.busqueda_raiz_newton(funcionNewton, semillaNewton, cota, False, 4)
    else:
        resultadoNewton = newton.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)

    print("\n===========================================" + "\n")
    print ("\t \t \t NEWTON \n")
    print("===========================================" + "\n")
    print("El resultado por Newton es: "+ str(resultadoNewton[:3]) + "\n")

    convergenciaNewton = ordenConvergencia.ordenDeConvergencia(resultadoNewton[3], resultadoNewton[2])
    graficar(convergenciaNewton, 'Newton', "Iteracion", "Orden de convergencia", "Orden de convergencia Newton")


    cteAsintoticaNewton = cteAsintotica.calcularConstanteAsintotica(resultadoNewton[3], resultadoNewton[2], 2)
    graficar(cteAsintoticaNewton, 'Newton', "Iteracion", "Constante Asintotica", "Constante Asintotica Newton")

    crearTabla.crearTabla(resultadoNewton[3], convergenciaNewton, cteAsintoticaNewton)

    if(cota == 10**(-5)):
        resultadoNewtonMult = newtonMult.busqueda_raiz_newton(funcionNewton, semillaNewton, cota, False, 4)

    else:
        resultadoNewtonMult = newtonMult.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)

    print("\n===========================================" + "\n")
    print ("\t \t \t NEWTON MULTIPLE \n")
    print("===========================================" + "\n")
    print("El resultado por Newton Mult es: "+ str(resultadoNewtonMult[:3]))

    convergenciaNewtonMult = ordenConvergencia.ordenDeConvergencia(resultadoNewtonMult[3], resultadoNewtonMult[2])
    print("\nOrden de convergencia: \n")
    print(convergenciaNewtonMult)
    graficar(convergenciaNewtonMult, 'Newtorn Multiple', "Iteracion", "Orden de convergencia", "Orden de convergencia Newton Multiple")

    cteAsintoticaNewtonMult = cteAsintotica.calcularConstanteAsintotica(resultadoNewtonMult[3], resultadoNewtonMult[2], 2)
    graficar(cteAsintoticaNewtonMult, 'Newton Multiple', "Iteracion", "Constante Asintotica", "Constante Asintotica Newton Multiple")

    crearTabla.crearTabla(resultadoNewtonMult[3], convergenciaNewtonMult, cteAsintoticaNewtonMult)

    print("\n")

x= sym.Symbol('x')

h= sym.Symbol('h')

graficarFuncionesYDerivadas()

volumenTotalDeAgua = volumenDelTanqueDeAgua(2*R)
porcentajePedido = porcentajeDeAguaABuscar()

volumenAHallar = volumenLlenoAPorcentaje(porcentajePedido)

funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))


#graficoAltura = sym.plotting.plot(funcionAltura, (h, 0, 2*R))

print("a) Volumen del tanque lleno al "+ str(porcentajePedido*100) +  "% calculado: " + str(volumenAHallar) + "\n")
print("b) El volumen total del tanque es: " + str(volumenLlenoAPorcentaje(1)))

print("\nc) \n")

buscarRaicesConDistintosMetodosYCota(10**(-5))
buscarRaicesConDistintosMetodosYCota(10**(-13))

raizScipy = optimize.brentq(lambda x: (math.pi * x ** 2 * (3 * R - x)) / 3, 1, 15)

print("f) Raiz encontrada con función de búsqueda de raíces Scipy: " + str(raizScipy))
