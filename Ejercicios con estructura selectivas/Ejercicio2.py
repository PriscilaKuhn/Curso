"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad)."""

edad=int(input("Ingrese la edad "))

"""for i in range (1, edad+1):

    print(i)"""
for i in range (edad):
   print("Ha cumplido "+ str(i+1)+ " años") #para concatenar texto con número

    #I es un indice, pero tambien un contador
