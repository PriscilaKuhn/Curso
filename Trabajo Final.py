#Importar librerias necesarias
import json
from random import randint

#Creación de procedimientos y funciones

def cargar():
    try:
        with open('Quiniela', 'r') as archivo:
            contenido = archivo.read().strip()
            if contenido:
                general = json.loads(contenido)
                print("Datos recuperados")
                return general
            else:
                print("El archivo 'Quiniela' se esta inicializando.")
                return {}
    except IOError:
        print("No se encontró el archivo 'Quiniela'. Se está iniciando por primera vez.")
        return {}
    except json.JSONDecodeError:
        print("El archivo 'Quiniela' no contiene datos válidos en formato JSON.")
        return {} #Esta función me permite crear (si no existe) un archivo de texto o
                  #abrir el archivo denominado ->Quiniela.txt que esta guardado en la máquina, modo lectura. 

def guardar_carga(datos):
    with open('Quiniela', 'w') as archivo:
        for clave, valor in datos.items():
          archivo.write(f"{clave}: {valor}\n") #Me permite escribir sobre el archivo creado o encontrado. 


def imprimir_menu():
    print("        *********************")
    print("       Quiniela SANTO PANCRACIO")
    print("        *********************")
    print("                MENÚ\n               ")
    print("Puede escoger entre el 1 y el 5, las opciones que ofrecemos son:\n")
    print("Presione [1] para jugar a la Quiniela Tradicional")
    print("Presione [2] para jugar al Quini 6")
    print("Presione [3] para comprobar si la apuesta del Quini6 es o no ganadora")
    print("Presione [4] para el arqueo de caja ")
    print("Presione [5] para salir") #Procedimiento

def quiere_menu(imprimir):
    
    if imprimir ==0:
        imprimir_menu()
    else:
        None #Procedimiento

def mostrar(datos):
    print("\n       COMPROBANTE\n")
    for clave, valor in datos.items():
        if clave == 'apuesta':
            print(f"{clave}: {' '.join(map(str, valor))}")
        else:
            print(f"{clave}: {valor}") #Es un procedimiento que me permite imprimir el ticket comprobante cuando se lo necesite.


#Creacción del diccionario con las claves vacías
datos = {
    'apuesta_dos_cifras': None,
    'apuesta_cuatro_cifras': None,
    'apuesta_seis_cifras': None,
    'nombre_quiniela': None,
    'fecha': None,
    'nro_comprobante': None,
    'dni': None,
    'cifra_apostada': None,
    'monto_recaudado': 0  # Inicializamos en 0
}


def cargar_todo(opcion, datos): #Procedimiento, se lo llama cuando se ingresa por teclado la opción 1 y/o 2 del Menú.
    monto_fijo = 600
    nombre_de_quiniela="SANTO PANCRACIO"
    if opcion==1:
        ingresar = int(input("Ingresar números: "))
        
        if 10 <= ingresar < 100:
            datos['apuesta_dos_cifras'] = ingresar
        elif 1000 <= ingresar < 10000:
            datos['apuesta_cuatro_cifras'] = ingresar
        elif 100000 <= ingresar < 1000000:
            datos['apuesta_seis_cifras'] = ingresar
        else:
            print("ERROR!. Solo puedes escoger para apostar números de 2, 4 o 6 cifras")
            return
        cifra=int(input("¿Cuánto apuesta? "))
        datos['nombre_quiniela'] = nombre_de_quiniela
        datos['fecha'] = input("Ingrese la fecha [formato(dd-mm-aaaa)]: ") #Aquí se podria implemetar mejor práctica de programación, por ejemplo que se ingresen datos de tipo datatime.
        datos['nro_comprobante'] = str(randint(1, 100000))  # Generar número de comprobante aleatoriamente
        datos['dni'] = input("Ingrese correctamente el DNI del cliente: ")#Aquí se podria aplicar mejor práctica, para que se ingrese bien el dni, ejemplo: una letra.
        datos['cifra_apostada'] = cifra
        if 'monto_recaudado' not in datos:
            datos['monto_recaudado'] = 0
        datos['monto_recaudado']+=cifra
    elif opcion==2:
        escoger=int(input("Ingrese [0] si deseas escoger seis números para apostar entre 00 y 45 inclusive o ingrese [1] si deseas que los números sean aleatorios: "))   
        apuesta=[]
        if escoger==0:
                for i in range(6):
                 aposto=int(input("Ingresar los números (1 a la vez) que se encuentre entre 00 y 45 inclusive : "))
                 apuesta.append(aposto)
        elif escoger==1:
                for i in range (6):
                 aposto=randint(0,45)

                 apuesta.append(aposto)         
        else:
            print("ERROR! Vuelve a ingresar 0 si deseas escoger los números o 1 si deseas que sean alaetorios")
          
            return
    
        if 'apuesta_dos_cifras' in datos:
            datos['apuesta_dos_cifras'] = None
        if 'apuesta_cuatro_cifras' in datos:
            datos['apuesta_cuatro_cifras'] = None
        if 'apuesta_seis_cifras' in datos:
            datos['apuesta_seis_cifras'] = None
    

        datos['apuesta'] = apuesta #números apostados alatorios o no
        datos['nombre_quiniela'] = nombre_de_quiniela
        datos['fecha'] = input("Ingrese la fecha [formato(dd-mm-aaaa)]:  ")
        datos['nro_comprobante'] = str(randint(100000, 500000))
        datos['dni'] = input("Ingrese correctamente el DNI del cliente: ")
        datos['cifra_apostada'] = monto_fijo
        if 'monto_recaudado' not in datos:
            datos['monto_recaudado'] = 0
        datos['monto_recaudado']+=monto_fijo
    else:
        print("Inválido. Vuelve a intentarlo")

       
