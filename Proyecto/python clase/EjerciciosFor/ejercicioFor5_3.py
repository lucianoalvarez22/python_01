#Modifica el programa anterior de tal forma que los caracteres utilizados en el 
# perímetro del rectángulo sean caracteres producto (*) y el interior esté vacío.

#numero = int(input("Dame un numero "))

base= 5
altura=4
veces = 2
#EMPIEZA DE ABAJO A ARRIBA

linea_1 = "*\t" * base
linea_2 = "*\t" + "\t" * (base-2) + "*"

for x in range(veces):
    print(linea_1)

    for i in range(altura-2):
        print(linea_2)

    
    print(linea_1)
    print()

    
