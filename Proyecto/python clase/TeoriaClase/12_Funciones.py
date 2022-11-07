#Funciones - Es una manera de reutilizar el codigo, agrupar una serie
#de lineas de codigo y ponerle nombre

#PARAMETROS (DENTRO DE LOS PARENTESIS) ES UN VALOR QUE LE PASO A LA FUNCION PARA QUE HAGA SUS CALCULOS
#LAS FUNCIONES PUEDEN TENER MUCHOS PARÁMETROS

#


#SINTAXIS

def hola ():
    print("Hola")

def saludo(nombre, dia):
    print(f"Buenas tardes, {nombre}. Hoy es {dia}")

saludo("Teo", "Lunes") #LO QUE ESTÁ DENTRO DEL PARENTESIS ES UN ARGUMENTO. UN ARGUMENTO ES EL VALOR DE UN PARAMETRO. 
#LOS ARGUMENTOS SE PASAN EN EL MISMO ORDEN QUE ESTÁN LOS PARAMETROS


def inversa (texto):
    print(texto[::-1])

inversa ("Inversa")

#################################

def inversa (texto):
    return texto[::-1] # [::-1] ME DA LA VUELTA AL TEXTO Y LO DEVUELVE A QUIEN LO HAYA INVOCADO

x = inversa ("Luciano") # X HA INVOCADO LA FUNCION Y LE HA DADO UN ARGUMENTO "LUCIANO"
print(x) # FINALMENTE IMPRIMIREMOS X 

########################################

