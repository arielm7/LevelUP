def lectura(usuario):
    print("Nivel de autorización va de 1-9, siendo 1 el más alto y 9 el más bajo")
    while True:
        try:
                print (usuario)
                nombre_usuario = usuario.split('/')
                print (nombre_usuario[0])
                print (nombre_usuario[1])
                if '*' in usuario:
                    print("Desbloquear funciones básicas del asistente, porque no se detectó la tarjeta")
                    return False
                elif nombre_usuario[1]=="1":
                    print("Desbloquear funciones avanzadas del asistente, por nivel de autorización")
                    return True
                else:
                    print("Desbloquear funciones básicas del asistente, por nivel de autorización")
                    return False
        finally:
            print("Se ha terminado la lectura")
