#OPERACIONES CON ARCHIVOS
#Modos de archivos "r" (read) 
# "w" (writer) 
# "a" (append para abrir y añadir) 
# "w+" (lectura y escritura, crea archivos inexistentes. Si no existe, lo crea. Y si existe, borra el existente y se sustituye por el nuevo) 
# "r+" (leer y escritura. Si no existe da un error)
# "a+" (Para lectura y escritura. Si existe, se añade al final)
# "b" (abre el archivo en modo binario)

archivo = open('/home/luciano/git1/python_01/Proyecto/python clase/Archivos/pruebas.txt','r')
numeros = []
for linea in archivo:
    numeros.append(int(linea))


archivo.close()
print(numeros)

