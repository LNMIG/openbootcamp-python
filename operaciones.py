# Forma de importar un módulo desde un package (A)
# from operaciones import suma

# Forma de importar un módulo desde un package (B)
# import operaciones.suma

# Forma de importar un módulo desde un package con otro nombre más corto (C)
import operaciones.suma as S

import operaciones.dividir.divide as D
import operaciones.multiplicar.multiplica as M
import operaciones.restar.resta as R

def main():
    # print(suma.suma(2,2)) # para forma (A)
    # print(operaciones.suma.suma(2,2)) # para forma (B)
    print("El módulo 'suma' da que 2+2 es: ",S.suma(2,2)) # para forma (C)
    print("El módulo 'resta', dentro del package 'restar', da que 8-3 es: ",R.resta(8,3))
    print("El módulo 'divide', dentro del package 'dividir', da que 10/5 es: ",D.division(10,5))
    print("El módulo 'multiplica', dentro del package 'multiplicar', da que 6x6 es: ",M.multiplicador(6,6))

if __name__ == '__main__':
    main()