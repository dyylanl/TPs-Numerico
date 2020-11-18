import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

import BusquedaRaicesBiseccion as biseccion
import BusquedaRaicesNewton as newton
import BusquedaRaicesMultiplesNewton as newtonMult
#import BusquedaRaicesPuntoFijo as puntoFijo
import BusquedaRaicesSecante as secante


R = 4.25
CANT_DE_INTEGRANTES = 6

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


def graficarFuncionesYDerivadas(mostrarLeyenda = False):
    
    funcionVolumenPorcentajeEnSimbolos = sym.simplify((math.pi * (x ** 2)* (3*R-x))/3)
    funcionVolumenPorcentajeDerivada = sym.simplify(sym.diff(funcionVolumenPorcentajeEnSimbolos,x))
    
    graficoVolumen = sym.plotting.plot(funcionVolumenPorcentajeEnSimbolos, (x, 0, 2*R), title = "Grafico Volumen y Derivada segun el Radio del Tanque", label = "Funcion Volumen", xlabel = "Radio", ylabel = "Volumen", legend = mostrarLeyenda)
    graficoDerivada = sym.plotting.plot(funcionVolumenPorcentajeDerivada, (x, 0, 2*R),  line_color = 'r', label = "Derivada de Volumen segun el Radio", legend = mostrarLeyenda)
    graficoVolumen.extend(graficoDerivada)
    graficoVolumen.extend(sym.plotting.plot(volumenDelTanqueDeAgua(2*R), (x, 0, 2*R), line_color = 'g', label = "Volumen maximo", legend = mostrarLeyenda))
    graficoVolumen.extend(sym.plotting.plot(0, (x, 0, 2*R), line_color = "Yellow", label = "Derivada Volumen Maximo", legend = mostrarLeyenda))
    
    
    graficoVolumen.show()


def funcionParaNewton(x):
    return
    
    
def funcionParaNewtonMult(x):
    return
    
        
def funcionParaPuntoFijo(x):
    return
    
    
def funcionParaBiseccion(x):
    funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))
    return funcionAltura.subs(h,x)


def buscarRaicesConDistintosMetodosYCota(cota):
    
    resultadoBiseccion = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion)
    print("El resultado por Bisección es: "+ str(resultadoBiseccion))
    
    #resultadoPuntoFijo = puntoFijo.busqueda_raiz(0, 2*R, cota, funcionParaPuntoFijo)
    #print("El resultado por Punto Fijo es: "+ str(resultadoPuntoFijo))
    
    x= sym.Symbol('x')
    y= sym.Symbol('y')
    semillaNewton = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, 5)[0]
    semillaAux = biseccion.busqueda_raiz(0, 2*R,cota, funcionParaBiseccion, 4)[0] # Solo para secante
    
    print("Semilla elegida con 5 iteraciones de biseccion: "+ str(semillaNewton))
    print("Semilla auxiliar elegida con 4 iteraciones de biseccion: "+ str(semillaAux))
    
    
    funcionNewton = sym.simplify((-1* (x**3)) + 3*R*(x**2) - (3 * volumenAHallar/ math.pi))
    
    resultadoSecante = secante.busqueda_raiz_secante(funcionNewton, semillaNewton, semillaAux,  cota)
    print("El resultado por Secante es: "+ str(resultadoSecante))
    
    resultadoNewton = newton.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)
    print("El resultado por Newton es: "+ str(resultadoNewton))
    
    resultadoNewtonMult = newtonMult.busqueda_raiz_newton(funcionNewton, semillaNewton, cota)
    print("El resultado por Newton Mult es: "+ str(resultadoNewtonMult))
    
x= sym.Symbol('x')

h= sym.Symbol('h')

 

graficarFuncionesYDerivadas()

volumenTotalDeAgua = volumenDelTanqueDeAgua(2*R)
porcentajePedido = porcentajeDeAguaABuscar()

volumenAHallar = volumenLlenoAPorcentaje(porcentajePedido)

funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * volumenAHallar/ math.pi))


#graficoAltura = sym.plotting.plot(funcionAltura, (h, 0, 2*R))

print("a) Volumen del tanque lleno al "+ str(porcentajePedido*100) +  "% calculado: " + str(volumenAHallar))
print("b) El volumen total del tanque es: " + str(volumenLlenoAPorcentaje(1)))

buscarRaicesConDistintosMetodosYCota(10**(-5))



