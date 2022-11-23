#Programa que pida 2 numeros al usuario y una operacion matematica a ejecutar con esos dos numeros
#Las operaciones son:
#Suma 
#Resta - El primero menos el segundo
#Multiplicacion
#Division - al primero sobre el segundo
#Exponeniacion - el primero es la base y el segundo el exponente
#Radicacion - el primero es el radicando y el segundo es el indice



def suma(a,b):
    return a + b

def resta(a,b):
    return a + b

def multi (a,b):
    return a * b

def div (a,b):
    return a / b

def exponenciacion (a,b):
    return a ** b

def radicacion (a,b):
    return a ** (1/b)
    

primer_numero = float(input("Inserta el primer numero: "))
segundo_numero = float(input("Inserta el segundo numero: "))
print("Opciones de operacion: 1. Suma 2. Resta 3. Multiplicacion 4. Division 5.Exponenciacion 6.Radicacion")
operacion_realizar = int(input("Ingresa el numero de la operacion que deseas: "))

if operacion_realizar == 1:
    print(f'{primer_numero} + {segundo_numero} = {suma(primer_numero,segundo_numero)}')

elif operacion_realizar == 2:
    print(f'{primer_numero} - {segundo_numero} = {resta(primer_numero,segundo_numero)}')

elif operacion_realizar == 3:
    print(f'{primer_numero} X {segundo_numero} = {multi(primer_numero,segundo_numero)}')

elif operacion_realizar == 4:
    print(f'{primer_numero} / {segundo_numero} = {div(primer_numero,segundo_numero)}')

elif operacion_realizar == 5:
    print(f'{primer_numero} ^ {segundo_numero} = {exponenciacion(primer_numero,segundo_numero)}')

elif operacion_realizar == 6:
    print(f'{primer_numero} ^ 1/ {segundo_numero} = {radicacion(primer_numero,segundo_numero)}')

else:
    print("ERROR!! Ingrese un número válido")
    
    
    







