"""Lea un valor de temperatura t y un código p que puede ser 1 o 2. Si el código es 1
convierta la temperatura t de grados f a grados c con la fórmula c=5/9(t-32). Si el
código es 2 convierta la temperatura t de grados c a f con la fórmula: f=32+9t/5,
caso contrario muestre un mensaje de error."""

valor_t=float(input("Ingrese el valor de la temperatura "))
codigo=int(input("Ingrese código "))

if codigo==1 or codigo==2:
    if codigo==1:
        temperatura_c=5/9*(valor_t-32)
        print(temperatura_c)
    else:
        temperatura_f=32+9*valor_t/5
        print(temperatura_f)

else:
    print(" Error! Por favor vuelva a ingresar, los valores 1 o 2 ")
