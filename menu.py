def menu_principal():
    print("")
    print("=="* 20)
    print("          BuscarCity")
    print("=="* 20)
    print("")
    print("     1. Registrar Ciudad")
    print("     2. Buscar Ciudad")
    print("     3. Filtrar")
    print("     4. Exportar Lista")
    print("     5. Salir")
    print("=="* 20)
    print("")

def menu_registrar():
    print("")
    print("=="* 20)
    print("          Registrar")
    print("=="* 20)
    print("")
    print("     1. Agregar ciudad")
    print("     2. Editar Ciudad")
    print("     3. Informacion Ciudad")
    print("     4. Salir")
    print("=="* 20)
    print("")

def menu_buscar():
    print("")
    print("=="* 20)
    print("          Buscar")
    print("=="* 20)
    print("")
    print("     1. Buscar ciudad")
    print("     2. Salir")
    print("=="* 20)
    print("")

def menu_filtrar():
    print("")
    print("=="* 20)
    print("          Filtrar")
    print("=="* 20)
    print("")
    print("     1. Busqueda Avazado  por Nombre, Pais o codigo postal")
    print("     2. Fitrar Datos por Poblacion Mayor o Menor")
    print("     3. Salir")
    print("=="* 20)
    print("")

def menu_filtrar():
    print("")
    print("=="* 20)
    print("          Exportar")
    print("=="* 20)
    print("")
    print("     1. Exportar lista ciudades")
    print("     2. Salir")
    print("=="* 20)
    print("")

def pedir_opcion():
    try:
        print("//"*20)
        op = int(input("  Ingrese su opcion: "))
        print("//"*20)
        
        return op
        
    except Exception:
        print("--"*20)
        print("valor invalido")