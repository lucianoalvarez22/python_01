#Un zoológico en particular determina el precio de la entrada según la edad del visitante. 

# Los huéspedes de 2 años de edad y menos se admiten sin cargo. 

# Niños entre 3 y 12 años cuestan $14.00. 

# Las personas mayores de 65 años o más cuestan $ 18.00. 

# La entrada para todos los demás invitados es de $23.00.

# Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. 

# El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. 

# Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 

# El costo debe mostrarse con dos decimales.

def dame_edades_grupo ():
    lista_edades = []
    edad_usuario = (input("Ingresa la edad del cliente: "))
    while True:
        if edad_usuario == "":
            break
        edad_usuario = int(edad_usuario)
        lista_edades.append(edad_usuario)
        edad_usuario = (input("Ingresa la edad del cliente: "))
    return lista_edades


def costo_grupo_total (edades_global):
    precio_total = 0
    for edades_grupo in (edades_global):
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









