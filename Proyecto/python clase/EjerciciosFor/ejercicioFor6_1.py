#Escribe un programa que utilizando el carácter producto (*), 
# dibuje triángulos rectángulos del tipo mostrado en el siguiente ejemplo. 
# El programa necesitará conocer el número de caracteres que forman los 
# catetos.

medida = 5
simbolo = "*\t"

for i in range(1,medida):
    print(simbolo * i)

