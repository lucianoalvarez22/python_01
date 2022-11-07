
def alumno_nota (alumno_nombre, *asignaturas):
    print(f"El alumno {alumno_nombre} se ha matriculado de las asignaturas: ")
    print(asignaturas)
    for a in asignaturas:
        print(a)

""" asig = ["Programacion", "BD", "Sistemas","Filologia"] #UNA LISTA CON LAS ASIGNATURAS
alumno_nota("Miguel", *asig) #LE PONEMOS EL ASTERISCO A *ASIG PARA DESEMPAQUETARLA DE LA LISTA  """

def alumno_nota2 (alumno_nombre, *asignaturas, **notas):
    print(f"El alumno {alumno_nombre} se ha matriculado de las asignaturas: ")
    for a in asignaturas:
        print(a)
    for k,v in notas.items():
        print(f"{k}: {v}")


alumno = "Miguel"
asig = ["Programacion", "BD", "Sistemas","Filologia"] #UNA LISTA CON LAS ASIGNATURAS
notas = {
    "Programacion":7, 
    "BD":2.5,
    "Sistemas":5
    }
alumno_nota2(alumno,*asig,**notas ) #LE PONEMOS EL ASTERISCO A *ASIG PARA DESEMPAQUETARLA DE LA LISTA 