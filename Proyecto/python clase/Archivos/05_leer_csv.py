import csv #Se utilizan para exportar datos de un sistema e importarlos en otro
import pprint
ruta_base = '/home/luciano/git1/python_01/Proyecto/python clase/Archivos/'
datos = ruta_base + 'hurricanes.csv'

def leer_reader (fichero):
    filas = []
    with open(fichero, 'r') as csv_file: 
        csvreader = csv.reader(csv_file)
        cabecera = next(csvreader)
        for f in csvreader: #Iteramos el archivo csv, estamos leyendo
            filas.append(f)
    print(cabecera)
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(filas)




#leer_reader(datos)

# --------------------------------------------------------------------

def leer_dictreader(archivo):
    f = open(archivo, 'r')
    lector_dict = csv.DictReader(f)
    lista_dict = list(lector_dict)
    f.close()

    pprint.pprint(lista_dict)

leer_dictreader(datos)