
#UNA FUNCION DEBE TENER ALTA COHESION Y BAJO ACOPLAMIENTO, ES DECIR, QUE TENGA PARAMETROS  (ALTO ACOPLAMIENTO QUE SOLO SIRVE PARA ESA FUNCION)
#UNA VARIABLE QUE ESTÁ DENTRO DE UNA FUNCION, NO SE CONOCE FUERA DE LA FUNCION.
#UNA FUNCION NO DEBE SABER NADA DEL MUNDO EXTERIOR

def saluda(personas):
    salida = []
    for p in personas:
       salida.append(f"Hola, {p}")
    return salida

gente = ["Ana", "Miguel", "Dani"]
saludos = saluda(gente)
print (saludos)