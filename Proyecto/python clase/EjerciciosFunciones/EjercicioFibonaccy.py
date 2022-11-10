#SUCECSION DE FIBONACCI
#EJEMPLO 1,1,2,3,5,8,13

def fibonacci(n):
    resultado = 1
    num1 = 0
    num2 = 1
    for i in range(n):
        resultado = num1 + num2
        num1 = num2
        num2 =resultado

    return resultado

print(fibonacci(0))


""" sucesion = [1,1,2,3,5,8,13]
print(fibonacci(sucesion)) """