import keyWordListener
import speechToText
import speech_recognition as sr
from playsound import playsound

if __name__ == "__main__":
    r=sr.Recognizer()
    m=sr.Microphone()
    while(True):
	    keyWordListener.keyWordListener()
	    response=speechToText.speechRecognizer(r,m)
	    if response["success"]==True:
	    	playsound('/home/ariel/LevelUp/success.mp3')
	    	print(response["transcription"])
	    	speechToText.playVoice(response["transcription"])
	    	##send trascription to server
	    	##KNX
	    	##

	    else:
	    	playsound('/home/ariel/LevelUp/fail.mp3')
	    	speechToText.playVoice(response["errorCode"])

    