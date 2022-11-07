#Crea un programa que muestre la tabla del ejercicio número 1, 
# utilizando bucles tipo for con tipos range() que tengan solamente un argumento.




for i in range(10):
    i +=1
    print(f"{i}\t",end="")

print()

for i in range (11):
    if i == 0:
        continue
    i = i*2
    print(f"{i}\t",end="")

print()
numero = 0
for i in range (45):
    if i>=17 and numero <= i:
        numero = i+3
        
        print(f"{numero}\t",end="")

print()

num=0
for i in range (27):
    if i >= 6 and num <=i:
        num = i + 4
        print(f"{num}\t",end="")

print()

offset = 0
for i in range(9):
    print(f'{(40-offset)}\t', end='')
    offset += 5

print()