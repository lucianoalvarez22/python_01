import csv
import os


contenido = []

def menu():
    print('1.- Porcentaje de ventas de cada vendedor.')
    print('2.- Porcentaje de ventas de cada cliente.')
    print('3.- Cinco productos mas vendidos.')
    print('4.- Ingresos mensuales.')
    print('5.- Salir.')


def limpiapantalla():
    os.system('clear')

def vendedor():
    leer()
    ventas = len(contenido)
    print(ventas)

def leer():
    with open('cust_orders_prods.csv') as csvfile:
        reader =  csv.DictReader(csvfile)
        for row in reader:
            contenido.append(row)

def cerrar():
    pass
    

vendedor()

# def main():
#     limpiapantalla()
#     menu()

#     opcion = input('Elije una opcion: ')

#     if opcion == 1:
#         vendedor()

