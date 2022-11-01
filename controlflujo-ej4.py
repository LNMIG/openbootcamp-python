# EJERCICIO 4
"""Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso."""

def ordenado():
    ordenado = []
    inverso = []

    for i in range(1, 100+1):
        ordenado.append(i)
    
    inverso = ordenado[::-1]
    print(inverso)

ordenado()