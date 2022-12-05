import csv
import os

ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'

datos = ruta_base + 'cust_orders_prods.csv'

def menu():
    print('MENU')
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
        contador_venta_empleado = 0
    return lista_ventas_empleados

def porcentaje_empleados(lista_venta_empleados, ventas_totales):
    for i in lista_venta_empleados:
        for k, v in i.items():
            porcentaje_vendedor = round((( v / ventas_totales) * 100) ,2)
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
        contador_compra_cliente = 0
    return lista_compra_clientes

def porcentaje_clientes(lista_compra_clientes, ventas_totales):
    for i in lista_compra_clientes:
        for k, v in i.items():
            porcentaje_clientes = round((( v / ventas_totales) * 100) ,2)
            print(f'{k}: {porcentaje_clientes}%')
    return  

def dame_nombre_producto(archivo_devuelto):
    nombres_productos = []
    for p in archivo_devuelto:
        nombre_productos_repetidos = p['product_name']
        if nombre_productos_repetidos not in nombres_productos:
            nombres_productos.append(nombre_productos_repetidos)
    return nombres_productos

def productos_vendidos(nombre_producto, archivo_devuelto):
    lista_venta_productos = []
    contador_venta_productos = 0
    for nombre in nombre_producto:
        for v in archivo_devuelto:
            if v['product_name'] == nombre:
                contador_venta_productos +=  int(v['quantity'])
        diccionario_vacio = {}
        diccionario_vacio[nombre] = contador_venta_productos
        lista_venta_productos.append(diccionario_vacio)
        contador_venta_productos = 0
    return lista_venta_productos

def orden_mas_vendidos(lista_productos_vendidos):
    lista_cant_prod = []
    for i in lista_productos_vendidos:
        for k, v in i.items():
            lista_cant_prod.append(v)
    # lista_ordenada_desc = sorted(lista_cant_prod, reverse=True) #Sorted para ordenar la lista(la lista de numeros, reverse=true ordena de mayor a menor)
    # print(lista_ordenada_desc)
    lista_cant_prod.sort(reverse=True)
    return lista_cant_prod[0:5]

def orden_productos_vendidos (productos_en_orden, lista_productos_vendidos):
    lista_definitiva = []
    for produc_orden in productos_en_orden:
        for ventas_productos in lista_productos_vendidos:
            for k, v in ventas_productos.items():
                if v == produc_orden:
                    lista_definitiva.append({k:v})
    print(lista_definitiva)

    
    """ for ventas_productos in lista_productos_vendidos:
        for k, v in ventas_productos.items():
            if v in productos_en_orden:
                lista_definitiva.append({k:v})
    print(lista_definitiva) """
            

archivo_devuelto = leer(datos)
nombre_empleados = dame_nombres_empleados(archivo_devuelto)
lista_venta_empleados = dame_venta_empleados(archivo_devuelto, nombre_empleados)
nombre_clientes = dame_nombre_clientes(archivo_devuelto)
lista_compra_clientes = dame_compra_clientes(archivo_devuelto, nombre_clientes)
ventas_totales = dame_ventas_totales(archivo_devuelto)
nombre_producto = dame_nombre_producto(archivo_devuelto)
lista_productos_vendidos = productos_vendidos(nombre_producto, archivo_devuelto)
productos_en_orden = orden_mas_vendidos(lista_productos_vendidos)

orden_productos_vendidos(productos_en_orden, lista_productos_vendidos)

def main():
    limpiapantalla()

    while True:
        menu()
        opcion = input('Elije una opcion: ')
        limpiapantalla()

        if opcion == '1':
            limpiapantalla()
            print(porcentaje_empleados(lista_venta_empleados, ventas_totales))
            
        if opcion == '2':
            limpiapantalla()
            print(porcentaje_clientes(lista_compra_clientes, ventas_totales))
        
        if opcion == '3':
            limpiapantalla()
            print(productos_en_orden)

            
        if opcion == '5':
            break
    print('Programa finalizado')

#6500000 48700000 2900000 2000000