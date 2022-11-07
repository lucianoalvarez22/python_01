#SPLIT PARA TROCEAR CARACTERES
cadena = '1,2,3,4,5,6,7'
trozos = cadena.split(',') 
print(trozos)

#JOIN ES PARA UNIR CARACTERES Y LO QUE ESTÉ EN '' ES EL SEPARADOR - SOLO VALE PARA CADENAS
unida = ''.join(trozos)
print(unida)


#Split CORTA LAS CADENAS, POR DEFECTO, POR EL ESPACIO. PERO SI ENTRE PARENTESIS("")PONEMOS UN SEPARADOR, SE SEPARA CON ESE SEPARADOR

cadena1 = 'esto es una tarde*# estupenda de aprender python'
print(cadena1)

palabras =  cadena1.split()
print(palabras)

#join

unidas = '--'.join(palabras)
print(unidas)


#Find - Para que busque dentro de una cadena, una subcadena y te devuelve la posicion del primer caracter

posicion = cadena1.find('#')
print(posicion)
print (cadena1[:posicion-1])
print(cadena1[posicion + 2:])