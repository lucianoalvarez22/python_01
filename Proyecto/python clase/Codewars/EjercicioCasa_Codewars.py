#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

#Escriba una función que tome una cadena de una o más palabras y devuelva la misma cadena, pero con las palabras de cinco o más letras invertidas (al igual que el nombre de este Kata). Las cadenas pasadas consistirán solo en letras y espacios. Los espacios se incluirán solo cuando haya más de una palabra presente.

""" Ejemplo

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test" 

"""
def spin_words (cadena):
    textotroceado = cadena.split(" ")
    resultado = []
    for t in textotroceado:
        if len(t) >= 5:
            resultado.append(t[::-1]) 
        else:
            resultado.append(t)
    cadenafinal = " ".join(resultado)
    return cadenafinal

texto = "This is another test"
print(spin_words(texto))
    

    


