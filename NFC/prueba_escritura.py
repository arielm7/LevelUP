import random
def escritura():
    Nombre = "Carlos"
    Nivel = random.randrange(10)
    str(Nivel)
    usuario = "%s/%s" %(Nombre,Nivel)
    return usuario
