"""Elaborar un algoritmo que permita calcular el número de micro discos 3 .5
necesarios para hacer una copia de seguridad, de la información almacenada en
un disco cuya capacidad se conoce. Hay que considerar que el disco duro está
lleno de información, además expresado en gigabyte. Un micro disco tiene 1.44
megabyte y un gigabyte es igual a 1,024 megabyte"""


GB=float(input("Ingrese la capacidad del disco en GB ")) #capacidad de disco del almacenamiento 


mg=GB*1024 # GB a megabyte

CD=round(mg/1.44,2) #cantidad de disco necesarios 

print(f"cantidad de discos necesarios {CD} megabyte")

