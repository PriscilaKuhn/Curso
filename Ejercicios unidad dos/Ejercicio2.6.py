"""Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. Si la
cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre
700. Muestre el valor total a pagar."""

#Input
cantidad_kw=float(input("Ingrese la cantidad de Kw consumido "))
precio_por_kw=float(input("Ingrese el precio por kw "))

#Proceso y Output
precio=cantidad_kw*precio_por_kw

if cantidad_kw >= 700:

    total=precio+((cantidad_kw-700)*(precio_por_kw*0.05)+precio_por_kw)

    print(f"El precio a pagar es {total}")
else:

    print(precio)

