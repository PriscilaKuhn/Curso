"""2. Escribe un programa que solicite al usuario una frase y luego muestre la frase
invertida."""

#Solicitar
frase= input("Ingresar una frase: ")

#Inicializar
frase_invertida=""

for i in range(len(frase)-1,-1,-1):
    #Agregar el caracter actual a la frase invertida
    frase_invertida+= frase[i] #concatenar cada letra de frase

#Imprimir
print("La frase invertida: ",frase_invertida)
