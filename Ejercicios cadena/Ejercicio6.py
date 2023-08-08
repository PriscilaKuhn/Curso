"""Escribe un programa que solicite al usuario una palabra y cuente cuántas vocales
(a, e, i, o, u) contiene."""

palabra= input("Ingrese una palabra ")

palabra=palabra.lower()

contador_vocales=0
for caracter in palabra:
    if caracter in "aeiou":
        contador_vocales+=1


print("Cantidad de vocales de la palabra" , palabra, "es:",contador_vocales)
