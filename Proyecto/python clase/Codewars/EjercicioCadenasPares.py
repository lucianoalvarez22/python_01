#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

""" Complete la solución para que divida la cadena en pares de dos caracteres. Si la cadena contiene un número impar de caracteres, debe reemplazar el segundo carácter faltante del par final con un guión bajo ('_').

Ejemplos:

'abc' =>  ['ab', 'c_']
'abcdef' => ['ab', 'cd', 'ef'] """

def solution(s):
  trozos = s.split("")
  print(trozos)





cadena = input("Introduce una cadena: ")

print(solution(cadena))