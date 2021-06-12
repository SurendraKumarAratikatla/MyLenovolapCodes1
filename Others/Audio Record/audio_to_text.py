import speech_recognition as sr
from scipy.io.wavfile import write

r = sr.Recognizer()
freq = 44100
with sr.Microphone() as source:
    print("Speak anything, i am listening you...")
    audio = r.listen(source)

    #try:
if r.recognize_google(audio):
    text = r.recognize_google(audio)
    write("recording1.wav",audio)
    print("you said: {}".format(text))
    #except:
     #   print("sorry could not recognize your voice, try again")