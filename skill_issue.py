import funciones_auxiliares as f
from datetime import datetime 

año_actual = datetime.now().year 
a1 = int(año_actual)


sueldo = 0
sueldo_asalariado = 1000
sueldo_comisiones = 800
ganancia_por_hora = 8
cotizacion_comision = 10
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
    sueldo = f.sueldo_asalariado(nombre,a1,año)    
   
       
elif(opcion == 2):
    comisiones = f.comisiones()
    while( f.comisiones_no_posibles(comisiones) ):
        f.mostrar_mensaje_no_valido()
        comisiones = f.comisiones()
    f.sueldo_comisiones(nombre,sueldo,sueldo_comisiones,comisiones,cotizacion_comision)
else:
    Horas_trabajadas = f.Horas_trabajadas() 
    while(f.horas_no_posibles(Horas_trabajadas)):
        f.mostrar_mensaje_horas_no_validas()
        Horas_trabajadas = f.Horas_trabajadas()
    f.sueldo_horas_trabajadas(nombre,Horas_trabajadas,ganancia_por_hora)
    