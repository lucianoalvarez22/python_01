#Diseña un programa que detecte números negativos, la aplicación debe funcionar de la
#siguiente forma:

#a. En primer lugar, el programa preguntará por la cantidad de números que se van a
#introducir.

#b. A continuación, el programa ha de pedir cada uno de esos valores (pueden ser
#ecimales)

#c. Por último el programa indicará cuántos de esos números son negativos.

""" cantidad_valores = int(input("¿Cuántos valores vas a introducir? ")) """

""" if cantidad_valores < 0:
    print("Imposible")

else:
    
    for i in range(1,cantidad_valores + 1):
        numeros_introducidos = float(input(f"Escribe el numero {i}: "))

        numeros_negativos = 0
        if numeros_introducidos < 0:
            numeros_negativos += 1
    print(f"Has escrito {numeros_negativos} numeros negativos") """


cantidad_valores = int(input("¿Cuántos valores vas a introducir? "))

if cantidad_valores < 0:
    print("Imposible")

else:
    contador_negativos = 0
    for i in range(1, cantidad_valores + 1):

        if float(input(f"Escribe el numero {i}: ")) < 0:
            contador_negativos += 1
            
    print(f"Has escrito {contador_negativos} numeros negativos")