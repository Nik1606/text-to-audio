from gtts import gTTS
from playsound import playsound

text_input = str(input("Enter text here"))
file=open('user-input.txt','w+')
file.write(text_input)
file.close()

filex = open('user-input.txt', 'r')
language='en'
obj=gTTS(text=filex, lang=language, slow=False)
obj.save("outputx.mp3")
playsound("outputx.mp3")

