import funciones_banco as f

a = f.deposito()

while (f.deposito_inrreal(a)):
    f.msg_deposito_incorrecto(a)
    a = f.deposito()

p = f.taza()

while (f.taza_no_posible(p)):
    f.msg_taza_no_posible(p)
    p = f.taza() 
    
n = f.años()

while (f.años_no_posible(n)):
    f.msg_año_imposible(n)
    n = f.años()
    
f.imprimir_linea()
print (a , "        " , type(a))
print (n , "            " , type(n))
print (p, "       ", type (p))       
f.imprimir_resultados(a,n,p)