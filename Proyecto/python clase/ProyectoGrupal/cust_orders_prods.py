import csv
import os

ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'

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
        precio = int(v['unit_price'])
        contador_quantity_total += (quantity * precio)
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
                contador_venta_empleado += (int(v['quantity']) * int(v['unit_price']))
        diccionario_vacio = {}
        diccionario_vacio[nombre] = contador_venta_empleado
        lista_ventas_empleados.append(diccionario_vacio)
        contador_venta_empleado == 0
    return lista_ventas_empleados

def porcentaje_empleados(lista_venta_empleados, ventas_totales, archivo_devuelto):
    for i in lista_venta_empleados:
        for k, v in i.items():
            porcentaje_vendedor = round(((v / ventas_totales) * 100), 2)
            print(f'{k}: {porcentaje_vendedor}%')
    return        

def dame_nombre_clientes(archivo_devuelto):
    nombre_clientes = []
    for e in archivo_devuelto:
        nombre_clientes_repetidos = e['customer_name']
        if nombre_clientes_repetidos not in nombre_clientes:
            nombre_clientes.append(nombre_clientes_repetidos)
    return nombre_clientes

def dame_compra_clientes(archivo_devuelto, nombre_clientes):
    lista_compra_clientes = []
    contador_compra_cliente = 0
    for nombre in nombre_clientes:
        for v in archivo_devuelto:
            if v['customer_name'] == nombre:
                contador_compra_cliente += (int(v['quantity']) * int(v['unit_price']))
        diccionario_vacio = {}
        diccionario_vacio[nombre] = contador_compra_cliente
        lista_compra_clientes.append(diccionario_vacio)
        contador_compra_cliente == 0
    return lista_compra_clientes

def porcentaje_clientes(lista_compra_clientes, ventas_totales, archivo_devuelto):
    for i in lista_compra_clientes:
        for k, v in i.items():
            porcentaje_clientes = round(((v / ventas_totales) * 100), 2)
            print(f'{k}: {porcentaje_clientes}%')
    return  




archivo_devuelto = leer(datos)
nombre_empleados = dame_nombres_empleados(archivo_devuelto)
lista_venta_empleados = dame_venta_empleados(archivo_devuelto, nombre_empleados)
nombre_clientes = dame_nombre_clientes(archivo_devuelto)
lista_compra_clientes = dame_compra_clientes(archivo_devuelto, nombre_clientes)
ventas_totales = dame_ventas_totales(archivo_devuelto)

'''print(dame_ventas_totales(archivo_devuelto))
dame_nombres_empleados(archivo_devuelto)
print(dame_venta_empleados(archivo_devuelto,nombre_empleados))
print(porcentaje_empleados(lista_venta_empleados, ventas_totales, archivo_devuelto)) 
limpiapantalla()'''




def main():
    limpiapantalla()
    menu()

    while True:
        opcion = input('Elije una opcion: ')
        limpiapantalla()

        if opcion == '1':
            limpiapantalla()
            print(porcentaje_empleados(lista_venta_empleados, ventas_totales, archivo_devuelto))
            menu()
        if opcion == '2':
            limpiapantalla()
            print(porcentaje_clientes(lista_compra_clientes, ventas_totales, archivo_devuelto))
            menu()
        if opcion == '5':
            break
    print('Programa finalizado')    


main()