#!/home/jack/Desktop/StoryMaker/env/bin/python
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response,flash
from flask import send_file, make_response,g
import os
import subprocess 
import shutil  
import logging
import random
from random import randint
import glob
import datetime
import time
from werkzeug.utils import secure_filename
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from logging.handlers import RotatingFileHandler
import uuid

app = Flask(__name__)

app.secret_key = os.urandom(24)

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

# Create a file handler to write log messages to a file
file_handler = RotatingFileHandler('Logs/app.log', maxBytes=10000, backupCount=1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Now you can use the logger to log messages

TEXT = "TEXT TEST abcd"
logger.debug('This is a debug message: %s', TEXT)
# Set up logging for the Flask app
app.logger.addHandler(file_handler)
# Create a logger object
logging.basicConfig(level=logging.DEBUG)
directory_path = "static/current_project"

if not os.path.exists(directory_path):
    os.makedirs(directory_path)
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


def zip_lists(list1, list2):
    return zip(list1, list2)

app.jinja_env.filters['zip'] = zip_lists

directory_path = 'temp'  # Replace with the desired directory path
# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

@app.route('/')
def index():
    image_dir = 'static/images'
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    random_image_file = random.choice(image_files)
    return render_template('index.html', random_image_file="images/"+random_image_file)

@app.route('/mkmoz', methods=['GET', 'POST'])
def mkmoz():
    im = Image.new("RGB", (2048,2048), (250,250,250))
    for i in range(0,2500):
        if i< 500:DIR = "/home/jack/.cache/thumbnails/large/*.png"
        if i> 500:DIR = "/home/jack/.cache/thumbnails/normal/*.png"
        #if i> 2495:DIR = "/home/jack/.cache/thumbnails/large/*.png"
        thumb = random.choice(glob.glob(DIR))
        print("THUMB:",thumb)
        Thum = Image.open(thumb)            
        im.paste(Thum,((randint(0,im.size[0])),randint(0,im.size[1])-50))
        filename = "static/images/ThumbNails.png"
        im.save(filename)
        Filename="images/ThumbNails.png"
    return render_template("mkmoz.html", filename=Filename)


@app.route('/mk_background', methods=['GET', 'POST'])
def mk_background():
    im = Image.new("RGB", (8000, 512), (127, 255, 127))
    for i in range(0, 1000):
        if i < 250:
            DIR = "/home/jack/.cache/thumbnails/large/*.png"
        else:
            DIR = "/home/jack/.cache/thumbnails/normal/*.png"
        thumb = random.choice(glob.glob(DIR))
        print("THUMB:", thumb)
        Thum = Image.open(thumb)
        im.paste(Thum, ((randint(0, im.size[0])), randint(0, im.size[1]) - 50))
        filename = "static/images/ThumbNails_Background.png"
        im.save(filename)
    return redirect('/mkvid')

@app.route('/mkvid')
def mkvid():
    Filename = "static/images/ThumbNails_Background.png"
    Video_file = "static/images/ThumbNails_Background_FFmpeg.mp4"
    command = [
        'FFmpeg', '-hide_banner',
        '-loop', '1', '-i', 'static/images/ThumbNails_Background.png',
        '-vf', 'scale=8000:512,scroll=horizontal=0.0001,crop=768:512:0:0,format=yuv420p',
        '-t', '240', '-y', 'static/images/ThumbNails_Background_FFmpeg.mp4'
    ]
    subprocess.run(command)
    return redirect('/mkvid2')

@app.route('/mkvid2')
def mkvid2():   
    command2 = [
    'ffmpeg', '-hide_banner',
    '-i', 'static/images/ThumbNails_Background_FFmpeg.mp4',
    '-vf', 'scale=512:768,setsar=1/1',
    '-c:a', 'copy', '-y','static/images/long_512-768.mp4'
    ]
    subprocess.run(command2)
    
    command3 = [
    'ffmpeg', '-hide_banner',
    '-i', 'static/images/ThumbNails_Background_FFmpeg.mp4',
    '-c:a', 'copy', '-y','static/images/assets/ThumbNails_Background.mp4'
    ]
    subprocess.run(command3)   
    Filenamez = "images/ThumbNails_Background.png"
    Video_filez = "images/long_512-768.mp4"   
    return render_template("mkvid2.html", filename=Filenamez, video=Video_filez)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

