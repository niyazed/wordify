FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /workspace/requirements.txt

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

RUN python -c "import nltk; nltk.download('punkt');"
RUN python -c "import nltk; nltk.download('averaged_perceptron_tagger');"
RUN python -c "import nltk; nltk.download('wordnet');"
RUN python -c "import nltk; nltk.download('omw-1.4');"