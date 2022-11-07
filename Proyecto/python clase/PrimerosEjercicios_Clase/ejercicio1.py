# Bin - pasar de decimal a binario
# hex para pasar de decimal a hexa
#oct para pasar de decimal a octa


# EJERCICIO - PROGRAMA PARA PONER EN MAYUSCULA UNA PALABRA
cadena = 'Esto es un experimento con cadenas'
print(cadena)
print(len(cadena))

palabra = "experimento"
longitud = len(palabra)
pto1 = cadena.find(palabra)
pto2 = pto1 + longitud


parte1 = cadena[:pto1]
parte2 = palabra.upper()
parte3 = cadena[pto2:]

resultado = parte1 + parte2 + parte3
print(resultado)










