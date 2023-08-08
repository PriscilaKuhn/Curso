"""Obtener la liquidación del sueldo de un empleado y sus detalles, teniendo en
cuenta que:
● La empresa empleadora, bonifica sobre el sueldo básico (SB) la
antigüedad del empleado con un 1.2% por año. Además, paga el
presentismo con un monto fijo (MP).
● Entre los descuentos, se deben contabilizar: el aporte jubilatorio (AJ)
que representa un 11% del sueldo básico; aporte a obra social (OS) con un
3% del básico y el aporte gremial (AG) con un 1% del básico.
● El empleador paga además $ 800.00 por cónyuge y $ 400.00 por cada
hijo.
● Son datos del problema: nombre y apellido del empleado, DNI, sueldo
básico, antigüedad en años, estado civil ( 1 si es casado, 0 si es soltero ),
número de hijos, presentismo ( 1 si corresponde cobrar, 0 si no cobra ).
Obtenga una salida con mensajes alusivos describiendo los haberes, los
descuentos y el sueldo neto a cobrar."""

nombre_apellido=(input("Ingrese el nombre y el apellido del empleado "))
dni=int(input("Ingrese el documento del empleado "))
SB=int(input("Ingrese el sueldo básico del empleado "))
cant_anios=int(input("Ingrese la cantidad de años que este empleador trabaja en la empresa "))
estado_civil=int(input("Ingrese el estado civil [1 si es casado], [0 si es soltero] ) "))
cant_hijos=int(input("ingrese la cantidad de hijos si es que tiene "))
presentismo=int(input("Presentismo: [1 si corresponde cobrar] , [0 si no cobra ]) "))

Aporte_jubilatorio= 0.11*SB
Obra_social= 0.03*SB
Aporte_gremial=0.01*SB


conyuge=estado_civil*800.00
hijos=cant_hijos*400.00

if presentismo==1:
        monto_fijo=int(input("Ingrese el monto fijo del presentismo "))
else:
        monto_fijo=0
    
 
haberes= SB*(0.012*cant_anios ) + monto_fijo + conyuge + hijos
descuento= Aporte_jubilatorio+Obra_social+Aporte_gremial
sueldo_neto= haberes-descuento

print("Haberes:" ,haberes)
print("Descuento", descuento)
print("La liquidación de sueldo de ", nombre_apellido, "con dni", dni,  ", es de: " ,sueldo_neto, "pesos")