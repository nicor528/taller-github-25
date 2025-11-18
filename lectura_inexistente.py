try:
    archivo = open("datos2.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
    archivo.close()
except FileNotFoundError:
#except Exception as e:
    print(f"Ocurrió un error: {FileNotFoundError}")
    #print("Error: El archivo 'datos2.txt' no existe.")
    #print("Verificá el nombre o la ubicación del archivo.")