
import csv #Se utilizan para exportar datos de un sistema e importarlos en otro
import pprint
ruta_base = '/home/luciano/git1/python_01/Proyecto/python clase/Archivos/'
datos = ruta_base + 'ejemplo.csv'

def escribe_writer(archivo):
    with open(archivo, 'w') as csv_file:
        escritor = csv.writer(csv_file,delimiter=';')
        escritor.writerow(['Nombre', 'Apellido', 'dni'])
        escritor.writerow(['Paco0', 'Gomez0', '12345678N']) #Metodo para escribir los datos uno a uno
        escritor.writerow(['Paco1', 'Gomez1', '12345678N'])
        escritor.writerow(['Paco2', 'Gomez2', '12345678N'])
        escritor.writerow(['Paco3', 'Gomez3', '12345678N'])
        escritor.writerow(['Paco4', 'Gomez4', '12345678N'])

#escribe_writer(datos)



def escribe_dict (archivo):
    campos = ['Nombre', 'Apellido', 'dni']
    with open (archivo,'w') as csv_file: 
        escritor = csv.DictWriter(csv_file,campos,) #'escritor' es un manejador
        escritor.writeheader() #Metodo para ESCRIBIR la cabecera. 
        escritor.writerow({'Nombre':'Luis', 'Apellido':'Martin', 'dni':'4564655746N'}) #Metodo para ESCRIBIR los DATOS

