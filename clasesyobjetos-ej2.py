# EJERCICIO 2
"""
En este segundo ejercicio, tendréis que crear un programa que tenga
una clase llamada Alumno que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    nombre = ""
    nota = 1
    isAprobado = "REPROBO"

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        if self.nota > 4:
            self.isAprobado = "APROBO"

    def descripcion(self):
        print("El alumno", self.nombre.upper(), "obtuvo una nota de", self.nota, "por lo que", self.isAprobado, "la materia")

nombre = input("Ingresa nombre de alumno: ")
nota = input ("Ingresa una nota: ")

alumno = Alumno(nombre, int(nota))
alumno.descripcion()

