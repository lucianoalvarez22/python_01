import os

ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'
archivo_tarea = ruta_base + 'tareas.txt'

def menu():
    print("MENÚ DE AGENDA")
    print("¿Que deseas hacer?")
    print("1. Añadir una tarea")
    print("2. Listar tareas")
    print("3. Editar tarea")
    print("4. Borrar tarea")
    print('6. Salir')


def dame_tareas():
    lista_tareas = []
    contador_id = dame_ultimo_id()
    while True:
        tarea = input('Escribe una tarea o pulsa "ENTER" para finalizar: ')
        contador_id += 1
        dict_tarea = {}
        dict_tarea['id'] = str(contador_id)
        dict_tarea['tarea'] = tarea
        dict_tarea['estado'] = 'pendiente'
        lista_tareas.append(dict_tarea)
        if tarea == '':
            break

    lista_tareas.pop(-1)
    return lista_tareas
    
def dame_ultimo_id():
    f = open(archivo_tarea, 'r+')
    lectura_linea = f.readlines()
    if lectura_linea == []:
        return 0
    else:
        ultima_linea = lectura_linea[-1]
        ultima_linea = ultima_linea[0]
        return int(ultima_linea) #Devuelve el ultimo id de la funcion dame_tareas

def dame_primer_id():
    f = open(archivo_tarea, 'r+')
    lectura_linea = f.readlines()
    if lectura_linea == []:
        return 0
    else:
        ultima_linea = lectura_linea[0]
        ultima_linea = ultima_linea[0]
        return int(ultima_linea)

def editar_tarea(tareas_devueltas):
    opcion_usuario = input('Introduce el ID de la tarea que deseas editar: ')
    limpiar_consola()
    for t in tareas_devueltas:
        for k,v in t.items():
            if k == 'id' and v == opcion_usuario:
                listar_tareas([t])
                tarea_estado = input("Para editar la descripción escriba 'd', para editar el estado escriba 'e', para editar las dos escriba 'de': ")
                if tarea_estado == 'd':
                    nueva_descripcion = input('Escriba la nueva descripción: ')
                    t['tarea'] = nueva_descripcion
                elif tarea_estado == 'e':
                    nuevo_estado = input('Elije nuevo estado (pendiente o hecho): ')
                    t['estado'] = nuevo_estado
                elif tarea_estado == 'de':
                    nueva_descripcion = input('Escriba la nueva descripción: ')
                    nuevo_estado = input('Elije nuevo estado (pendiente o hecho): ')
                    t['tarea'] = nueva_descripcion
                    t['estado'] = nuevo_estado
                else:
                    print("Opcion incorrecta: Las opciones son 'd', 'e' y 'de'")
    return tareas_devueltas

    
def borrar_tarea(tareas_devueltas):
    opcion_borrar = int(input("Elije el ID de la tarea que quieras borrar: "))
    nuevas_tareas = []
    for t in tareas_devueltas:
        if int(t['id']) != opcion_borrar:
            nuevas_tareas.append(t)
    return nuevas_tareas


    """ if opcion_borrar > primer_id and opcion_borrar <= len(tareas_devueltas):
        tareas_devueltas.pop(opcion_borrar-1)
        return tareas_devueltas
    else:
        print("Opcion incorrecta (Elije un ID válido) ")
        return tareas_devueltas  """


def guardar_tareas (lista_tareas_insertadas, modo):

    f = open(archivo_tarea, modo)

    for t in lista_tareas_insertadas:
        guardando_tareas = t['id'] + '-' + t['tarea'] + '-' + t['estado']
    
        f.write(guardando_tareas + '\n')
    f.close()
    return '\nTareas guardadas correctamente\n'


def leer_archivo():

    f = open(archivo_tarea, 'r+')
    lista_lectura = []
    lectura_linea = f.readlines()

    for lineas in lectura_linea:
        linea_trozos = lineas.split('-')
        dict_lectura = {}
        dict_lectura['id'] = linea_trozos[0]
        dict_lectura['tarea'] = linea_trozos[1]
        dict_lectura['estado'] = linea_trozos[2].replace('\n', '')
        lista_lectura.append(dict_lectura)
        
    return lista_lectura


def listar_tareas(tareas_devueltas):
    print(tareas_devueltas)
    print("LISTA DE TAREAS:\n")
    for t in tareas_devueltas:
        #print(t)
        print(f"ID: {t['id']} || Descripción: {t['tarea']} || Estado: {t['estado']}")


def limpiar_consola ():
    os.system('clear')


""" lista_tareas_insertadas = dame_tareas()
dame_ultimo_id()
guardar_tareas(lista_tareas_insertadas)
print(leer_archivo()) """
#editar_tarea()

#if__name__ == '__main__':   Se usa para usar main, se introduce todo dentro del if y no hace falta llamar a la funcion "main" al final.
def main():
    limpiar_consola()
    menu()

    while True:
        opcion = int(input("Elija una opcion: "))

        if opcion == 1:
            limpiar_consola()
            lista_tareas_insertadas = dame_tareas()
            print(guardar_tareas(lista_tareas_insertadas, 'a+'))
            limpiar_consola()
            menu()

        if opcion == 2:
            tareas_devueltas = leer_archivo()
            limpiar_consola()
            listar_tareas(tareas_devueltas)
            menu()
        
        if opcion == 3:
            limpiar_consola()
            print('¿Qué tarea desea editar?')
            tareas_devueltas = leer_archivo()
            listar_tareas(tareas_devueltas)
            lista_editada = editar_tarea(tareas_devueltas)
            print(guardar_tareas(lista_editada, 'w+'))
            listar_tareas(lista_editada)
            menu()
        
        if opcion == 4:
            print('¿Qué tarea desea borrar?')
            tareas_devueltas = leer_archivo()
            listar_tareas(tareas_devueltas)
            lista_editada = borrar_tarea(tareas_devueltas)
            print(guardar_tareas(lista_editada, 'w+'))
            listar_tareas(lista_editada)
            menu()

        if opcion == 6:
            exit()

main()


    
        

    



""" for key,value in t.items():
    print(key,":",value) """