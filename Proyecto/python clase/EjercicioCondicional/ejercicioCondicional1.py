#Escribe un programa que pida por teclado dos números enteros. 
# A continuación, el programa debe calcular su división, 
# escribiendo el cociente entero, en caso de que el resto
#no sea cero, habrá que mostrar también el valor del resto entero.


dividendo = int(input("Dame el dividendo: "))
divisor = int(input("Dame el dividor: "))


if divisor ==0:
    print("NO se puede dividir por 0")
else:
    cociente = int(dividendo/divisor)
    resto = dividendo%divisor

    if resto ==0:
        print('La division no es exacta. Cociente: ',cociente, 'Resto: ', resto)

    else:
        print('La division es exacta. Cociente: ',cociente)








