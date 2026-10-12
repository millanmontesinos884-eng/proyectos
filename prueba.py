
def prueba():
    entrada = input("Introduce la hora")
    hora = int(entrada)
    if 12 <= hora < 21:
        print("Estas en la tarde ") 
    elif 21 < hora < 24 or 0 < hora < 6:
        print("Estas en la noche")
    else:
        print("Estas en la mañana")

    return 0
prueba()