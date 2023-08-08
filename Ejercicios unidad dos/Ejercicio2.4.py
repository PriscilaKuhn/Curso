"""Lea un número de dos cifras. Determinar si la suma de ambas cifras es un número
par o impar. Muestre un mensaje"""


numero = int(input("Ingrese un número de dos cifras: "))

# Obtener las dos cifras del número
cifra1 = numero // 10
cifra2 = numero % 10

# Calcular la suma de las cifras
suma_cifras = cifra1 + cifra2

# Verificar si la suma es par o impar
if suma_cifras % 2 == 0:
    mensaje = "La suma de las cifras es un número par."
else:
    mensaje = "La suma de las cifras es un número impar."

print(mensaje)
