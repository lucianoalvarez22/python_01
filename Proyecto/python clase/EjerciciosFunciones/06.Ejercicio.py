#EJERCICIO 6 - MAS O MENOS

def pinta_tabla():

    tabla = [   #HACER UNA TABLA
        [1,2,3,4,5,6,7,8,9,0], #ESTO ES UNA FILA
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1]

    ]
    for f in tabla:
        for c in f:
            print(f"{c}\t",end="")
        print()

#pinta_tabla()

#------------------------------

#EJERCICIO 4

def pinta_tablas (filas,cols):
    cadena = "<table>"
    for f in range(filas):
        cadena= "<tr>"
        for c in range(cols):
            cadena += f"<td>{f},{c}</td>"
        cadena += "<tr>"
    
    cadena += "</table>"
    return cadena

print(pinta_tablas(10,10))