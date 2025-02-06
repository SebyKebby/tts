from pypdf import PdfReader
from pdfminer.high_level import extract_text as fallback_text_extraction
import pyttsx3
engine = pyttsx3.init()
strict=False

#get the text from the pdf file
text = ""
try:
    reader = PdfReader(placeholder.pdf)
    for page in reader.pages:
        text += page.extract_text()
except Exception as exc:
    text = fallback_text_extraction("example.pdf")


#cleaning text
readable_text = text.strip().replace('\n', ' ')

#reading it
engine.say(readable_text)


#saving to mp3
engine.save_to_file(readable_text , 'test.mp3')
engine.runAndWait()