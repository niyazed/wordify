from PIL import Image
import pytesseract
from tika import parser
import docx2txt
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# os.environ["TIKA_SERVER_JAR"] = 'generator/functions/tika-server.jar'
# TIKA_SERVER_JAR="file:////tika-server.jar"

class textParse:
  def from_doc(path):
    text = docx2txt.process(path)
    return text
 
  def from_pdf(path):
    raw = parser.from_file(path)
    text = raw['content'] 
    # print(raw['content'])

    text = str(text)
    text=text.replace('\n',"")
    return text

  def from_image(path):
    im = Image.open(path)

    text = pytesseract.image_to_string(im, lang = 'eng')
    text = str(text)
    text=text.replace('\n',"")

    return text

