import pyttsx3
from PyPDF2 import PdfReader

pdf_path = r""

with open(pdf_path, "rb") as pdf_book:
    reading_pdf = PdfReader(pdf_book)
    pages = len(reading_pdf.pages)

    speaker = pyttsx3.init()
    page_to_read = reading_pdf.pages[3]
    text = page_to_read.extract_text()
    
    speaker.say(text)
    speaker.runAndWait()

pdf_book.close()

