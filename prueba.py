def prueba():
    print("Nivel de autorización va de 1-9, siendo 1 el más alto y 9 el más bajo")
    while True:
        try:
                Nombre = input("Digite el nombre del cliente:")
                Nivel = input ("Digite el nivel de autorización:")
                usuario = "Nombre: %s / Autorización: %s" %(Nombre,Nivel)
                print (usuario)
        finally:
                print("Se ha hecho la escritura")
                nivel_autorizacion = [int(s) for s in usuario.split() if s.isdigit()]
                if '*' in usuario:
                    print("Desbloquear funciones básicas del asistente, porque no se detectó la tarjeta")
                    return False
                elif nivel_autorizacion==[1]:
                    print("Desbloquear funciones avanzadas del asistente, por nivel de autorización")
                    return True
                else:
                    print("Desbloquear funciones básicas del asistente, por nivel de autorización")
                    return False
