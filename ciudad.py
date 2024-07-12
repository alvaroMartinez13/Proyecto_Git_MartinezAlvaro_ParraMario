import config

ciudad = "ciudad.json"

datos_ciudad = config.cargar_datos(ciudad)

#Si existe ciudad, no se deja crear
def existe_ciudad(clave, valorNuevo):
    for ciudad_existente in datos_ciudad["ciudad"]:
        if ciudad_existente[clave] == valorNuevo:
            print("Valor existe")
            return False
    return True

#Agrega una ciudad
def nueva_ciudad(nuevaCiudad):
    print(nuevaCiudad["nombre"])
    existe = existe_ciudad("nombre", nuevaCiudad["nombre"])
    if existe is False:
        print("Ya existe la ciudad")
        return False
    
    datos_ciudad["ciudad"].append(nuevaCiudad)

    config.guardar_datos(datos_ciudad, ciudad)

    return f"Nueva ciudad {nuevaCiudad['nombre']}"

def ver_ciudades():
    for ciudad_existente in datos_ciudad["ciudad"]:
        print(f"Ciudad: {ciudad_existente['nombre']} Código postal: {ciudad_existente['codigo_postal']} Poblacion estimada: {ciudad_existente['poblacion_estimada']} Pais: {ciudad_existente['pais']}")

def edita_ciudad(clave, valorAntiguo, valorNuevo):
    print()
    




