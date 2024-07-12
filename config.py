import json

def cargar_datos(archivo):
    try:
        datos = {}
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception:
        print("Error durante la ejecución. Revisar el log de errores.")
        
        

def guardar_datos(datos, archivo):
    try:
        datos = dict(datos)
        
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception:
        print("Error durante la ejecución. Revisar el log de errores.")

