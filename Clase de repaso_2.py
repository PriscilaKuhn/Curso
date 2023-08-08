"""Imprimir por pantalla la siguiente sucesion numerica 1,99,2,98,3,97,4,96,5,95   
-Tener en cuenta que el ultimo valor no tiene coma
-Utilizar estrucutra iteractivas"""

cont_max=0
cont_min=100

while True:
    cont_max+=1
    cont_min-=1
    print(f"{cont_max},{cont_min}", end=",", end="")
    if cont_max==5 and cont_min==95:
        break
