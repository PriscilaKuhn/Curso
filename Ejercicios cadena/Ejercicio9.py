"""Escribe un programa que solicite al usuario una frase y una subcadena, y luego
cuente cuántas veces aparece esa subcadena en la frase."""

frase=input("Ingrese una frase")
subcadena=input("Ingrese una subcadena") #Porcion de una frase
contador=0

long_subcadena=len(subcadena)

indice=0

while indice<= len(frase) - long_subcadena:
    porcion=frase[indice:indice+long_subcadena]
    if porcion==subcadena:
        contador+=1

    indice+=1
    

print(contador)