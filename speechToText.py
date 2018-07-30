#Ariel Mata Vega
#LevelUp project 
import speech_recognition as sr
from google.cloud import texttospeech
from playsound import playsound
import os


#listens using the microphone and sends the audio to Google Speech to text 
#it return a dictionary which indicates if everything worked fine, the errorCode code if 
#something went wrong and finally the trasncription of the audio
def speechRecognizer(recognizer, microphone):
    
    # parameter type checking
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    ###########

    response = {
        "success": False, # True if everything went ok
        "errorCode": None, #error code for identification 
        "transcription": None #text obtained from the transcription of the speech
    }
    #recording from system microphone
    with microphone as source:
        recognizer.dynamic_energy_threshold = True  #used for avoiding noise efects 
        recognizer.pause_threshold = 1  #maximum amount of seconds between words 
        recognizer.adjust_for_ambient_noise(source, duration=1) #used for avoiding noise efects
        try:
            playsound('/home/ariel/LevelUp/startRecord.mp3')
            print('ya puede hablar...')
            audio = recognizer.listen(source,timeout=10,phrase_time_limit=5) #record of the audio obtained with the microphone
            print('fin grabacion...')
        except sr.WaitTimeoutError: #defined period for start talking is over
            print('se paso el tiempo y no hablo')
            response["errorCode"] = "timeOut"
            
    #########    	    	
    #transcription audio to text
    try:
    	#transcription of the audio using Google Cloud speech API
        response["transcription"] = recognizer.recognize_google(audio).lower() #used for testing
        #response["transcription"] = recognizer.recognize_google_cloud(audio,language='es-ES').lower()
        print('usted ha dicho: ' + response["transcription"] + '\n')
        response["success"] = True
    except sr.RequestError: # API was unreachable or unresponsive
        response["errorCode"] = 'conexion fallida'
        print('fallo de conexion')
             
    except sr.UnknownValueError: #unrecognizable speech is received
        print('No se entendio lo que dijo')
        response["errorCode"] = 'no se entendio lo que dijo'
        
       

    return response

##############################################
# Copyright 2018, Google, LLC.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.tr

## THIS CODE WAS MODIFIED FROM HIS ORIGINAL VERSION BY ELECTRISING
def playVoice(text): #takes a text variable as input parameter and plays it content as human-like speech 
    client = texttospeech.TextToSpeechClient() #client of the Google text to speech API
    input_text = texttospeech.types.SynthesisInput(text=text) #convertion of the input text variable

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams( #configuration of the used voice
        language_code='es-ES',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3) #audio format configuration

    response = client.synthesize_speech(input_text, voice, audio_config) #audio of the text content converted to speech

    # the audio is stored in the output.mp3 file 
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('archivo de audio creado')
    playsound('/home/ariel/LevelUp/output.mp3') #plays output.mp3 file    
######################

    

