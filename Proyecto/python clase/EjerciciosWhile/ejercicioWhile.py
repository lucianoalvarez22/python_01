#UNA LISTA DE PALABRAS
# ENCONTRAR LA MAS LARGA E IMPRIMIRLA


palabras = ["hola","adios","manzana","pera","pin"]

indice_max = -1
len_max = 0

for i in range (len(palabras)):
    largo = len(palabras[i])
    if largo > len_max: 
        indice_max = i
        len_max = largo

print(palabras[indice_max])