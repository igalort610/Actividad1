
numero = 1
comercio = []
nombre_comercial = input("introduzca el nombre de comercial: ")
while (numero != 5):
    dia = ("x")
    if (numero == 1):
        dia = ("(L)")
    if (numero == 2):
        dia = ("(M)")
    if (numero == 3):
        dia = ("(X)")
    if (numero == 4):
        dia = ("(J)")
    if (numero == 5):
        dia = ("(V)")
    comercio.append(int(input(f"Venta{dia}:")))
    numero = numero +1
   