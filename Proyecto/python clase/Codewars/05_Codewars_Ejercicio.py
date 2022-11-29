#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

""" Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" 


"""


def solution(s):
    for p in s:
        if p.isupper():
            posicion = s.find(p) #La posicion de la mayus
            s_principio = s[0:posicion] #La palabra desde 0 hasta la Mayus
            s_final = s[posicion:] #La palabra desde la mayus al final
            print(f"{s_principio} {s_final}")
            break
    if s.islower() or s == '""':
        print(s)

        


palabra = input('Introduce una palabra: ')
solution(palabra)


