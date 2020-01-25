from django.shortcuts import render
from django.http import HttpResponse

# Generation functions imports
from generator.functions.make_keyword_wordart import generate
# from make_wordart import make_wordart
from generator.functions.textParse import textParse
import nltk
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
import pytesseract

import os
import sys
# Create your views here.

def generator(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        ftype = filetype(uploaded_file.name)
        print(ftype)
        
        if ftype == "pdf":
            text = textParse.from_pdf(uploaded_file)
        if ftype == "doc":
            text = textParse.from_doc(uploaded_file)
        if ftype == "img":
            text = textParse.from_image(uploaded_file)

        print(text)

        mk = generate(text)
        kw = mk.generate_keyword()

        hmap = {}

        for x in kw:
            hmap[x[0]]=x[1]
        wordcloud = WordCloud(font_path='generator/functions/kalpurush.ttf',min_font_size = 10, background_color="white").generate_from_frequencies(hmap)
        wordcloud.to_file('wordarts/'+uploaded_file.name+'.png')
        print(kw[:10])
        
    return render(request, 'generate.html')

# Detemine the filetype
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
