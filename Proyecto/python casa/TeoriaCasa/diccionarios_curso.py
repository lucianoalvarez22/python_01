import pprint

#DICCIONARIOS - SINTAXIS DICCIONARIO = {CLAVE, VALOR}
#PERMITE ALMACENAR CUALQUIER TIPO DE DATO COMO VALOR


diccionario ={
    'uno': 'Primero', #CLAVE =UNO  VALOR=PRIMERO
    'dos': 'Segundo',
    'hola@gmail.com': 'Miguel' }

print(diccionario['uno']) #AQUI BUSCA LA "CLAVE" DEL DICCIONARIO Y TE DEVUELVE EL "VALOR"

diccionario['Tres'] = 'Tercero' #ASÍ SE AÑADE UNA CLAVE Y UN VALOR AL DICCIONARIO

print(diccionario['Tres']) #AQUI IMPRIMO EL VALOR DE TRES QUE ES IGUAL A TERCERO

print(list(diccionario.keys())) #AQUI TE MUESTRA TODAS LAS KEYS(CLAVES)
print(list(diccionario.values())) #AQUI TE MUESTRA TODOS LOS VALORES DE LAS KEYS(CLAVES) 

del diccionario['Tres']  #AQUI BORRAMOS UNA CLAVE CON LA FUNCION "DEL"
print(list(diccionario))



# --------------------------------------------
#EJEMPLO 

coches = {
    '1234FRD': 'Opel Corsa',
    '9876TRD': 'Ford Fiesta',
    '6546LFV' : 'Ford Kuga'
}
coches['7777KHGF'] = 'Ferrari'

pprint.pprint(coches) #EL PPRINT VIENE DE UNA LIBRERIA QUE HEMOS IMPORTADO ARRIBA 