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
                nombre= campo_no_vacio("Ingrese nombre de la ciudad: ")
                codigo_postal= solo_numeros("Ingrese codigo postal de la ciudad: ")
                poblacion_estimada= solo_numeros("Ingrese la poblaicon de la ciudad: ")
                pais= campo_no_vacio("Ingrese nombre del Pais: ")
                ciudad={
                    "nombre": nombre,
                    "codigo_postal": codigo_postal,
                    "poblacion_estimada": poblacion_estimada,
                    "pais": pais
                }
                existe = nueva_ciudad(ciudad)
                if existe is False:
                    print("Ciudad ya existe")
                    print("selecciona otra opcion")
                    
                else:
                    print(existe)

                print("--"*20)
            elif op1 == 2:
                print("--"*20)
                ver_ciudades()
                nombre_ciudad = campo_no_vacio("Ingrese nombre de la ciudad: ")
                ciudad_busqueda = busqueda_ciudad(nombre_ciudad)
                if ciudad_busqueda:
                    print("1.Nombre, 2.Codigo Postal, 3.Poblacion, 4.Pais")
                    op1 = solo_numeros("Ingrese la opcion: ")
                    if op1 == 1:
                        nombre_nuevo = campo_no_vacio("ingrese el nuevo nombre: ")
                        if nombre_nuevo != ciudad("nombre"):
                            edita_ciudad("nombre", nombre_ciudad, nombre_nuevo)
                        else:
                            print("El nombre es el mismo")
                    elif op1 == 2:
                        codigo_postal_nuevo = solo_numeros("Ingrese el nuevo codigo postal de la ciudad: ")
                        if codigo_postal_nuevo != ciudad("codigo_postal"):
                            edita_ciudad("codigo_postal",codigo_postal,codigo_postal_nuevo) 
                        else:
                            print("El codigo es el mismo")
                    elif op1 == 3:
                        poblacion_estimada_nueva= solo_numeros("Ingrese la nueva poblaicon de la ciudad: ")
                        if poblacion_estimada_nueva != ciudad("poblacion_estimada"):
                            edita_ciudad("poblacion_estimada", poblacion_estimada, poblacion_estimada_nueva)
                        else:
                            print("La catidad de poblacion es la misma")
                    elif op1 == 4: 
                        pais_nuevo = campo_no_vacio("Ingrese nombre del nuevo  Pais: ")
                        if pais_nuevo != ciudad("pais"):
                            edita_ciudad("pais", pais, pais_nuevo)
                        else:
                            print("El nombre del pais es el mismo")

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
