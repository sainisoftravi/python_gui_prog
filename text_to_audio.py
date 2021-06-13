
import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from gtts import *
from playsound import playsound

book = askopenfile("rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(1)
text = page.extractText()
ttos = gTTS(text)
speaker.say(ttos)
speaker.runAndWait()