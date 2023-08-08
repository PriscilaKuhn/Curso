"""Dadas las tres calificaciones de dos estudiantes. La calificación final de cada uno
es la suma de sus dos mejores calificaciones. Muestre un mensaje que indique cual
estudiante (1 o 2) tiene la mayor calificación final."""


print("*--------Primer estudiante---------*")
#Primer estudiante
estudiante_1_1=float(input("Ingrese primera calificación "))
estudiante_1_2=float(input("Ingrese segunda calificación "))
estudiante_1_3=float(input("Ingrese tercera calificación "))

if estudiante_1_1 >= estudiante_1_2 and estudiante_1_2 >= estudiante_1_3:
    calificacion_final_1=estudiante_1_1 + estudiante_1_2
else:
    if estudiante_1_1 <= estudiante_1_2 and estudiante_1_2 >= estudiante_1_3:
     calificacion_final_1=estudiante_1_2 + estudiante_1_1
    else:
        if estudiante_1_1 <= estudiante_1_2 and estudiante_1_2 <= estudiante_1_3:
            calificacion_final_1=estudiante_1_2 + estudiante_1_3
        else:
            calificacion_final_1= estudiante_1_1 + estudiante_1_3
  
print("Calificación final del primer estudiante", calificacion_final_1)


print("*--------Segundo estudiante---------*")
#Segundo estudiante
estudiante_2_1=float(input("Ingrese primera calificación "))
estudiante_2_2=float(input("Ingrese segunda calificación "))
estudiante_2_3=float(input("Ingrese tercera calificación "))

if estudiante_2_1 >= estudiante_2_2 and estudiante_2_2 >= estudiante_2_3:
    calificacion_final_2=estudiante_2_1 + estudiante_2_2
else:
    if estudiante_2_1 <= estudiante_2_2 and estudiante_2_2 >= estudiante_2_3:
     calificacion_final_2=estudiante_2_2 + estudiante_2_1
    else:
        if estudiante_2_1 <= estudiante_2_2 and estudiante_2_2<= estudiante_2_3:
            calificacion_final_2=estudiante_2_2 + estudiante_2_3
        else:
            calificacion_final_2= estudiante_2_1 + estudiante_2_3

print("Calificación final del segundo estudiante ", calificacion_final_2)

print("*--------Calificación final---------*")
if calificacion_final_1 >calificacion_final_2:
    print("El primer estudiante tiene la mayor calificación final")
else:
    print("El segundo estudiante tiene la mayor calificación final")



