import json

def cargar():
    try:
        with open('Quiniela', 'r') as archivo:
            general = json.loads(archivo.read())
        print("Datos recuperados")
        return general
    except IOError:
        print("Se está iniciando por primera vez")
        return {}

def guardar_carga(datos):
    with open('Quiniela', 'w') as archivo:
        archivo.write(json.dumps(datos))

def imprimir_menu():
    print("*******************")
    print("Quiniela [NOMBRE]")
    print("*******************")
    print(" \n MENÚ:\n ")
    print("Puede escoger entre el 1 y el 5, las opciones que ofrecemos son:\n")
    print("Presione 1 para jugar a la Quiniela")
    print("Presione 2 para jugar al Quini 6")
    print("Presione 3 para comprobar si la apuesta es ganadora o no")
    print("Presione 4 para el arqueo de caja")
    print("Presione 5 para salir") 

def opcion_uno(ingresar, datos):
    if 0 < ingresar < 100:
        datos['apuesta_dos_cifras'] = ingresar
    elif 1000 < ingresar < 10000:
        datos['apuesta_cuatro_cifras'] = ingresar
    elif 100000 < ingresar < 1000000:
        datos['apuesta_seis_cifras'] = ingresar
    else:
        print("ERROR!. Solo puedes escoger para apostar números de 2, 4 o 6 cifras")

def mostrar(datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

nombre_quiniela = ''
fecha = ''
hora = ''
comprobante = ''
dni = ''
cifra = ''
jugada = ''

datos = {'nombre_quiniela': nombre_quiniela, 'fecha': fecha, 'hora': hora,
         'comprobante': comprobante, 'dni': dni, 'cifra': cifra, 'jugada': jugada}

def opcion_cinco():
    print("Su elección fue salir. Adiós!")
    return datos

imprimir_menu()

eleccion = int(input("Ingresar la opción: "))

datos = cargar()

while eleccion != 5:
    if eleccion < 1 or eleccion > 5:
        print("¡Error! Vuelve a ingresar otra opción, entre los números 1 y 5 ")
        imprimir_menu()
    elif eleccion == 1:
        print("Puedes escoger entre apostar números de 2, 4 o 6 cifras.")
        ingresar = int(input("Ingresar números: "))
        opcion_uno(ingresar, datos)
        mostrar(datos)
    elif eleccion == 5:
        datos = opcion_cinco()

    guardar_carga(datos)
    imprimir_menu()
    eleccion = int(input("Ingresar la opción: "))
