#Escriba un programa que lea una posición del usuario. 
# Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
# Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
# Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
# Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
# Su programa puede suponer que siempre se ingresará una posición válida. 
# No es necesario realizar ninguna comprobación de errores.

def crear_tabla():
    color = "blanco"
    dict = {}
    columnas = ["A","B","C","D","E","F","G","H"]

    for fila in range(8):
        for columna in columnas:
            key = str(fila) + str(columna)
            if color == "blanco":
                dict[key] = color
                color = "negro"
            else:
                dict[key] = color
                color = "blanco"

        if color == "blanco":
            color = "negro"
        else:
            color = "blanco"
    return dict


def peticion_usuario(f_usuario, c_usuario,dicionario_completo):
    usuario = f_usuario + c_usuario.upper()

    return dicionario_completo.get(usuario)

diccionario = crear_tabla()
fila_usuario = input("Introduce la fila: ")
columna_usuario = input("Introduce la columna: ")
resultado = peticion_usuario(fila_usuario,columna_usuario,diccionario)
print(resultado)


