# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:34:28 2022

@author: ahmet
"""
import pytchat
import time
from utils.getkeys import key_check
from textblob import TextBlob
from google_trans_new import google_translator  

translator = google_translator()  

stream = pytchat.create(video_id = "XXXXXXXXX")
analiz = []
infos = []

def sent(text):
    translate_text = translator.translate(text,lang_tgt='en')  
    blob = TextBlob(translate_text)
    sentiment = blob.sentiment.polarity
    if sentiment != 0.0:
        analiz.append(sentiment)



while True:
    data = stream.get()
    items = data.items
    time.sleep(0.01)
    for c in items:
        #print(f"{c.datetime} [{c.author.name}]- {c.message}")
        infos.append(c.message)
        sent(infos[-1])
        ortalama = sum(analiz)/len(analiz)*100
        print(f"Puan: {analiz[-1]}, Ortalama: {ortalama}")
    keys = key_check()
    if keys == "H":
        break