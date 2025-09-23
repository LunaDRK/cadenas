"""Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por
pantalla el número de teléfono sin el prefijo y la extensión."""

telefono = input("Telefono con codigo de pais y extension:")
separar_numero = telefono.split("-")
numero = separar_numero[1]
print(f"El numero de telefono es: {numero}")