#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

#Si se pone el número 1 indica autorización para todo, el numero 2 indica menor nivel de autorizacion
#y así sucesivamente
print("Nivel de autorización va de 1-9, siendo 1 el más alto y 9 el más bajo")

try:
        #text = raw_input("Nombre_NivelAcceso:")
        #print("Coloque la tarjeta")
        #reader.write(text)
        #print("Escrito")

        Nombre = raw_input("Digite el nombre del cliente:")
        Nivel = raw_input ("Digite el nivel de autorización:")
        text = "%s/%s" %(Nombre,Nivel)
        #usuario = "Nombre: %s / Autorización: %s" %(Nombre,Nivel)
        reader.write(text)
        print ("Escrito")
finally:
        GPIO.cleanup()
