#Un minorista en particular tiene un 60 por ciento de descuento en una variedad de productos descontinuados.

# Al minorista le gustaría ayudar a sus clientes a determinar el precio reducido de la mercancía al tener una tabla de descuentos impresa en el estante que muestre los precios originales y los precios después de que se haya aplicado el descuento. 

# Escriba un programa que use un bucle para generar esta tabla, que muestre el precio original, el monto del descuento y el nuevo precio para compras de $4.95, $9.95, $14.95, $19.95 y $24.95.

# Asegúrese de que los montos de descuento y los nuevos precios se redondeen a 2 decimales cuando se muestren.


def imprime_tabla_precios (lista_precios, porcentaje_descuento):
    print("Precio original","Descuento","Nuevo precio")
    for precio_original in (lista_precios):
        descuento = precio_original * (porcentaje_descuento / 100)
        nuevo_precio = precio_original - descuento
        print(precio_original," €","\t",round(descuento,2)," €","\t",round(nuevo_precio,2)," €","\n")


precios = [4.95, 9.95, 14.95,19.95,24.95]
porcentaje = 60
imprime_tabla_precios(precios,porcentaje)
