#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
def funciones():
    while True:
        try:
                id, usuario = reader.read()
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
                print(id)
                print(usuario)
        finally:
                GPIO.cleanup()
    else:
        GPIO.cleanup()
