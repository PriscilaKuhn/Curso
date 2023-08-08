"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión."""

invertir=float(input("Cantidad a invertir"))
interes=float(input("Ingrese el interés porcental anual"))
anios=int(input("Ingrese la cantiadd de años"))
"""
for i in range (1,anios+1):
   capital=(invertir*i)*interes
   print(i,capital)

"""
for i in range(anios):
    invertir*=1+ (interes/100)
    print("Capital tras " +str(i+1) + "años: "+ str(round(invertir,2)))


    ##VER
