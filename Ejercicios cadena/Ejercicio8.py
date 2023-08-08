"""Escribe un programa que solicite al usuario una frase y una longitud, y luego
cuente cuántas palabras de esa longitud hay en la frase."""

frase= input("Ingresa una frase:")

longitud=int(input("Ingresa una longitud"))

palabras= frase.split() #LISTA DE SUBCADENAS

contador_palabras=0

for palabra in palabras:
    if len(palabras)==longitud:
        contador_palabras+=1


print("La cantidad de palabras de esta " , longitud, " longitud hay en la frase,  es de: ",contador_palabras)