España = {}
provincia = "azul"
while (provincia != "" ):
    provincia = input("introduzca el nombre de la provincia: ")
    muerto_covid = int(input(f"numero de muertos por covid en {provincia} :")) 
    España[provincia] = muerto_covid
    provincia = input("introduzca el nombre de la provincia: ")
    
print (España())

    
    
    
    
    
    
