
import speech_recognition as sr
import os


#escucha por el microfono y envia el audio al API de Google Speech to text 
#retorna un diccionario que indica si hubo exito, el error que hubo en caso de que existiera y la trasncripicion del audio
def audioATexto():
    
    r = sr.Recognizer()
    respuesta = {
        "exito": True,
        "error": None,
        "transcripcion": None
    }

    with sr.Microphone() as source:
        r.dynamic_energy_threshold = True
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        try:
        	print('ya puede hablar...')
        	audio = r.listen(source,timeout=10,phrase_time_limit=30)
        except sr.WaitTimeoutError:
        	print('se paso el tiempo y no hablo')
        	respuesta["exito"] = False
        	respuesta["error"] = "timeOut"
        	    	
    try:
        respuesta["transcripcion"] = r.recognize_google(audio).lower()
        #command = r.recognize_google_cloud(audio,language='es-MX').lower()
        print('usted ha dicho: ' + respuesta["transcripcion"] + '\n')

    except sr.RequestError:
        # API was unreachable or unresponsive
        respuesta["exito"] = False
        respuesta["error"] = "falloConexion"
        print('fallo de conexion')    
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('No se entendio lo que dijo')
        respuesta["exito"] = False
        respuesta["error"] = "noEntendido"
       

    return respuesta
print(audioATexto()["transcripcion"])
