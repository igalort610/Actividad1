numero_ingresado = {}
numero = 0
numero_longitud = 0
while(numero != "END" ):
        numero = input("introduce el numero que quieras añadir, si quieres terminar escriba END ")
        if (numero.isdigit()): 
                if numero in numero_ingresado:
                        numero_ingresado [numero] += 1
                else:
                        numero_ingresado [numero] = 1

    
print(len(numero_ingresado))

    
    
