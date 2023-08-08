"""Ingresar 3 valores numéricos y determinar e informar el mayor."""

numero_1=int(input("Ingrese un número "))
numero_2=int(input("Ingrese un número "))
numero_3=int(input("Ingrese un número "))

if (numero_1 > numero_2) and (numero_1> numero_3):
    print("El", numero_1, "es el mayor")
else :
    if (numero_2>numero_1) and (numero_2> numero_3):
     print("El", numero_2, "es el mayor")
    else:
      print("El", numero_3, "es el mayor")
