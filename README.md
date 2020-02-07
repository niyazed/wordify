# Wordify

## Installation
### Postgres and pgadmin Installation
--------------------------------

Youtube link - 
1. https://www.youtube.com/watch?v=Vdzb7JTPnGk
2. https://www.youtube.com/watch?v=-LwI4HMR_Eg

### NLTK
-----
```
type 'python' in CLI
--------------------
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('wordnet')
````
### Pytesseract
-----------
First you should install binary:
##### On Linux
```
    $ sudo apt-get update
    $ sudo apt-get install tesseract-ocr
    $ sudo apt-get install libtesseract-dev
```
##### On Mac
`
brew install tesseract
`
##### On Windows
```
download binary from https://github.com/UB-Mannheim/tesseract/wiki. 
then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.
Then you should install python package using pip:

    $ pip install tesseract
    $ pip install tesseract-ocr
```
