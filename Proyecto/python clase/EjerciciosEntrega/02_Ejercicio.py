#Escriba un programa que determine el nombre de una forma a partir de su número de lados. 
# Lea la cantidad de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 
# Su programa debe admitir formas con entre 3 y 10 lados (incluidos). 
# Si se ingresa un número de lados fuera de este rango, su programa debería mostrar un mensaje de error apropiado.

""" Triangulo
Cuadrado
Pentagono
Hexagono
Heptagono
Octógono
Eneágono
Decágono """

numero_lados = int(input("Dame un numero de lados: "))
while numero_lados < 3 or numero_lados > 10:
    numero_lados = int(input("Dame un numero de lados: "))

def dame_nombre_figuras (lados_usuario):
    figuras = {
        3:"triangulo",
        4:"cuadrado",
        5:"pentagono",
        6:"hexagono",
        7:"hepagono",
        8:"octogono",
        9:"eneagono",
        10:"decagono"
    }
    return figuras.get(lados_usuario)

resultado = dame_nombre_figuras(numero_lados)
print(f"El numero de lados que ha introducido el usuario equivale a un {resultado}")

