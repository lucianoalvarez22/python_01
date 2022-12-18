
""" def esto_falla (): 
    try: #Abrimos el archivo para ver si existe. Si no existe, pasa el EXCEPT. Si existe va al ELSE. Y al final tanto si existe como sino, va al FINALLY
        f = open('no_existe.txt', 'r')

    except FileNotFoundError as e: #Cuando sepamos el nombre del error, lo podemos sustituir con el Exception. En este caso podriamos poner "FileNotFoundError as e"
        print(e)
    else: #En caso de que el archivo existe, pasa al else
        pass
    
    finally:  #Si hay un error o no, pasa a finally
        pass """




def genera_error(num): #Funcion para generar el error que QUERAMOS. 
    if num < 10: #Si numero es menor que 10...ERROR! Pasa a Exception
        raise Exception('Error de numero demasiado pequeño') #Levantamos(raise) una excepcion de tipo objects(Cualquiera)
    else:
        print("Funciona")

try:
    genera_error(5)
except:
    exit()


