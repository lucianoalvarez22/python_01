#https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

#Cree una función que tome un entero positivo como su parámetro y devuelva una cadena que contenga la representación en números romanos de ese entero.

#Los números romanos modernos se escriben expresando cada dígito por separado, comenzando con el dígito más a la izquierda y omitiendo cualquier dígito con un #valor de cero. En números romanos, 1990 se representa: 1000=M, 900=CM, 90=XC; resultando en MCMXC. 2008 se escribe como 2000=MM, 8=VIII; o MMVIII. 1666 utiliza #cada símbolo romano en orden descendente: MDCLXVI.

""" def solution(numero_romanos):

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
 """

integer_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def integer_to_roman(integer):
    roman = '' # Se declara la variable roman y se le asigna una cadena vacía.

    while integer > 0: # Mientras el número ingresado sea mayor a cero.
        for i, r in integer_roman: # Iteramos en la lista integer_roman sobre cada par entero-romano.
            while integer >= i: # Mientras el número sea mayor o igual al iterable i. 95 >= 90 -> roman = XC -> integer = 5
                roman += r # A la variable roman le sumamos lo que vale r.
                integer -= i # A la variable num le sumamos lo que vale r.

    return roman # Regresamos el número romano.

integer = int(input('Ingrese un número entero: '))
print(f'El número ingresado es: {integer_to_roman(integer)}')