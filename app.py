from flask import Flask
from flask import render_template
from transformers import pipeline
pipe = pipeline("image-classification", model="mushrooms_image_detection")
pipe("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/parrots.png")
app = Flask(__name__)
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/register")
def register():
    return render_template('register.html')
@app.route("/")
def cabinet():
    return render_template('cabinet.html')
