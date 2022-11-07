#Escribe un programa que en primer lugar pregunte si se quiere calcular el área de un
#triángulo o la de un círculo.
#Si se contesta que se quiere calcular el área de un triángulo, el programa tiene que pedir
#entonces la base y la altura y escribir el área.
#Si se contesta que se quiere calcular el área de un círculo, el programa tiene que pedir
#entonces el radio y escribir el área.
#En ambos casos el programa debe ser capaz de calcular y mostrar el resultado adecuado. 

print("Cálculo de areas - Elige una figura geometrica: ")
print("a) Triangulo")
print("b) Circulo")

opciones = input("Qué figura quieres calcular (Escribe T o C): ")
eleccion = opciones.lower()

if eleccion in ("t"):
    base = float(input("Escribe la base: "))
    altura = float(input("Escriba la altura: "))
    area_triangulo = (base*altura)/2
    print(f"Un triangulo de base {base} y altura {altura} tiene un área de {area_triangulo}")

elif eleccion in ("c"):
    radio= float(input("Escribe el radio: ")) 
    area_circulo = 3.14 * radio**2
    print(f"Un círculo de radio {radio} tiene una base de {area_circulo}")

else:
    print("La letra no corresponde a ninguna opción")
 




