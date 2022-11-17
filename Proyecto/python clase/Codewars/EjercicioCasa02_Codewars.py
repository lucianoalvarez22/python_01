#https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

#Cree una función que tome un entero positivo como su parámetro y devuelva una cadena que contenga la representación en números romanos de ese entero.

#Los números romanos modernos se escriben expresando cada dígito por separado, comenzando con el dígito más a la izquierda y omitiendo cualquier dígito con un #valor de cero. En números romanos, 1990 se representa: 1000=M, 900=CM, 90=XC; resultando en MCMXC. 2008 se escribe como 2000=MM, 8=VIII; o MMVIII. 1666 utiliza #cada símbolo romano en orden descendente: MDCLXVI.

def solution(numero_romanos):

    simbolo = {
        1:"I",
        4: "IV",
        5:"V",
        9:"IX",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    lista = []
    
    if len(numero_romanos) < 1:
        return len(numero_romanos)

    #return simbolo.get(numero_romanos)


numero = int(input("Introduce un numero: "))
print(solution(numero))
