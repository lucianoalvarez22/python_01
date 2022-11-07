
#Hacer un procedimiento que cuente el nº de cada una de las vocales de una cadena

cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

""" cuenta_a = 0
cuenta_e = 0
cuenta_i = 0
cuenta_o = 0
cuenta_u = 0


for c in cadena:
    if c == "a":
        cuenta_a +=1
    elif c == "e":
        cuenta_e +=1

    elif c == "i":
        cuenta_i +=1
    
    elif c == "o":
        cuenta_o +=1
    
    elif c == "u":
        cuenta_u +=1

print(f"a: {cuenta_a}, e: {cuenta_e}, i: {cuenta_i}, o: {cuenta_o}, u: {cuenta_u}") """


# -----------------------------------------------------

""" vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
letra = "aeiou"

for c in cadena.lower():
    if c in letra:
        vocales[c] += 1

print(vocales)  """

#--------------------------------
vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
letra = "aeiou"

for c in letra:
    vocales[c] = cadena.lower().count(c)

print(vocales)