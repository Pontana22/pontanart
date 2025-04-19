import os

from lib.userinput import process_options
from lib.convert import convert
from flask import Flask, render_template, request

app = Flask(__name__)
root_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/create', methods=['POST'])
def create():
    image = request.files['image']
    image.save(image.filename)
    
    options = dict(request.form)
    options['img'] = image.filename
    
    process_options(options)
    
    convert(options, root_dir)
    
    return str(options)
    

    
        