from gtts import gTTS
from playsound import playsound

f = open("userip.txt", "w+")
userinput=str(input(" Enter text here:\t"))
f.write(userinput)
f.close()





