# 10. Diseña un programa que pregunte por la cantidad de números que se van a introducir. 
# A continuación, la aplicación debe de mostrar como resultado el mayor, el menor y 
# la media aritmética de todos ellos.

cantidad_valores = int(input("¿Cuántos valores vas a introducir? "))

if cantidad_valores < 0:
    print("Imposible")

else:
    
    for i in range(1, cantidad_valores + 1):
        