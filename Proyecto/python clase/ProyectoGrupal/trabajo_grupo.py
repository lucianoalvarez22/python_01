
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

    lista_tareas.pop()
    return lista_tareas

lista_tareas_insertadas = dame_tareas()
#print(dame_tareas())


def guardar_tareas (lista_tareas_insertadas):
    ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'
    archivo_tarea = ruta_base + 'tareas.txt'

    f = open(archivo_tarea, 'a+')
    for t in lista_tareas_insertadas:
        guardando_tareas = t['tarea'] + '-' + t['estado']

        f.write(guardando_tareas + '\n')
    f.close()



def leer_archivo():
    ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'
    archivo_tarea = ruta_base + 'tareas.txt'

    f = open(archivo_tarea, 'r')
    lectura_linea = f.readlines()
    lista_lectura = []
    for lineas in f:
        print(lineas)




print(leer_archivo())
#print(guardar_tareas(lista_tareas_insertadas))


    
        

    



""" for key,value in t.items():
    print(key,":",value) """