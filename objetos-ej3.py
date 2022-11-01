# EJERCICIO 3
"""Escribe un programa en la consola de python que pida al usuario su peso (en kg)
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal
calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip."""

peso = int(input("Ingresa tu peso (en kg) por favor: "))
estatura = float(input("Ingresa tu estatura (en m) por favor: "))

indiceMasaCorporal = round(peso / estatura**estatura, 2)

print("Tu índice de masa corporal es: ",indiceMasaCorporal)