"""Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el
algoritmo que permita obtener la distancia entre A y B."""

Ax=float(input("Ingrese coordenada de eje x del punto A "))
Ay=float(input("Ingrese coordenada de eje y del punto A "))

Bx=float(input("Ingrese coordenada de eje x del punto B "))
By=float(input("Ingrese coordenada de eje y del punto B "))



distancia= (((Bx-Ax)**2 )+ ((By-Ay)**2))**0.5

print(f"La distancia entre el valor A y B es de {distancia}")
