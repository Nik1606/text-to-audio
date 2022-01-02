from gtts import gTTS
from playsound import playsound

f = open("userip.txt", "w+")
userinput=str(input(" Enter text here:\t"))
f.write(userinput)
f.close()

ipread=open("userip.txt","r")
content=ipread.read()
print(type(content))

language='en'
obj=gTTS(text=content, lang=language, slow=False)
obj.save("exam.mp3")

playsound("exam.mp3")



