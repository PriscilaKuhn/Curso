"""Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad
constante (m/s) durante un tiempo t (s), considerar que es un MRU (Movimiento
Rectilíneo Uniforme). Fórmula de distancia: d = v . t"""

#Input
velocidad=float(input("Ingrese su velocidad en m/s "))
tiempo=float(input("Ingrese el tiempo de recorrido en segundos "))
 
#Proceso
distancia=velocidad*tiempo

#Generando el output

print("La distancia recorrida es :", distancia, "metros")
