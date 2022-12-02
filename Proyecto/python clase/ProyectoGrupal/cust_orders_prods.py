import csv
import os

ruta_base = '/home/luciano/git1/python_01/Proyecto/python clase/ProyectoGrupal/'
datos = ruta_base + 'cust_orders_prods.csv'

def menu():
    print('1.- Porcentaje de ventas de cada vendedor.')
    print('2.- Porcentaje de ventas de cada cliente.')
    print('3.- Cinco productos mas vendidos.')
    print('4.- Ingresos mensuales.')
    print('5.- Salir.')

def limpiapantalla():
    os.system('clear')


def leer(archivo):
    f = open(archivo,'r')
    leer_dict = csv.DictReader(f)
    lista_dict = list(leer_dict)
    f.close()
    return lista_dict

def dame_ventas_totales(archivo_devuelto):
    contador_quantity_total = 0
    for v in archivo_devuelto:
        quantity = int(v['quantity'])
        contador_quantity_total += quantity
    return contador_quantity_total

def dame_nombres_empleados(archivo_devuelto):
    nombre_empleados = []
    for e in archivo_devuelto:
        nombre_empleados_repetidos = e['employee_name']
        if nombre_empleados_repetidos not in nombre_empleados:
            nombre_empleados.append(nombre_empleados_repetidos)
    return nombre_empleados

def dame_venta_empleados(archivo_devuelto,nombre_empleados):
    lista_ventas_empleados = []
    contador_venta_empleado = 0
    for nombre in nombre_empleados:
        for v in archivo_devuelto:
            if v['employee_name'] == nombre:
                contador_venta_empleado += int((v['quantity']))
        diccionario_vacio = {}
        diccionario_vacio[nombre] = contador_venta_empleado
        lista_ventas_empleados.append(diccionario_vacio)
        contador_venta_empleado == 0
    return lista_ventas_empleados




limpiapantalla()
archivo_devuelto = leer(datos)
nombre_empleados = dame_nombres_empleados(archivo_devuelto)
dame_ventas_totales(archivo_devuelto)
dame_nombres_empleados(archivo_devuelto)
print(dame_venta_empleados(archivo_devuelto,nombre_empleados))





# def main():
#     limpiapantalla()
#     menu()

#     opcion = input('Elije una opcion: ')

#     if opcion == 1:
#         vendedor()

