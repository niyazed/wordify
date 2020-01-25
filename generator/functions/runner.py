from make_keyword_wordart import generate
# from make_wordart import make_wordart
from textParse import textParse
import nltk
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
import os
import sys


def filetype(name):
    file_name, file_extension = os.path.splitext(name)

    doc = [".docx",".doc",".DOCX"]
    pdf = [".PDF",".pdf"]
    text = [".txt",".rtf",".TXT"]
    image = [".PNG",".jpg",".png",".jpeg",".JPG",".svg",".bmp",".BMP"]
    ans = ""
    if file_extension in doc:
    	ans = "doc"
    if file_extension in pdf:
    	ans = "pdf"
    if file_extension in text:
    	ans = "txt"
    if file_extension in image:
    	ans = "img"
    return ans

file_name = sys.argv[1]

ftype = filetype(file_name)
print(ftype)
text =""
if ftype == "pdf":
	text = textParse.from_pdf(file_name)
if ftype == "doc":
	text = textParse.from_doc(file_name)
if ftype == "img":
	text = textParse.from_image(file_name)


mk = generate(text)
kw = mk.generate_keyword()

hmap = {}
for x in kw:
    hmap[x[0]]=x[1]
wordcloud = WordCloud(font_path='kalpurush.ttf',min_font_size = 10, background_color="white").generate_from_frequencies(hmap)
wordcloud.to_file('cloud.png')
print(kw[:10])




