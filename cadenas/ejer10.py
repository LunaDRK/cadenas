"""Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""

productos = input("separa por comas los productos que necesitas:")
lista_productos = productos.split(",")
numero_productos = len(lista_productos)
contador = 0
while contador < numero_productos:
    print(lista_productos[contador])
    contador += 1
