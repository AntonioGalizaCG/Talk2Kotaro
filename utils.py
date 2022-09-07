#!/usr/bin/env python3
from PIL import Image
from io import BytesIO
import base64
import cv2
import numpy as np
from random import choice, random
import subprocess
import soundfile as sf
import io

## @package utils
## Contains helper functions which do not fit in the other scripts.

## Converts the image from the browser side to OpenCV2 format (np.array).
## @param uri original image from the browser side in bytes;
## @retval img converted image in OpenCV2 np.array format.
def data_uri_to_cv2_img(uri):
    ## binary encoded image
    encoded_data = uri.split(',')[1]
    ## binary image decoded into a np.array.
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    ## image converted into OpenCV2 np.array format.
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    return img


## Converts the image from the PIL library format to OpenCV2 format (np.array).
## @param Image in the PIL format.
## @return PIL image converter to convert to OpenCV2 format (np.array).
def pil_image_to_base64(pil_image):
    ## buffer for input and output of bytes.
    buf = BytesIO()
    ## converts the encoded image into .JPEG format.
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())


## Converts the image from a base64 img to PIL format.
## @param base64_img base64 image to be converted.
## return image converted into PIL's format.
def base64_to_pil_image(base64_img):
    return Image.open(BytesIO(base64.b64decode(base64_img)))


## Generates Kotaro's semantic free speech contents.
## @retval phrase contents of Kotaro's gibberish speech.
def gibberish():
    ## minimum number of iterations to create a gibberish word; int.
    min_len_words=1
    ## maximum number of iterations to create a gibberish wordl; int.
    max_len_words=10
    ## minimum number of gibberish words in Kotaro's utterance; int.
    min_len_phrase=1
    ## maximum number of gibberish words in Kotaro's utterance; int.
    max_len_phrase=1
    ## list of consonantes in Kirshebaum's ASCII IPA notation; list of str.
    consonants=["m", "M", "n[","n","n.","n^","N",'n"',"p","b","t[","d[","t","d","t.","d.","c","J","k","g","q","G","?","s","z","S","Z","s.","z.","P","B","f","v","T","D","C","C<vcd>","x","Q","X",'g"',"H","H<vcd>","h","h<?>","s<lat>","z<lat>", "r<lbd>","r[","r","r.","j","j<vel>",'g"', "l[","l","l.","l^","L","*","*.","*<lat>","b<trl>","r<trl>",'r"',"p!","t!","c!","k!","l!","b`","d`","J`","g`","G`","p`","t[`","t`","c`","k`","q`"]
    ## list of vowels in Kirshebaum's ASCII IPA notation; list of str.
    vowels=["i","y",'i"','u"',"u-","u","I","I.","U","e","Y","@<umd>","o-","o","@","@.","E","W",'V"','O"',"V","O","&","a","a.","A","A."]
    ## list of "other symbols" in Kirshebaum's ASCII IPA notation; list of str.
    otherSymbols=["n<lbv>","t<lbv>","d<lbv>","w<vls>","w"]
    ## empty symbol
    empty = [""]
    ## number of gibberish words counter; int
    counter0 = 0
    ## randomly selectes the number of gibberish words for Kotaro's utterance
    ## int.
    max_len_phrase = choice(range(min_len_phrase, max_len_phrase+1))
    ## Kotaro's utterance; str.
    phrase = ""

    while counter0 <= max_len_phrase:
        ## number of iterations while forming gibberish words; int.
        counter1 = 0
        ## randomly selects the length of the next gibberish word; int.
        wordlen = choice(range(min_len_words, max_len_words+1))
        ## gibberish word to be added to Kotaro's utterance; str.
        word = ""
        while counter1 < wordlen:
            ## current phone to be added to the gibberish word; str.
            phone = choice(choice([vowels,consonants]))
            phone +=  choice(choice([vowels,consonants,otherSymbols,[""]]))
            if len(phone)>1:
                if phone[0] in consonants and phone[1] in consonants:
                    phone += choice(vowels)
                elif phone[1] in otherSymbols:
                    phone +=  choice(choice([vowels,consonants]))
                else:
                    phone +=  choice(choice([vowels,consonants,[""],[""],[""],[""],[""],[""]]))

            word+= phone+" "
            counter1+=1

        phrase += word+" "
        counter0 += 1
    return phrase
