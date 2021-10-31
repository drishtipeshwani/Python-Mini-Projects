# importing the modules
import PyPDF2
import pyttsx3
  
# path of the PDF file
path = open('file.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# Defining the speaker
speaker = pyttsx3.init()

# For loop to read each and every page from pdf  
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()