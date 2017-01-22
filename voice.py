from tts_watson.TtsWatson import TtsWatson 

def speak(dialog):
	ttsWatson = TtsWatson('0c35d3e5-a8d5-4bc8-bbdd-a6e32a0afe20', 'Qt8sQUmLly46', 'en-US_AllisonVoice') 
	# en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices 
	ttsWatson.play(dialog) 

