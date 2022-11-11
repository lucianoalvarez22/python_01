#OPERACIONES CON ARCHIVOS
#Modos de archivos "r" (read) "w" (writer) "a" (append para abrir), "w+" (lectura y escritura, crea archivos inexistentes) "r+" (leer y escritura)
# "a+" (Para )

archivo = open('/home/luciano/git1/python_01/Proyecto/python clase/Archivos/pruebas.txt','r')
numeros = []
for linea in archivo:
    numeros.append(int(linea))


archivo.close()
print(numeros)

