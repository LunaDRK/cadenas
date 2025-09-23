"""Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con
dos decimales y muestre por pantalla el número de euros y el número de céntimos
del precio introducido."""

precio = input("ingresar precio del producto:")
centimos = precio.split(".")
euros = centimos[0]
centimos = centimos[1]
print(f"el precio del producto es de {euros} euros y {centimos} centimos")