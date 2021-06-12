import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

# duration is given in seconds

duration = 20

recording  = sound.rec(int(duration*freq), samplerate= freq, channels=2)

sound.wait()
write("recording.wav",freq,recording)
