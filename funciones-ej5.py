# EJERCICIO 5
"""Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."""

def isBisiesto(anio):
    isBisiesto = "no es"
    
    if anio % 4 == 0:
        isBisiesto = "es"
    
    print ("El año", anio, isBisiesto,"bisiesto")

anio = input("Ingresa un año para saber si es bisiesto o no: ")
isBisiesto(int(anio))

