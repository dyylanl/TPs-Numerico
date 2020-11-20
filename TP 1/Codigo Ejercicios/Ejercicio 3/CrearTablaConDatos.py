import OrdenDeConvergencia as ordenConvergencia
import ConstanteAsintotica as cteAsintotica
import sympy as sym
import math
import BusquedaRaicesBiseccion as biseccion

def crearTabla (historiaRaices, convergencia, cteAsintotica):

    print("Iteración\t\t\t\tRaiz\t\t\t\t\tError\t\tConvergencia\tCte Asintótica") 
    for i in range(0, len(historiaRaices) - 1):
    
        print("\t" + str(i) + str("\t\t\t{:.16f}".format(historiaRaices[i][1])) + "\t\t" + str("{:.16f}".format(historiaRaices[i][2])) + "\t\t" + str(convergencia[i][1]) + "\t\t\t\t" + str(cteAsintotica[i][1]))

#R = 4.25

#def funcionParaBiseccion(x):
#    funcionAltura = sym.simplify((-1* (h**3)) + 3*R*(h**2) - (3 * 129.75030272770212/ math.pi))
#    return funcionAltura.subs(h,x)

#h= sym.Symbol('h')
#resultadoBiseccion = biseccion.busqueda_raiz(0, 2*R,10**(-5), funcionParaBiseccion)

#convergenciaBiseccion = ordenConvergencia.ordenDeConvergencia(resultadoBiseccion[3], resultadoBiseccion[2])
#cteAsintoticaBiseccion = cteAsintotica.calcularConstanteAsintotica(resultadoBiseccion[3], resultadoBiseccion[2], 1)

#crearTabla(resultadoBiseccion[3], convergenciaBiseccion, cteAsintoticaBiseccion)