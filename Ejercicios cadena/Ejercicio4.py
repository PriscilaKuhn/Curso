"""Escribe un programa que solicite al usuario una frase y cuente cuántas palabras
contiene."""

frase=input("Ingresar una frase ")

contador=1

for caracter in frase:
    if caracter==" ":
        contador +=1

print(contador)