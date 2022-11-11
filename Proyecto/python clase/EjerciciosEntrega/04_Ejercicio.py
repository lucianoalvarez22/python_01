#Escriba un programa que lea una posición del usuario. 
# Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
# Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
# Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
# Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
# Su programa puede suponer que siempre se ingresará una posición válida. 
# No es necesario realizar ninguna comprobación de errores.

def crear_tabla(): #Funcion para crear una tabla(filas-columnas) e ir metiendo en el diccionario "dict" las filas y columnas con su color correspondiente
    color = "blanco"
    dict = {}
    columnas = ["A","B","C","D","E","F","G","H"] #Columnas de letras

    for fila in range(8): #Itero las filas (De 0 a 7)
        for columna in columnas: #Itero columnas (De la A a la H)
            key = str(fila) + str(columna) #Convierto la fila y columna en String y la meta en la variable "Key"
            if color == "blanco": #Esto al comenzar la primera iteracion es True
                dict[key] = color #Meto la fila y la columna (clave-valor) en el diccionario vacio
                color = "negro" #A partir de aquí color pasará a valer "Negro"
            else:
                dict[key] = color #Meto la fila y columna en el diccionario(clave-valor) cuando color es "Negro"
                color = "blanco" #Y vuelvo a cambiar el color a "Blanco"
        #Acaba la primera columna y la primera fila y antes de empezar con la segunda fila...
        if color == "blanco": # ... Si la última columna terminó en bñanco
            color = "negro" # ...Empezar la segunda fila en negro
        else:
            color = "blanco"
    return dict #Devuelve todas las filas y columnas en un diccionario


def peticion_usuario(f_usuario, c_usuario,dicionario_completo): #Funcion que devuelva el valor del diccionario = "Blanco" o "Negro"
    usuario = f_usuario + c_usuario.upper()

    return dicionario_completo.get(usuario)

diccionario = crear_tabla()
fila_usuario = input("Introduce la fila: ")
columna_usuario = input("Introduce la columna: ")
resultado = peticion_usuario(fila_usuario,columna_usuario,diccionario)
print(f"La casilla correspondiente a {fila_usuario}-{columna_usuario} es {resultado}")


