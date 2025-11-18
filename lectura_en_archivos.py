archivo = open("datos.txt", "r")
print(archivo)

#lectura de archivos
#texto = archivo.read()
#print(texto)

#lectura de datos por linea
lineas = archivo.readlines()
print(lineas)
for linea in lineas:
    print(f"Linea: {linea.strip()}")