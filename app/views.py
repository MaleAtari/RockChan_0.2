from app import app
from flask import render_template
from app.my_captcha import MyCaptcha

@app.route('/')
def home():
    return render_template('home.html', kapcza=MyCaptcha())


