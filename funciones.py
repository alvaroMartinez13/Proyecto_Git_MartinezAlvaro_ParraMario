def solo_numeros(mensaje):
    while True:
        try:
            valido = int(campo_no_vacio(mensaje))

            if valido > 0:
                return valido
            else:
                print("{:^150}".format(Back.BLACK + Fore.CYAN +
                      Style.BRIGHT + "╔══════════════════════════════════════╗"))
                print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.WHITE +
                      "           Debes digitar solo números positivos          " + Fore.CYAN + "║"))
                print("{:^150}".format(Back.BLACK + Fore.CYAN +
                      Style.BRIGHT + "╚══════════════════════════════════════╝"))
                # print("Debes digitar solo números positivos")

        except Exception as e:
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.WHITE +
                  "           Debes digitar un número entero          " + Fore.CYAN + "║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╚══════════════════════════════════════╝"))
            # print("Debes digitar un número entero")


# Recibe únicamente números en texto, repite cuando no se cumple
def solo_numeros_texto(mensaje):
    while True:
        valido = campo_no_vacio(mensaje)

        if valido.isdigit():
            return valido
        else:
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" +
                  Fore.WHITE + "           Digita unicamente números          " + Fore.CYAN + "║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╚══════════════════════════════════════╝"))
            # print("Digita unicamente números")


# No acepta que se dejen espacios, repite cuando no se cumple
def sin_espacios(mensaje):
    while True:

        valido = campo_no_vacio(mensaje)

        if ' ' in valido:
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.WHITE +
                  "           Debes digitar información sin espacios          " + Fore.CYAN + "║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╚══════════════════════════════════════╝"))
            # print("Debes digitar información sin espacios")
        else:
            return valido


# Valida que en los campos tenga información, sino repite cuando no se cumple
def campo_no_vacio(mensaje):

    while True:

        valido = input(mensaje)

        if valido.strip():
            return valido
        else:
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.WHITE +
                  "           No puedes omitir sin acceder información requerida          " + Fore.CYAN + "║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╚══════════════════════════════════════╝"))
            # print("No puedes omitir sin acceder información requerida")


# Solo acepta texto y sin caracteres especiales
def solo_texto(mensaje):
    while True:

        patron = re.compile(r"[a-zA-ZáéíóúñÑ ]+$")

        valido = campo_no_vacio(mensaje)

        if patron.match(valido):
            return valido
        else:
            print("No se acepta números o caracteres especiales")

            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.WHITE +
                  "           No se acepta números o caracteres especiales          " + Fore.CYAN + "║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN +
                  Style.BRIGHT + "╚══════════════════════════════════════╝"))
            # print("No se acepta números o caracteres especiales")

