"""9. Dadas las tres calificaciones de un estudiante, encuentre y muestre la calificación
mayor y la calificación menor."""

calficacion_1=float(input("Ingrese la primera calificación "))
calficacion_2=float(input("Ingrese segunda calificación "))
calficacion_3=float(input("Ingrese tercera calificación "))

#Calificación mas alta
alta=0
if alta< calficacion_1:
    alta=calficacion_1
if calficacion_2>alta:
    alta=calficacion_2
if calficacion_3 >alta:
    alta=calficacion_3

#Calificación mas baja
baja=calficacion_1
if calficacion_2< baja:
        baja=calficacion_2
if calficacion_3 <baja:
     baja=calficacion_3


# Mostrar los resultados
print("La calificación mayor es:", alta)
print("La calificación menor es:", baja)


   