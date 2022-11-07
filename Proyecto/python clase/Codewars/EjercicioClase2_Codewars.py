 #https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python



def duplicate_encode(word):

    salida = ""
    for l in word.lower():
        ct = word.count(l)
        if ct == 1:
            salida += "("
        else:
            salida += ")"

    return salida
