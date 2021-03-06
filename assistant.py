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
import rgb_led

if __name__ == "__main__":
    r=sr.Recognizer()
    m=sr.Microphone()
    inicio = 'Hola'
    bienvenida = 'bienvenido!'
    url = 'http://192.168.10.105/watson.php'
    
    class StopThread(StopIteration): pass
    threading.SystemExit = SystemExit, StopThread 
    
    class Thread2(threading.Thread):
		def stop(self):
			self._stop=True
		def _bootstrap(self):
			if threading._trace_hook is not None:
				raise ValueError('Cannot Run thread with tracing')
			self._stop=False
			sys.settrace(self._trace)
			super()._bootstrap
		def _trace(self, frame, event, arg):
			if self._stop:
				raise StopThread()
			return self._trace
			
			
    
    while(True):
	    keyWordListener.keyWordListener()
	    autorizacion, id, nombre, nivel, num_habitacion = Read.Read()
	    if autorizacion:
			mensaje_inicial = '%s %s, %s' %(inicio, nombre, bienvenida)
			speechToText.playVoice(mensaje_inicial)		
	    else:
			speechToText.playVoice('Bienvenido')	
		
				
	    color='1'
	    if color=='1':
			flashing_thread = Thread2(target=rgb_led.rgb(color))
			flashing_thread.start()
	    else:
			print '2'
	    response=speechToText.speechRecognizer(r,m)
	    if response["success"]==True:
			color='2'
			flashing_thread.stop()
			flashing_thread = Thread2(target = rgb_led.rgb(color))
			os.system("mpg123 /home/pi/levelUP/success.mp3")
			print(response["transcription"])
			payload = {'knx':response["transcription"], 'nombre': nombre, 'id': id, 'autorizacion': nivel, 'num_habitacion': num_habitacion}
			resp = requests.get(url,params=payload)
			#text_f = resp.text.split("'")
			#print(text_f)
			print(resp.text)
			#if True:
				#str(text_f[1])
			speechToText.playVoice(resp.text)
			flashing_thread.stop()
			#else:
				#str(text_f[0])
				#speechToText.playVoice(resp.text)


	    else:
	    	os.system("mpg123 /home/pi/levelUP/fail.mp3")
	    	flashing_thread = Thread2(target = rgb_led.rgb('3'))
	    	speechToText.playVoice(response["errorCode"])
	    	flashing_thread.stop()

    
