import funciones_auxiliares as f

def prueba_año_posible():
    valor_esperado = True
    año = 2026
    valor_obtenido = f.año_no_posible(año)
    
    print("Valor esperado:", valor_esperado, "; Valor obtenido:", valor_obtenido)
    
# ---------------------------

prueba_año_posible()