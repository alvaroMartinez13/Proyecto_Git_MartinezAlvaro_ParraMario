from menu import *
from funciones import *
from config import *
from ciudad import *




while True:
    menu_principal()
    op = pedir_opcion()
    
    if op == 5:
        print("--"*20)
        print("Adios!!")
        print("--"*20)
        break
    if op == 1:
        while True:
            menu_registrar()
            op1 = pedir_opcion()

            if op1 == 1:
                print("--"*20)
                datos = agregar_usuario(datos)
                print("--"*20)
            elif op1 == 2:
                print("--"*20)
                buscar_usuario(datos)
                print("--"*20)
            elif op1 == 3:
                print("--"*20)
                datos = eliminar_usuario(datos)
                print("--"*20)
            elif op1 == 4:
                print("--"*20)
                datos = modificar_usuario(datos)
                print("--"*20)
            elif op1 == 5:
                break
            else:
                print("Opción no válida")
