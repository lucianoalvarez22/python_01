

def dame_articulos():
    dict_articulos = {}
    while True:
        usuario_nombre = input('Introduce el nombre del articulo: ')
        usuario_precio = input('Introduce el precio del articulo: ')
        if usuario_nombre == "" and usuario_precio == "":
            break
        dict_articulos[usuario_nombre] = usuario_precio

    return dict_articulos

        
dame_articulos()