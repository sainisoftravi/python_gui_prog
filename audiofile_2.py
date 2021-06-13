import PyPDF2 as reader
from gtts import *
import os
from playsound import playsound

filename = '/home/ravisaini/GrassClass/PDF/digit.pdf'

with open(filename,'rb') as file:
    pdf = reader.PdfFileReader(file)
    print(pdf.numPages)
    for num in range(pdf..numPages):
    page = pdf.getPage(num)
    text = page.extractText()
    print(text)
    tts = gTTS(text)
    savefile = f'{str(num)}.mp3'
    tts.save(savefile)
   # playsound("home/ravisaini/GrassClass/PDF/new1.mp3")
