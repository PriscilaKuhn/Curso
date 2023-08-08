"""Ejercicio 1 con estructuras selectivas
Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y
muestre el valor del volumen del cilindro, caso contrario muestre el valor del área
del cilindro.

"""

from math import pi

radio=float(input("Ingrese el radio del cilindro: "))
altura=float(input("Ingrese la altura del cilindro: "))


if radio < altura:
    volumen_c= ((radio**2)*pi)*altura
    print(" El valor del volumen del cilindro", volumen_c)
else: 
    area_c= 2*pi*radio*(radio+altura)
    print("El valor del área del cilindro", area_c )