#Un zoológico en particular determina el precio de la entrada según la edad del visitante. 

# Los huéspedes de 2 años de edad y menos se admiten sin cargo. 

# Niños entre 3 y 12 años cuestan $14.00. 

# Las personas mayores de 65 años o más cuestan $ 18.00. 

# La entrada para todos los demás invitados es de $23.00.

# Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. 

# El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. 

# Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 

# El costo debe mostrarse con dos decimales.

def dame_edades_grupo (): #Funcion que devuelve una lista con las edades introducidas
    lista_edades = []
    edad_usuario = input("Ingresa la edad del cliente: ")
    while True: #Mientras el input sea true(introduzca un valor que no sea "intro")
        if edad_usuario == "": 
            break
        edad_usuario = int(edad_usuario) #Convierto el string en entero
        lista_edades.append(edad_usuario) #Añado el valor a la lista vacia
        edad_usuario = (input("Ingresa la edad del cliente: ")) #Vuelvo a pedir el input para ingresar un valor y mientras siga siendo True vuelve arriba.
    return lista_edades


def costo_grupo_total (edades_global): #Funcion de devuelve el cálculo total de lo que cuesta el grupo
    precio_total = 0
    for edades_grupo in (edades_global): #Itero la lista de edades y con condicionales voy añadiendole y sumandole valores a la variable "precio_total"
        if edades_grupo <= 2:
            precio_total += 0
        elif edades_grupo >= 3 and edades_grupo <=12:
            precio_total += 14
        elif edades_grupo >= 65:
            precio_total += 14
        else:
            precio_total += 23
    return "{0:.2f}".format(precio_total) 

coleccion_edades = dame_edades_grupo()
print(f"El pago total de tu grupo es de {costo_grupo_total(coleccion_edades)}€")









