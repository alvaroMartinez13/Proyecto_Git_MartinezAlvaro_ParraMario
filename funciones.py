#Solo acepta solo números enteros
def solo_numeros(mensaje):
    while True:
        try:
            valido = int(campo_no_vacio(mensaje))

            if valido > 0:
                return valido
            else:
                print("Debes digitar solo números positivos")

        except Exception:
            print("Debes digitar un número entero")


# Recibe únicamente números en texto, repite cuando no se cumple
def solo_numeros_texto(mensaje):
    while True:
        valido = campo_no_vacio(mensaje)

        if valido.isdigit():
            return valido
        else:
            print("Digita unicamente números")


# No acepta que se dejen espacios, repite cuando no se cumple
def sin_espacios(mensaje):
    while True:

        valido = campo_no_vacio(mensaje)

        if ' ' in valido:
            print("Debes digitar información sin espacios")
        else:
            return valido


# Valida que en los campos tenga información, sino repite cuando no se cumple
def campo_no_vacio(mensaje):

    while True:

        valido = input(mensaje)

        if valido.strip():
            return valido
        else:
            print("No puedes omitir sin acceder información requerida")


# Solo acepta texto y sin caracteres especiales
def solo_texto(mensaje):
    while True:

        patron = re.compile(r"[a-zA-ZáéíóúñÑ ]+$")

        valido = campo_no_vacio(mensaje)

        if patron.match(valido):
            return valido
        else:
            print("No se acepta números o caracteres especiales")

