"""Escribe un programa que solicite al usuario una palabra y luego muestre la palabra
sin los caracteres repetidos."""



palabra=input("Ingresar una palabra: ")

caracteres_unicos= []

for caracter in palabra:

    if caracter not in caracteres_unicos:
        caracteres_unicos.append(caracter)

palabras_sin_repetidos="".join(caracteres_unicos)

print("Palabra sin caracteres repeditos: ", palabras_sin_repetidos)