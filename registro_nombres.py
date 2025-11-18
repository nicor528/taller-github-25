archivo = open("nombres.txt", "w")
archivo.write("María\n")
archivo.write("Carlos\n")
archivo.write("Lucía\n")
archivo.write(input("Ingresu su nombre: ").title())
archivo.close()

archivo = open("nombres.txt", "r")
print("Contenido del archivo:")
for linea in archivo:
    print(linea.strip())
archivo.close()