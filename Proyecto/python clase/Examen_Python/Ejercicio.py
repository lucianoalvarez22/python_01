""" 
Escribe una funcion que reciba como parametro una cadena de texto y devuelva una lista con las vocales que haya en dicha cadena
 """
#20
def cadena_vocal(texto):
    vocales = ['a', 'e','i','o','u']
    lista_vocales = []
    for letra in texto:
        if letra.lower() in vocales and letra.lower() not in lista_vocales:
            lista_vocales.append(letra)
    return lista_vocales
            
cadena = 'luciano'
#print(cadena_vocal(cadena))



""" 
Funcion que reciba una cadena y devuelva una cadena con los codigos ASCII de las letras
A = 65
B = 66
C = 67
 """

def txt_ascii (cadena):
    salida = []
    for i in cadena:
        salida.append(str(ord(i)))
    
    return ' '.join(salida)

cad = 'hola'
txt_ascii(cad)

""" Al reves ahora, de ASCCI a Cadena """

def ascii_txt(cadena):
    salida = ''
    cadena = cadena.split(' ')
    for c in cadena:
        salida += chr(int(c))
    return salida

ascii_txt(txt_ascii(cad))

def suma (num1, num2):
    suma = num1 + num2
    #print(f'La suma de los dos números es: {suma}')

num1 = 5
num2 = 4
#suma(num1,num2)


#num1 = int(input('Enter first number: '))
#num2 = int(input('Enter second number: '))
sum = num1 + num2
#print('The sum of the numbers is', sum)



num1 = 123
num2 = "456"
#print("Data type of num1:",type(num1))
#print("Data type of num2:",type(num2))
#print("Sum data type is:",type(num1 + num2))

txt = 'you are doing well' 
#print(txt[2:999])


""" s = 0
#for d in range(0, 5, 0.1):
s += d
#print(s) """