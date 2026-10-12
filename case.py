def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1.Gestionar Recambios")
        print("2. Gestionar Correas")
        print("3.Condiciones de la sala")
        print("4. Salas controladas por cada UTA")
        print("5. Salir")

        opcion = input("Seleccione una opción:(1, 2 ,3, 4 o 5) ")
        match opcion:
            case "1":
                recambios()
            case "2":
                correas()
            case "3":
                condiciones_sala()
            case "4":
                salas_por_uta()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")  

def recambios():
    almacen = {}
    almacen ["Abrazadera bosch ref 8935118612"] = (57102143,"P-2D-07-05")
    almacen ["Abrazadera cierre nucha AISI-316L"] = (57345515,"P-5D-07-00")
    almacen ["Abrazadera clamp 1/2 pulgada SH inox 316L"] = (4207741,"P-6E-04-01")
    almacen ["Abrazadera 2 1/2 pulgadas  sh inox 316L"] = (57102143,"P-6E-04-08")
    almacen ["Abrazadera clamp 3 piezas 1- 1/2 pulgada"] = (57304122,"P-6E-04-04")
    almacen ["Abrazadera clamp 3 piezas 2 pulgadas"] = (57304122,"P-6E-04-07")
    almacen ["Abrazadera clamp 5 pulgadas sh inox 316L"] = (42007948,"P-6E-04-04")
    almacen ["Abrazadera clamp 6 pulgadas sh inox 316L"] = (4207915,"P-6E-05-05")
    almacen ["Abrazadera clamp DN 200 sh inox 316L"] = (4207979,"P-6E-05-05")
    almacen ["Abrazadera clamp DN 20 sh inox 316L"] = (4207742,"P-6E-04-02")
    almacen ["Abrazadera clamp DN 80 sh inox 316L"] = (4207789,"P-6E-05-02")





    print("=== SISTEMA DE GESTIÓN DE RECAMBIOS DE MILLÁN ===")
    texto_buscado = input("Que componente deseas buscar? :")

    print(f"Buscando coincidencias para: '{texto_buscado}'...\n")
    encontrados = False


    for componente, (codigo,ubicacion) in almacen.items():
        if texto_buscado.lower() in componente.lower():
            print(f"Encontrado : {componente}")
            print(f"-> codigo : {codigo} | ubicacion : {ubicacion} \n")
            encontrados = True
    
    if not encontrados:
        print("No se ha podido encontrar el material")


def correas():
    lista = {}
    lista ["uta03"] = ("correa_A", 2)
    lista ["uta04"] = ("correa_A", 3)
    lista ["uta05"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta06"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta07"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta08"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta09"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta10"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta11"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta12"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta13"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta14"] = ("correa_B", 2, "correa_C", 3)
    lista ["uta15"] = ("correa_B", 2, "correa_C", 3)

    print("=== SISTEMA DE GESTIÓN DE CORREAS DE MILLÁN ===")
    texto_buscado = input("De que equipo quieres saber las correas que usa? :")
    
    print(f"Buscando coincidencias para: '{texto_buscado}'...\n")
    encontrados = False


    for equipo, datos in lista.items():
         if texto_buscado.lower() in equipo.lower():
            print(f"Encontrado : {equipo}")
            print(f"->correas : {datos}")
            encontrados = True
    
    if not encontrados:
        print("No se ha podido encontrar el material")




def condiciones_sala():
    lista_sala = {}
    lista_sala ["N1019"] = (18, 26, 25, 60, 100, 10)
    
    print("===CONDICIONES DE LA SALA ===")
    texto_buscado = input("De que sala quieres saber las condiciones? :")

    print(f"Buscando coincidencias para: '{texto_buscado}'...\n")
    encontrados = False

    for sala, (temp_min, temp_max, humedad, pres_min, pres_max, pres_dif) in lista_sala.items():
        if texto_buscado.lower() in sala.lower():
            encontrados = True
            print(f"sala_encontrada : {sala}")
            print(f"Temperatura_minima:{temp_min} ºC")
            print(f"Temperatura_maxima:{temp_max} ºC")
            print(f"Humedad:{humedad} %")
            print(f"Presion_minima:{pres_min}Pa")
            print(f"Presion_maxima:{pres_max}Pa")
            print(f"Presion_diferencial:{pres_dif}Pa")

def salas_por_uta():
    salas_uta = {}

    salas_uta ["01"] = ("N1024", "N1026", "N1028", "N1030", "N1031", "N1032", "N1033", "N1052", "N1054")
    salas_uta ["02"] = ("N1023",)
    salas_uta ["03"] = ("N1011",)
    salas_uta ["04"] = ("N1005",)
    salas_uta ["05"] = ("N1001", "N1002", "1004", "N1009", "N1010", "N1029")


    print("=== SALAS POR UTA ===")
    texto_buscado = input("De que UTA quieres saber las salas que tiene asignadas? :")

    print(f"Buscando coincidencias para: '{texto_buscado}'...\n")
    encontrados = False

    if texto_buscado.lower() == "completo":
        print("\n=== DICCIONARIO COMPLETO DE UTAS ===")
        print(salas_uta)

    for uta, salas in salas_uta.items():
        if texto_buscado.lower() in uta.lower():
            encontrados = True
            print(f"UTA: {uta} -> Salas: {', '.join(salas)}") ## {', '.join(salas) le estoy dicien que me muestre todos los elementos del parentesis separados por comas y espacio}

    if not encontrados:
        print("No se ha podido encontrar la uta")
menu_principal()