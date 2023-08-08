"""Dados los tres lados de un triángulo determine su tipo: Equilátero, Isósceles, o
Escaleno."""

lado_1=int(input("Ingrese  valor lado 1 "))
lado_2=int(input("Ingrese  valor lado 2 "))
lado_3=int(input("Ingrese  valor lado 3 "))

if lado_1== lado_2 and lado_2==lado_3:
    print("Es un triángulo equilátero, tiene sus tres lados iguales")
else:
    if (lado_1 == lado_2 and lado_2!=lado_3 ) or (lado_1 !=lado_2 and lado_2==lado_3) or (lado_1==lado_3 and lado_3!= lado_2)or(lado_1 !=lado_3 and lado_3== lado_2):
        print("Es un triángulo isósceles, tiene dos lados iguales y uno desigual")
    else:
        print("Se trata de un triángulo escaleno, sus tres lados son desiguales")
