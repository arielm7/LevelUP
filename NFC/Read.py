#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import requests
import json

url = 'http://192.168.1.73/post.php'

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
                    nombre_usuario = usuario.split('/')
                    nombre = nombre_usuario[0]
                    autorizacion = nombre_usuario[1]
                    payload_nombre = {'Nombre' : nombre }
                    payload_id = {'ID' : id }
                    r_nombre = requests.post(url, data=json.dumps(payload_nombre))
                    r_id = requests.post(url, data=json.dumps(payload_id))
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
