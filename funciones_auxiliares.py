from datetime import datetime 

año_actual = datetime.now().year 

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

def año_no_posible(año):
    peru = int(año_actual)
    print("funciones_auxiliares::año_posible::",año, " - ", type(año))
    print("funciones_auxiliares::año_posible::",peru, " - ", type(peru))
     
    return año <= peru 

def mostrar_mensaje_de_año_no_valido():
    print("El año seleccionado no es correcto debe ser un año igual  a " + año_actual + " o menor")