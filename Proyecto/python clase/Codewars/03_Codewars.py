#https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def valid_braces(cadena):
    if len(cadena) % 2 == 1:
        return False
    parejas = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    valores = list(parejas.values())
    pila = []
    for s in cadena:
        if s in valores:
            pila.append(s)
        else:
            if pila == []:
                return False
            ultimo = pila.pop()
            if ultimo != parejas[s]:
                return False

    return pila == []

print(valid_braces("{[()]]"))



#ENTENDER ESTA FUNCION
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

