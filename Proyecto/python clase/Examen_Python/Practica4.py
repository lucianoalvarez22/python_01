
ruta_base = '/home/luciano/git1/python_01/Proyecto/python clase/Examen_Python/'
datos = ruta_base + 'archivo.txt'

def leer_archivo():
    f = open(datos, 'r+')
    lectura_linea = f.readlines()

    return lectura_linea


def cuenta_palabras(archivo):
    for p in archivo:
        print(p)

""" palabras = archivo.split(p)
        num_palabras = len(palabras)
        print(num_palabras)
 """



lista_archivo_leido = leer_archivo()
print(cuenta_palabras(lista_archivo_leido))

