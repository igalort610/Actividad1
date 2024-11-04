import funciones_auxiliares as f
from datetime import datetime 

año_actual = datetime.now().year 
a1 = int(año_actual)
 
sueldo_asalariado = 1000
nombre = f.pedir_nombre()

opcion = f.pedir_opcion()
while (f.opcion_no_valida(opcion)):
    f.mostrar_mensaje_opcion_no_valida()
    opcion = f.pedir_opcion()

if(opcion == 1):
    año = f.año_de_contratacion()
#    print("skill_issue::if::año = ", año)
    while (f.año_no_posible(año)):
        f.mostrar_mensaje_de_año_no_valido
        año = f.año_de_contratacion()
    sueldo = f.sueldo_asalariado(a1,año)    
    print ("El sueldo de ", nombre , " \n total =" , sueldo)
       
elif(opcion == 2):
    comisiones = f.comisiones()
    while(f.comisiones_no_posibles)
        