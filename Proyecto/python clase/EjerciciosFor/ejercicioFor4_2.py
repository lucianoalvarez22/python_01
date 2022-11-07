#Crea un programa que muestre el mismo resultado que en el ejercicio anterior, pero
#utilizando ahora bucles tipo for con tipos range() de dos argumentos. 

for i in range(1,11):
    print(f"{i}\t",end="")

print()

for i in range(2,21):
    if i % 2 == 0:
        print(f"{i}\t",end="")

print()


for i in range(20,49):
    if i % 3 == 0:
        i -= 1
        print(f"{i}\t",end="")

print()

for i in range(10,32):
    if i % 4 == 0:
        i -= 2
        print(f"{i}\t",end="")

print()
    
