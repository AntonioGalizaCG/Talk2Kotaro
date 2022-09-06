#!/usr/bin/env python3
from PIL import Image
from io import BytesIO
import base64
import cv2
import numpy as np

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    return img

def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())

def base64_to_pil_image(base64_img):
    return Image.open(BytesIO(base64.b64decode(base64_img)))

def gibberish():
    from random import choice, random
    import subprocess
    import soundfile as sf
    import io
    min_len_words=1
    max_len_words=10
    min_len_phrase=1
    max_len_phrase=1
    consonants=["m", "M", "n[","n","n.","n^","N",'n"',"p","b","t[","d[","t","d","t.","d.","c","J","k","g","q","G","?","s","z","S","Z","s.","z.","P","B","f","v","T","D","C","C<vcd>","x","Q","X",'g"',"H","H<vcd>","h","h<?>","s<lat>","z<lat>", "r<lbd>","r[","r","r.","j","j<vel>",'g"', "l[","l","l.","l^","L","*","*.","*<lat>","b<trl>","r<trl>",'r"',"p!","t!","c!","k!","l!","b`","d`","J`","g`","G`","p`","t[`","t`","c`","k`","q`"]
    otherSymbols=["n<lbv>","t<lbv>","d<lbv>","w<vls>","w"]
    vowels=["i","y",'i"','u"',"u-","u","I","I.","U","e","Y","@<umd>","o-","o","@","@.","E","W",'V"','O"',"V","O","&","a","a.","A","A."]
    empty = [""]

    counter0 = 0
    max_len_phrase = choice(range(min_len_phrase, max_len_phrase+1))
    phrase = ""
    t0 = 0
    tries = 0

    while counter0 <= max_len_phrase:
        counter1 = 0
        wordlen = choice(range(min_len_words, max_len_words+1))
        word = ""
        while counter1 < wordlen:
            phoneme = choice(choice([vowels,consonants]))
            phoneme +=  choice(choice([vowels,consonants,otherSymbols,[""]]))
            if len(phoneme)>1:
                if phoneme[0] in consonants and phoneme[1] in consonants:
                    phoneme += choice(vowels)
                elif phoneme[1] in otherSymbols:
                    phoneme +=  choice(choice([vowels,consonants]))
                else:
                    phoneme +=  choice(choice([vowels,consonants,[""],[""],[""],[""],[""],[""]]))

            word+= phoneme+" "
            counter1+=1

        phrase += word+" "
        counter0 += 1
    return phrase
