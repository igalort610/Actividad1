def deposito():
    a = float(input("Cantidad a ingresar (€): "))
    return a

def deposito_inrreal(a):
    return a < 0

def msg_deposito_incorrecto(a):
    print("Cantidad a ingresar (la cantidad a ingresar debe ser positiva): ",  f'{a:.2f}' )

def taza():
    p = float(input("Interés (%): "))
    return p

def taza_no_posible(p):
    return p < 0

def msg_taza_no_posible(p):
    print("Tipo de interés (el tipo de intes debe ser positiva): ",  f'{p:.2f}')  

def años():
    n = float(input("Número de años: "))
    return n

def años_no_posible(n):
    return n < 0 

def msg_año_imposible(n):
    print("Años de depósito (los años de depósito deben especificarse con un número positivo): " , f'{n:.2f}')
    
def imprimir_linea():
    print("----" * 8)
 
def imprimir_resultados(a,p,n):
    
    resultado = a*(1+(p/100))**n
    
    print(f""" total a pagar '{resultado:.2f}')  
          """)    