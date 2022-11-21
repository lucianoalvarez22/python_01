#CREAR UN ARCHIVO NUEVO Y ESCRIBIR DENTRO DEL ARCHIVO MEDIANTE ESTE CODIGO. 

RUTA_BASE = '/home/luciano/git1/python_01/Proyecto/python clase/Archivos/'


""" archivo = RUTA_BASE + 'datos_03.txt'

datos = [{'nombre':'Juan', 'apellido1':'Garcia', 'apellido2':'Romero', 'edad':22},
         {'nombre': 'Maria', 'apellido1':'López', 'apellido2': 'Sanchez', 'edad':20},
         {'nombre': 'Luciano','apellido1':'Ochoa', 'apellido2': 'Alvarez', 'edad':28}

]
f = open (archivo, 'w') #Con la w hemos creado el archivo y abierto

for d in datos:
    cadena = d['nombre'] + ',' + d['apellido1']+ ',' + d['apellido2']+ ',' + str(d['edad']) + '\n'
    f.write(cadena) #CON EL WRITE TE ESCRIBE LA LINEA DE ARRIBA (CADENA)

f.close() """

""" 
Crear funcion para crear archivo y escribir
 """


def escribe_archivo (nombre, datos):
    f = open(nombre, 'a+')
    f.write(datos)
    f.close()

c1 = 'Juan,Garcia,Romero,22\n'
c2 = 'Maria,López,Sanchez,20\n'
c3 = 'Luciano,Ochoa,Alvarez,28\n'

mi_archi = RUTA_BASE + 'mi_arch.txt'
escribe_archivo (mi_archi,c1)
escribe_archivo (mi_archi,c2)
escribe_archivo (mi_archi,c3)
    
