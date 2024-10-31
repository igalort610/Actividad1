import funciones_auxiliares as f

f.pedir_nombre()

opcion = f.pedir_opcion()
while (f.opcion_no_valida(opcion)):
    f.mostrar_mensaje_opcion_no_valida()
    opcion = f.pedir_opcion()

if(opcion == 1):
    año = f.año_de_contratacion()
    while (f.año_no_posible(año)):
        f.mostrar_mensaje_de_año_no_valido
        año = f.año_de_contratacion()
       
    