from datetime import datetime 

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
    return opcion >= 1 and opcion >= 3

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
    print("El año seleccionado no es correcto debe ser un año igual  a " + año_actual + " o menor")
    
def sueldo_asalariado(a1,año): 
    sueldo = sueldo_base + ((a1 - año) * 100)
    return sueldo

def comisiones()
    comisiones = int(input("numerio de comiciones = "))
    print ("este mes has vendido ", comisiones , "totales")
    return comisiones 