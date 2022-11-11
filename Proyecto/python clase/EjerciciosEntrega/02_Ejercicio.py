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


numero_lados = int(input("Dame un número de lados: "))
while numero_lados < 3 or numero_lados > 10:
    print("Solo puedes ingresar lados del 3 al 10")
    numero_lados = int(input("Vuelve a ingresar un número de lados: ")) #Valido con el While para que el usuario no introduzca numeros menores que 3 y mayores que 10

def dame_nombre_figuras (lados_usuario): #Funcion que me devuelva el nombre de la figura a partir del numero que ingrese el usuario
    figuras = {  #Diccionario figuras clave-valor
        3:"Triángulo",
        4:"Cuadrado",
        5:"Pentágono",
        6:"Hexágono",
        7:"Heptágono",
        8:"Octógono",
        9:"Eneágono",
        10:"Decágono"
    }
    return figuras.get(lados_usuario) #Me devuelve el valor de la clave de figuras(numeros que meterá el usuario)

resultado = dame_nombre_figuras(numero_lados) 
print(f"El número de lados que ha introducido el usuario equivale a un {resultado}")

