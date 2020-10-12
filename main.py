import pyttsx3
import PyPDF2
from pyttsx3 import engine
engine = pyttsx3.init()
book = open('monk.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('Current Rate of Speaking -' , rate)   #printing current voice rate
engine.setProperty('rate', 125)      #125 is the value set for speaking words , change accordingly to your preference
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #voices[1]->for female voice and voices[0]->for male
print('No. of pages in Book-' ,pages)
speaker = pyttsx3.init()
for num in range(10, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
