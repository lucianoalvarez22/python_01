#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

""" Complete la solución para que divida la cadena en pares de dos caracteres. Si la cadena contiene un número impar de caracteres, debe reemplazar el segundo carácter faltante del par final con un guión bajo ('_').

Ejemplos:

'abc' =>  ['ab', 'c_']
'abcdef' => ['ab', 'cd', 'ef'] """

def solution(s):
  ultimo_caracter = ''
  if len(s)%2 != 0:
    ultimo_caracter = s[-1]
    s = s[0:len(s)-1]
  lista_caracteres = []
  for c in range(0,len(s), 2):
    lista_caracteres.append(s[c:c+2])

  if ultimo_caracter != '':
    lista_caracteres.append(ultimo_caracter +'_')
  print(lista_caracteres)

cadena = input("Introduce una cadena: ")
print(solution(cadena))







  """ lista = []
  contador = 0
  for i in s:
    contador += 1
    if contador == 1:
      lista.append(i)
      contador = 0
  print(lista) """

  

"""  if lista[0] and lista [1] == True:
    unir = ''.join(lista)
  print(lista.append(unir))  """
    

    






