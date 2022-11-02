# Texto a introducir

list = ["Plataforma: Openbootcamp", "Curso: full stack", "Situación: voy llevando el curso"]

# Creo archivo
def create():
    f = open('txtEjercicio1.txt', 'w', encoding="utf-8")
    f.close()

# Escribo en archivo
def writeIn():
    f = open('txtEjercicio1.txt', 'a',encoding="utf-8")
    for items in list:
        if not items.endswith('\n'):
            items += '\n'
        f.write(items)
    f.close()

# Muestro el contenido
def printContent():
    f = open('txtEjercicio1.txt', 'r',encoding="utf-8")
    print(f.read())
    f.close()

def main():
    create()
    writeIn()
    printContent()

if __name__=="__main__":
    main()