"""Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @)
pero con dominio ceu.es."""

correo = input("Correo Electronico:")
partes_correo = correo.split("@")
nombre = partes_correo[0]
nuevo_correo = nombre + "@ceu.es"
print(f"El nuevo correo es:{nuevo_correo}")