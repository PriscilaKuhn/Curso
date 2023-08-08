def promedio (suma,cantidad):
    prom =(suma/cantidad)
    return prom
     


n1=float(input("Ingrese la nota 1 "))

n2=float(input("Ingrese la nota 2 "))

n3=float(input("Ingrese la nota 3 "))

acumulador= n1+n2+n3

prom=promedio(acumulador,3)

print("El promedio del alumno es: ", prom)
