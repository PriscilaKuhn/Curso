"""Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) y se
desea visualizar si el número es par o impar. Validar"""
numero=int(input("Ingrese número entre 0 y 10 inclusive"))

if numero >= 0 and numero <= 10:
    if numero %2==0:

        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")
    
else:
    print("Valor inválido.Por favor, ingrese un número entre 0 y 10.")
