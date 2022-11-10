#Escriba un programa que lea una posición del usuario. 
# Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
# Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
# Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
# Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
# Su programa puede suponer que siempre se ingresará una posición válida. 
# No es necesario realizar ninguna comprobación de errores.

tablero = []

for f in range(8):
    fila = []
    for c in range(8):
        if c%2 == 0:
            fila.append(0)
        else:
            fila.append(1)
    tablero.append(fila)
print(f"{tablero}\t",end="")



    
""" tablero[("a",1)] = "Blanco"
tablero[("a",2)] = "Negro"
tablero[("a",3)] = "Blanco"

print(tablero[("a",1)]) """

#OTRA OPCION CON TABLERO