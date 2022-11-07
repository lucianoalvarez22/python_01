import math

def superficie (radio=1):
    return radio * radio * math.pi






""" s = superficie(3)
print(s) """

def vol_cilindro (radio, altura):
    return superficie(radio) * altura

v = vol_cilindro(10,12)
print(v)