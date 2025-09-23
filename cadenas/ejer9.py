"""Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también
funcione cuando el día o el mes se introduzcan con un solo carácter."""

fecha = input("ingresa fecha de nacimeiento como dd/mm/aaaa:")
fecha_separada = fecha.split("/")
contador = 0
while contador < 3:
    print(f"tu dia es:{fecha_separada[0]} y mes {fecha_separada[1]} y año {fecha_separada[2]}")
    contador += 1
    break