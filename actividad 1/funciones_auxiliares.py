from datetime import datetime 

sueldo = 0
sueldo_asalariado = 1000
sueldo_comisiones = 800
ganancia_por_hora = 8
cotizacion_comision = 10
año_actual = datetime.now().year 
sueldo_base = 1000

def añoactual(año_actual):
    return año_actual


def pedir_nombre():
    nombre = input("Nombre del empleado:")
    return nombre  
    
def pedir_opcion():
    opcion = int(input("""Que tipo de empleado eres:
                    1 = Asalariado 
                    2 = Comisionado 
                    3 = Por horas
                    Opción (1, 2 ,3)"""))
    return opcion

def opcion_no_valida(opcion):
    return opcion >= 1 and opcion > 3

def mostrar_mensaje_opcion_no_valida():
    print("La opción no está dentro de los parámentros correctos -->(1|2|3)")

def año_de_contratacion():
    año =  int(input("Año de contratación: ")) 
    return año

def año_no_posible(año):

    a1 = int(año)
    a2 = int(año_actual)
#    print("funciones_auxiliares::año_posible::",a1, " - ", type(a1))
#    print("funciones_auxiliares::año_posible::",a2, " - ", type(a2))
     
    return a1 > a2 

def mostrar_mensaje_de_año_no_valido():
    print("El año seleccionado no es correcto debe ser un año igual  a " , año_actual , " o menor")
    
def sueldo_asalariado(nombre,a1,año): 
    sueldo = sueldo_base + ((a1 - año) * 100)
    print ("El sueldo de ", nombre , " \n total =" , sueldo, "€")

def comisiones():
    comisiones = int(input("numerio de comiciones = "))
    print ("este mes has vendido ", comisiones , "en total")
    return comisiones 

def sueldo_comisiones(nombre,sueldo,sueldo_comisiones,comisiones,cotizacion_comision):
    sueldo = int(sueldo_comisiones + (comisiones * cotizacion_comision))
    print ("El sueldo de ", nombre , " \n total =" , sueldo,"€")
     
def comisiones_no_posibles(comisiones):
    return comisiones < 0

def mostrar_mensaje_no_valido():
    print("para poder cobrar por comisiones debes vender comisiones =/")

def Horas_trabajadas():
    Horas_trabajadas = int(input("numero de horas trabajadas: "))
    return Horas_trabajadas

def horas_no_posibles(Horas_trabajadas):
 return Horas_trabajadas < 0    

def mostrar_mensaje_horas_no_validas():
    print("el numero de horas introducido no es valido debe ser mayor o igual a 0") 

def sueldo_horas_trabajadas(nombre,Horas_trabajadas,ganancia_por_hora):
    sueldo = ganancia_por_hora * Horas_trabajadas
    print ("El sueldo de ", nombre , " \n total =" , sueldo,"€")