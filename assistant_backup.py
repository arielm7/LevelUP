import keyWordListener
import speechToText
import os
import speech_recognition as sr
import Read
import requests
import json
import RPi.GPIO as GPIO
import threading
import sys
import time

if __name__ == "__main__":
    r=sr.Recognizer()
    m=sr.Microphone()
    inicio = 'Hola'
    bienvenida = 'bienvenido!'
    url = 'http://192.168.10.105/watson.php'
    leds = 'escuchar'
    
    while(True):
	    keyWordListener.keyWordListener()
	    autorizacion, id, nombre, nivel, num_habitacion = Read.Read()
	    if autorizacion:
			mensaje_inicial = '%s %s, %s' %(inicio, nombre, bienvenida)
			speechToText.playVoice(mensaje_inicial)		
	    else:
			speechToText.playVoice('Bienvenido')	
				
	    #Aqui se reproducen los leds
	    response=speechToText.speechRecognizer(r,m)
	    if response["success"]==True:
			os.system("mpg123 /home/pi/levelUP/success.mp3")
			print(response["transcription"])
			payload = {'knx':response["transcription"], 'nombre': nombre, 'id': id, 'autorizacion': nivel, 'num_habitacion': num_habitacion}
			resp = requests.get(url,params=payload)
			#text_f = resp.text.split("'")
			#print(text_f)
			print(resp.text)
			if True:
				#str(text_f[1])
				speechToText.playVoice(resp.text)
			else:
				#str(text_f[0])
				speechToText.playVoice(resp.text)


	    else:
	    	os.system("mpg123 /home/pi/levelUP/fail.mp3")
	    	speechToText.playVoice(response["errorCode"])

    
