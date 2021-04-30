
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import speech_recognition as speech
from gtts import gTTS
import os


r = speech.Recognizer()
my_mic = speech.Microphone(device_index=1) 
with my_mic as source:
    print("WHATS YOUR MOOD TODAY ?!.... ")
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source)

    mytext = r.recognize_google(audio)
    print(mytext)
language='en'
output=gTTS(text=mytext, lang=language, slow=False)
output.save("final.wav")
os.system("start final.wav")

    
with open('final.wav','wb') as f:
         f.write(audio.get_wav_data())
             
             
input_data = read("final.wav")
audio = input_data[1]
plt.plot(audio[0:1024])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("VOICE AS WAVEFORM")
plt.show()


