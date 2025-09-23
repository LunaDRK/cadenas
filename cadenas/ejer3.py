"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que
el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE>
es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre."""

nombre = input("Introducir nombre:")
numero_letras = len(nombre)
contador = 0
numero_mayusculas = 0

while contador < numero_letras:
    if nombre[contador].isupper():
        numero_mayusculas += 1
    contador+=1

print(f"tu nombre tiene {numero_mayusculas} mayusculas y tiene {numero_letras} letras")