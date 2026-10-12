def recambios():
    almacen = {}
    almacen ["motor"] = (6, 3, 2)
    almacen ["bomba"] = (6, 3, 3)
    almacen ["valvula_reguladora"] = (4, 3, 2)
    almacen ["valvula_manual"] = (3, 2, 1)
    almacen ["tornillos_M5"] = (1, 3, 2)
    almacen ["tornillos_M6"] = (1, 2, 2)
    almacen ["tornillos_M8"] = (1, 2, 3)
    almacen ["contactor"] = (1, 1, 1)
    almacen ["magnetotermico_2P"] = (4, 5, 5)
    almacen ["magnetotermico 3P"] = (5, 5, 5)
    almacen ["magnetotermico 4P"] = (4, 2, 5)
    almacen ["sonda_temperatura"] = (5, 1, 1)
    almacen ["sonda_humedad"] = (5, 1, 2)
    almacen ["sonda_pt100"] = (5, 1, 3)
    almacen ["guantes_latex"] = (5, 1, 4)
    almacen ["guantes proteccion mecanica"] = (5, 1, 5)

    print("=== SISTEMA DE GESTIÓN DE RECAMBIOS DE MILLÁN ===")
    texto_buscado = input("Que componente deseas buscar? :")

    print(f"Buscando coincidencias para: '{texto_buscado}'...\n")
    encontrados = False


    for componente, (pasillo, fila, columna) in almacen.items():
        if texto_buscado.lower() in componente.lower():
            print(f"Encontrado : {componente}")
            print(f"-> pasillo : {pasillo} | fila : {fila} | columna {columna} \n")
            encontrados = True
    
    if not encontrados:
        print("No se ha podido encontrar el material")
recambios()
        
        

