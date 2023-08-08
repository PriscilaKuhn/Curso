"""3. Escribe un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda)."""


frase= input("Ingresar una frase: ")

frase_invertida=frase[::-1] #Slicing

if frase==frase_invertida:
    print(f" {frase}, es palíndromo")

else:
    print(f"La palabra ingresada, {frase}, no es palíndromo")


