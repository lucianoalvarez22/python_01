#WITH 

RUTA_BASE = '/home/luciano/git1/python_01/Proyecto/python clase/Archivos/'
archivo = RUTA_BASE + 'datos_04.txt'

datos = [{'nombre':'Juan', 'apellido1':'Garcia', 'apellido2':'Romero', 'edad':22},
         {'nombre': 'Maria', 'apellido1':'López', 'apellido2': 'Sanchez', 'edad':20},
         {'nombre': 'Luciano','apellido1':'Ochoa', 'apellido2': 'Alvarez', 'edad':28}

]

#MANERA STANDAR DE MANEJAR LOS FICHEROS CON WITH - MANERA DE CREAR Y ESCRIBIR UN ARCHIVO
#SOLO HAY QUE ABRIRLO YA QUE SE CIERRA SOLO AUTOMATICAMENTE

with open(archivo, 'a+') as f: #WITH OPEN PARA ABRIR
    for d in datos:
        cadena = d['nombre'] + ',' + d['apellido1']+ ',' + d['apellido2']+ ',' + str(d['edad']) + '\n'
        f.write(cadena) #WRITE para ESCRIBIR
    
#NO HAY CLOSE PORQUE SE CIERRA SOLO