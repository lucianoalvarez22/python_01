ruta_base = '/home/luciano/git1/python_01/Proyecto/python clase/ProyectoGrupal/'
archivo_tarea = ruta_base + 'tareas.txt'


def dame_tareas():
    lista_tareas = []

    while True:
        tarea = input('Dime qué tareas vas a hacer: ')
        dict_tarea = {}
        dict_tarea['tarea'] = tarea
        dict_tarea['estado'] = 'pendiente'
        lista_tareas.append(dict_tarea)
        if tarea == '':
            break

    lista_tareas.pop(-1)
    return lista_tareas

#print(dame_tareas())


def guardar_tareas (lista_tareas_insertadas):

    f = open(archivo_tarea, 'w')
    for t in lista_tareas_insertadas:
        guardando_tareas = t['tarea'] + '-' + t['estado']
    
        f.write(guardando_tareas + '\n')
    f.close()
    return guardando_tareas



def leer_archivo():

    f = open(archivo_tarea, 'r+')
    lista_lectura = []
    lectura_linea = f.readlines()

    for lineas in lectura_linea:
        linea_troceada = lineas.split('-')
        print(linea_troceada)
        
        """ linea_troceada = lineas.split('-')
        linea_troceada = lineas.replace('\n', '')
        print(type(linea_troceada)) 
        dict_lectura = {}
        dict_lectura['tarea'] = linea_troceada[0]
        dict_lectura['estatus'] = linea_troceada[1]
        lista_lectura.append(dict_lectura)

    return lista_lectura
  """




lista_tareas_insertadas = dame_tareas()
print(guardar_tareas(lista_tareas_insertadas))
print(leer_archivo())


    
        

    



""" for key,value in t.items():
    print(key,":",value) """