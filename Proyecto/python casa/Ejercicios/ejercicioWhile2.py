#Crea un programa que pida números positivos indefinidamente. 
# El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos

numero_positivo = int(input("Dame numero positivo: "))
cajon = 0
while numero_positivo > 0:
    cajon = numero_positivo + cajon
    numero_positivo = int(input("Dame numero positivo: "))

print(f"{numero_positivo} es un numero negativo, la suma de todos los numeros introducidos es {cajon}")