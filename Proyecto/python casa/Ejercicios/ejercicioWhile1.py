#Crea un programa que pida números infinitamente. Los números introducidos deben 
# ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
# el anterior

numero_1 = int(input("Dame un numero: "))
numero_2 = int(input(f"Dame un numero mayor que {numero_1}: "))
    
while numero_2 > numero_1:
    numero_1 = numero_2
    numero_2 = int(input(f"Dame un numero mayor que {numero_1}: "))

print(f"{numero_2} no es mayor que {numero_1}")
    
    