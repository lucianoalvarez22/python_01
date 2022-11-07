#Escribe el código necesario para generar las siguientes 
# siete secuencias de números utilizando bucles for.


for i in range(1,11):
   print(f"{i*i}\t",end="")

print()

for i in range(1,11):
    i = i*i + 1
    print(f"{i}\t",end="")

print()

for i in range(2,8):
    i = i**3
    print(f"{i}\t",end="")

print()

for i in range(2,9):
    i = i*(i-1)
    print(f"{i}\t",end="")

print()

for i in range(0,5):
    i = 10**i
    print(f"{i}\t",end="")

print()

for i in range(1,6):
    i = 10/(10**i)
    print(f"{i}\t",end="")


print()

for i in range(0,8):
    if i % 2 == 0:
        print(f"{1}\t",end="")
    else:
        print(f"{-1}\t",end="")
    



    


   