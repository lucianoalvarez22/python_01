import pprint

tablero = []

def crear_tablero():
    for f in range(10):
        fila = []
        for c in range(10):
            fila.append(0)
        tablero.append(fila)
    return tablero


def pedir_barco(tablero):
    while True:
        barco_f = input("Dame la fila (intro = fin): ")
        if barco_f == "":
            break
        barco_f = int(barco_f)
        barco_c = int(input("Dime la columna: "))
        tablero[barco_f][barco_c] = 1


def disparo(tablero):
    objetivo_f = int(input("Dime la fila: "))
    objetivo_c = int(input("Dime la columna: "))

    if tablero[objetivo_f][objetivo_c] == 1:
        print("Tocado")
    else:
        print("Agua")

# 1.Funcion de Tablero
# 2.Funcion Posicion de Barco
# 3.Funcion diparo
# 4. Funcion verificar disparo

def main():
    cuadro = crear_tablero()
    pedir_barco(cuadro)
    pprint.pprint(cuadro)
    disparo(cuadro)

main()