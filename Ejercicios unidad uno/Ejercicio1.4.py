
"""Elaborar un algoritmo que permita ingresar el número de partidos ganados,
perdidos y empatados, por ABC club en el torneo apertura, se debe de mostrar su
puntaje total, teniendo en cuenta que por cada partido ganado obtendrá 3 puntos,
empatado 1 punto y perdido 0 puntos."""

partidos_ganados=int(input("Ingrese la cantidad de partidos ganados "))
partidos_perdidos=int(input("Ingrese la cantidad de partidos perdidos "))
partidos_empatados=int(input("Ingrese la cantidad de partidos empatados "))

puntaje_total= ((partidos_ganados*3)+(partidos_perdidos*1)+(partidos_empatados*0))

print("El puntaje final es :" , puntaje_total)