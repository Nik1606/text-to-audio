from gtts import gTTS
from playsound import playsound
import os


f = open("userip.txt", "w+")
userinput=str(input(" Enter text here:\t"))
f.write(userinput)
f.close()

ipread=open("userip.txt","r")
content=ipread.read()
ipread.close()

language='en'
obj=gTTS(text=content, lang=language, slow=False)
obj.save("exam.mp3")

playsound("exam.mp3")

os.remove("exam.mp3")
os.remove("userip.txt")


