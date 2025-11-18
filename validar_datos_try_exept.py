print("=== Calculadora de División ===")
try:
    numerador = float(input("Ingresá el numerador: "))
    denominador = float(input("Ingresá el denominador: "))
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado:.2f}")
except ValueError:
    print("[ERROR] Debés ingresar valores numéricos válidos.")
except ZeroDivisionError:
    print("[ERROR] El denominador no puede ser cero.")
    print(" Intentá nuevamente.")
print("Gracias por usar la calculadora.")
