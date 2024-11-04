numero = int(input("Dime un número"))
resultado = numero
limite = int(input("dime el limite"))
multiplicado = int(input("dime cada cuanto avanza"))
while(resultado <= limite):
    print(resultado)
    resultado = multiplicado * numero 
    multiplicado = 1 + multiplicado 
    
print("el limite es " , multiplicado)    
     