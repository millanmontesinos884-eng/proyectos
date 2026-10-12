
def correas():
    lista = {}
    lista ["uta03"] = ("correa_A", 2)
    lista ["uta04"] = ("correa_A", 3)
    lista ["uta05"] = ("correa_B", 2, "correa_C", 3)

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
correas()
