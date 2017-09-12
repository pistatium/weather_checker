# coding: utf-8

import os
import sys 
import io
import datetime
import time
from PIL import Image, ImageFilter, ImageChops

import requests


CAPTURE_URL = os.environ['CAPTURE_URL']

def get_image(url):
    data = requests.get(url).content
    return Image.open(io.BytesIO(data))
    
def sum_px(img):
    return sum(list(img.convert('L').getdata()))

def diffimage( img1, img2 ):
    img1 = img1.crop((240, 380, 460, 480))
    img2 = img2.crop((240, 380, 460, 480))
    subtract = ImageChops.subtract( img1 , img2 )
    return subtract

if __name__ == "__main__":
    img1 = get_image(CAPTURE_URL)
    time.sleep(0.1)
    img2 = get_image(CAPTURE_URL)
    diff = diffimage( img1, img2 )
    print(sum_px(diff))
    with open('result.csv', 'a') as f:
        f.write('{},{}\n'.format(datetime.datetime.now(), sum_px(diff)))
