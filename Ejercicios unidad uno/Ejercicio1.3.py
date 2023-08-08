"""Se necesita elaborar un algoritmo que solicite el número de respuestas correctas,
incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje final
considerando que por cada respuesta correcta tendrá 3 puntos, respuestas
incorrectas tendrá -1 y respuestas en blanco tendrá 0."""



respuestas_correctas= int(input("Ingrese cantidad de respuestas correctas "))
respuestas_incorrectas=int(input("Ingrese cantidad de respuestas incorrectas "))
respuestas_blanco=int(input("Ingrese cantidad de respuestas en blancos "))

puntaje_final=((respuestas_correctas*3)+(respuestas_incorrectas*-1)+(respuestas_blanco*0))


print("Puntaje final" ,puntaje_final)

