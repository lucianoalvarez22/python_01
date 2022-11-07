#Escribe un programa que permita sumar números, la aplicación debe funcionar de la
#siguiente forma: 

# a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir

# b. A continuación, el programa debe pedir cada uno de esos valores (pueden ser decimales)

# c. Por último el programa calculará la suma de todos ellos y mostrará el resultado por 
# pantalla.


cantidad_valores = int(input("¿Cuántos valores vas a introducir? "))

if cantidad_valores < 0:
    print("Imposible")

else:
    suma = 0
    for i in range(1,cantidad_valores + 1):
        numeros_introducidos = float(input(f"Escribe el numero {i}: "))
        suma = suma + numeros_introducidos
    print(f"La suma de los numeros que has escrito es {suma}")