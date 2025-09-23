"""Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola
y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

frase = input("frase con una vocal al final:")
vocales = "a", "e", "i", "o", "u"
frase_vocal = frase[-1]

if frase_vocal in vocales:
    print(frase)
    vocal_mayuscula = frase_vocal.upper()
    print(f"vocal en mayuscula: {vocal_mayuscula}")
else:
    print("Introduce una vocal al final de la frase")