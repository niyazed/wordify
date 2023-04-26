import json
from fastapi import FastAPI, File, UploadFile, Request,Form
from fastapi.staticfiles import StaticFiles
from modules import utils

import shutil
import os
import time
import socket

HOST = '0.0.0.0'  #socket.gethostbyname(socket.gethostname())
MEDIA_PATH = 'media'
WORDART_PATH = 'wordarts'

if not os.path.exists(MEDIA_PATH):
    os.mkdir(MEDIA_PATH)

if not os.path.exists(WORDART_PATH):
    os.mkdir(WORDART_PATH)


app = FastAPI(title="Wordify Swagger")
app.mount("/static", StaticFiles(directory="wordarts"), name="static")


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    filepath = "media/"+file.filename
    wordarts_path = "wordarts/"
    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        return {"message": "There was an error uploading the file"}

    wordart_name, top_ten_kw = utils.wordify(file, filepath, wordarts_path)

    return {
            "wordart_url": f"http://{HOST}:8001/static/{wordart_name}",
            "top_ten_keywords": f"{top_ten_kw}"
            }
