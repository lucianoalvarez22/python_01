ruta_base = '/home/luciano/Github_Luciano/PythonCasa_01/python_01/Proyecto/python clase/ProyectoGrupal/'

tareas = ruta_base + 'tareas2.txt'


def get_task_from_user():
    lista_pen = []
    while True:
        pen = input('Dime qué tareas vas a hacer: ')
        dict_task = {}
        dict_task['name'] = pen
        dict_task['status'] = 'pending'
        lista_pen.append(dict_task)
        # a.write(pen + '\n')
        if pen == '':
            break
    lista_pen.pop(-1)
    return lista_pen


def save_task_to_file(tasks):
    """ Parámetros de open()
        https://j2logo.com/como-escribir-en-un-fichero-en-python/
        Uso w+ para que se sobreescriban los datos actualizados
    """

    a = open(tareas, 'w+')
    for task in tasks:
        task_line = ""
        for key, value in task.items():
            task_line = task_line + value + "-"
        a.write(task_line + '\n')
    print("Tasks saved succesfully\n")
    a.close()


def get_tasks_from_file():
    print("Extrayendo tareas del fichero...\n")
    a = open(tareas, 'r+')
    lista = []
    lineas = a.readlines()
    for linea in lineas:
        array_line = linea.split('-')
        dict_task = {}
        dict_task['name'] = array_line[0]
        dict_task['status'] = array_line[1]
        lista.append(dict_task)
    return lista


def print_infotasks_to_user(list_tasks_file):
    """Aqui van las opciones que el usuario podrá elegir, modificar, eliminar, o agregar una nueva tarea"""

    print("La lista de tareas son las siguientes: \n")

    # Enumerate te permite iterar un array y te da un indice y el valor
    message = ""
    for indice, task in enumerate(list_tasks_file):
        message_task = str(indice) + ": "
        for key, value in task.items():
            message_task = message_task + key + "= " + value + "\t"
        message = message_task + message + "\n"
        print(message_task + "\n")


def get_option_selected_by_user(list_tasks_file):
    options = """
        - Para eliminar una tarea escriba 'delete' o 'd'
        - Para modificar una tarea escriba 'update' o 'u'
        - Para añadir una nueva tarea escriba 'add' o 'a'
    ¿Qué desea hacer?:
    """
    option = input(options)
    return option


def switch_case_fake(list_tasks_file, option):
    if "delete" in option or "d" in option:
        print_infotasks_to_user(list_tasks_file)
        indice = int(input("Introduce el índice de la tarea que quieres eliminar: "))
        list_tasks_file.pop(indice)
        print("Task deleted succesfully\n")
        print_infotasks_to_user(list_tasks_file)
        
    elif "update" in option or "u" in option:
        pass
    else:
        pass


list_tasks = get_task_from_user()
save_task_to_file(list_tasks)
list_tasks_file = get_tasks_from_file()
print_infotasks_to_user(list_tasks_file)
option_selected = get_option_selected_by_user(list_tasks_file)
switch_case_fake(list_tasks_file, option_selected)
# print(list_tasks_file)


































""" ruta_base= '/home/alejandro/Proyectos/Python_01/archivos/'
tareas = ruta_base + 'tareas.txt'

def agenda():
  a = open(tareas, 'a+')
  lista_pen = []
  lista_ter = []
  while True:
    pen = input('Dime qué tareas vas a hacer: ')
    if pen in lista_pen:
      print('Esa tarea está repetida')
    else:
      lista_pen.append(pen)
    if pen == '':
      break
  while True:
    ter = input('Dime qué tareas has terminado: ')
    if ter == '':
      break
    if ter in lista_ter:
      print('Esa tarea ya está terminada')
    if ter in lista_pen:
      lista_pen.remove(ter)
      lista_ter.append(ter)
    else:
      lista_ter.append(ter)
  lista_pen.pop()
  a.write('La lista de tareas pendientes es: ' + str(lista_pen) + '\n')
  a.write('La lista de tareas terminadas es: ' + str(lista_ter) + '\n')
  a.close()

agenda() """













