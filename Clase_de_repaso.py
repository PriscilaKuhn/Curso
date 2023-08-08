lista=["F","M", "S","K","L"]

for i in range(len(lista)): #Si desconozco la cantidad de elementos
    print(lista[i])

print("Segunda forma")

for letra in lista:
    print(letra)

print("Con While")


cont=0
while True:
    print(lista[cont])
    cont+=1
    if cont==5:
        break