def opcion_generar_numeros_ganadores():
    numeros_ganadores=[]
    for i in range(6):
        numero_ganador=randint(0,45)
        numeros_ganadores.append(numero_ganador)
    return numeros_ganadores #Función que me permite generar los números ganadores del día del Quini6.
                             #Se la llama cuando se ingresa la opción 3.


def comparar_listas(apuesta,numeros):# Función que permite comparar las listas de los números del Quini6 apostados                                       
    if len(apuesta) != len(numeros):# posición a posición con los números ganadores del día.
        return False

    for i in range(len(apuesta)):
        if apuesta[i] != numeros[i]:
            return False

    return True    

def apuesta_ganadora(numeros_ganadores):
    if "apuesta" in datos and comparar_listas(datos["apuesta"], numeros_ganadores):
                print("GANASTE LA QUINIELA! ¡FELICITACIONES!")
                print(f"Los números ganadores de la fecha son : {numeros_ganadores}")
    else:
                print(f"Los números ganadores de la fecha son : {numeros_ganadores}")
                print("LO SIENTO NO ACERTASTE NINGÚN NÚMERO. Mejor suerte para la próxima.") #Procedimiento, imprime si la apuesta es o no ganadora.



def arqueo_de_caja():
    porcentaje_estado = 0.47
    ganancia_estado= datos['monto_recaudado']* porcentaje_estado
    ganancia_quiniela =datos['monto_recaudado'] - ganancia_estado

    print(f"Monto recaudado: {datos['monto_recaudado']} pesos")
    print(f"Ganancia para el Estado: {ganancia_estado}") 
    print(f"Ganancia para la Quiniela SANTO PANCRACIO: {ganancia_quiniela}")
    return ganancia_estado, ganancia_quiniela #Función, me permite calcular la recaudación diaria en apuestas y otros calculos más.
                                                #Se la llama cuando se ingresa la opción 4. 


def opcion_cinco():
    print("Su elección fue salir. Adiós!")
    return datos    #Función que guarda los datos ingresados.



#A partir de esta línea se encuentra el programa principal. 
 
imprimir_menu()

eleccion = int(input("Ingresar la opción: "))

datos = cargar()


while eleccion != 5:

    if eleccion < 1 or eleccion > 5:
        print("¡Error! Vuelve a ingresar otra opción, entre los números [1] y [5] ")
        imprimir_menu()
        eleccion = int(input("Ingresar la opción: "))
    if eleccion == 1:
        print("Puedes escoger entre apostar números de 2, 4 o 6 cifras.")
        cargar_todo(eleccion,datos)
        mostrar(datos)
        imprimir=int(input("Ingrese [0] si quiere volver a consultar el menú. De no ser asi presione cualquier [otro número positivo] para seguir avanzando."))
        quiere_menu(imprimir)
        eleccion = int(input("Ingresar la opción: "))
    elif eleccion==2:
        cargar_todo(eleccion,datos)
        mostrar(datos)
        imprimir=int(input("Ingrese [0] si quiere volver a consultar el menú. De no ser asi presione cualquier [otro número positivo] para seguir avanzando."))
        quiere_menu(imprimir)
        eleccion = int(input("Ingresar la opción: "))
    elif eleccion==3:
        numeros_ganadores=opcion_generar_numeros_ganadores()
        apuesta_ganadora(numeros_ganadores)
        imprimir=int(input("Ingrese [0] si quiere volver a consultar el menú. De no ser asi presione cualquier [otro número positivo] para seguir avanzando."))
        quiere_menu(imprimir)
        eleccion = int(input("Ingresar la opción: "))
    elif eleccion==4: 
        ganancia_estado, ganancia_quiniela = arqueo_de_caja()
        imprimir=int(input("Ingrese [0] si quiere volver a consultar el menú. De no ser asi presione cualquier [otro número positivo] para seguir avanzando."))
        quiere_menu(imprimir)
        eleccion = int(input("Ingresar la opción: "))
    else:
        print("Opción inválida. Vuelve a intentarlo.")
        imprimir=int(input("Ingrese [0] si quiere volver a consultar el menú. De no ser asi presione cualquier [otro número positivo] para seguir avanzando."))
        quiere_menu(imprimir)
        eleccion = int(input("Ingresar la opción: "))
if eleccion == 5:
        datos = opcion_cinco()



guardar_carga(datos)



 
