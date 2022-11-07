
#Escribe un programa que pida por teclado dos números 
# y que indique cuál de ellos es el menor
#y cuál el mayor o bien si ambos números son iguales.

numero1 = float(input("Escribe un numero: "))
numero2 = float(input("Escribe otro numero: "))

if numero1 > numero2:
    print('Menor: ',numero2, '; Mayor:', numero1)

elif numero1 < numero2:
    print('Menor: ',numero1, '; Mayor:', numero2)

else:
    print("Los dos numero son iguales")


