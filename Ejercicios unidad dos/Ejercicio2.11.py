"""Desarrolle un algoritmo para determinar si un año leído por teclado es o no
bisiesto. Dato: AÑO (Variable tipo Entero, almacena el año a evaluar). Un año
bisiesto es aquel múltiplo de 4 pero no de 100 o si es múltiplo de 400."""


anio=int(input("Ingrese año "))

if anio %4==0 or anio %400==0:
    print("Se trata de un año bisiesto")
else:
    print("El año ", anio, "no es un año bisiesto")