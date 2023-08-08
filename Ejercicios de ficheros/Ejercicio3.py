"""Crear un programa que permita al usuario registrar y analizar las ventas de un negocio.
Las ventas se registrarán en un archivo de texto y se podrán realizar operaciones como
calcular el total de ventas, el promedio de ventas y encontrar las ventas más altas y más
bajas."""


#Crear un menú
print("Hola")
print("Las opciones que ofrecemos son :")


def opcion_uno():
    productos= (input("Ingrese nombre de producto "))
    fecha= (input("Ingrese la fecha de venta "))
    monto=float(input("Ingrese el monto de la venta: "))

    with open("ventas.txt", "a") as archivo:
        archivo.write(f"{fecha}\t{productos}\t{monto}\n")
    print("Venta registrada") 

def cant_total():
     cont=0
     with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            _,_, monto= linea.strip().split("\t")
            cont+= float(monto)

     return cont

def promedio():
    total_ventas=cant_total()
    with open("ventas.txt", "r") as archivo:
        num_ventas = sum(1 for _ in archivo)

    if num_ventas > 0:
        promedio = total_ventas / num_ventas
    else:
        promedio = 0

    return promedio
     


def ventas_max_min():
     
    ventas = []

    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            monto = linea.strip().split("\t")
            ventas.append(float(monto[2]))

    if ventas:
        venta_maxima = max(ventas)
        venta_minima = min(ventas)
        return venta_maxima, venta_minima
    else:
        return None, None    
    
def imprimir_menu():
    while True:    
        print ("\n MENÚ:\n")
        print("Presione 1 para registrar la venta")
        print("Presione 2 para analizar el calcular el total de ventas")
        print("Presione 3 para analizar el promedio de ventas")
        print("Presione 4 para encontrar la venta más alta y más baja")
        print("Presione 5 para salir")
        ingresar=input("Selecciona una opción: ")
        if ingresar=="1":
            opcion_uno()
            
        elif ingresar=="2":
            total_ventas=cant_total()
            print(f"Total de venta: ${total_ventas:.2f}")
        elif ingresar=="3":
            promedio_ventas= promedio()
            print(f"Promedio de ventas: ${promedio_ventas:.2f}")
            
        elif ingresar=="4":
            max,min= ventas_max_min()
            if max is not None and min is not None:
                    print(f"Venta más alta: ${max:.2f}")
                    print(f"Venta más baja: ${min:.2f}")
        
        elif ingresar =="5":
            print("Gracias, hasta luego!")
        else:
            print("Por favor, presione valores entre 1 y 5")

imprimir_menu()


