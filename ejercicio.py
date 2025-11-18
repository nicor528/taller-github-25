try:
    archivo = open("clientes.txt", "a")
except FileNotFoundError:
    print(FileNotFoundError)
    archivo = open("clientes.txt", "w")

nombre = ""
apellido = ""
mail = ""

try:
    nombre = input("Ingrese su nombre: ")
    if len(nombre) < 1:
        raise ValueError("el nombre no puede estar vacio")
    apellido = input("Ingrese su apellido: ")
    if len(apellido) < 1:
        raise ValueError("el apellido no puede estar vacio")
    mail = input("Ingrese su mail: ")
    arrobas = mail.count("@")
    if arrobas != 1:
        raise ValueError("Mail incorrecto")
    archivo.write(f"{nombre},{apellido},{mail}\n")
    print("Cliente registrado exitosamente.")
except ValueError as e:
    print(f"Se ha producido un error: {e}")

archivo.close()