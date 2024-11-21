
def agregarnumeros(cantidad_numeros,total_numeros):
    total_numeros = input("¿Cuantos números se insertarán?")
 
    for i in range(total_numeros):
        numeros = input("Número:")
        cantidad_numeros.append(numeros) 
    return cantidad_numeros

 