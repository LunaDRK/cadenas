""" Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido"""
import sys

sys.argv[0]
nombre = sys.argv[1]
numero = int(sys.argv[2])
contador = 0

while contador < numero:
    print(nombre)
    contador+= 1