from app import app
from flask import render_template, request, redirect, url_for, session
from app.my_captcha import MyCaptcha
from app.users.func import is_checked, make_empty_user, user_is_checked
import functools


# def is_checked(f):
#     @functools.wraps(f)
#     def decorated_func(*args, **kwargs):
#         if session.get('is_checked') == True:
#             return f(*args, **kwargs)
#         else:
#             return redirect(url_for('main'))
#     return decorated_func








@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        user_info = make_empty_user()
        mycaptcha = MyCaptcha()
        session['captcha'] = mycaptcha.captcha_text
        session['user_info'] = user_info


    if request.method == 'POST':
        userCaptcha = request.form['userCaptcha']

        if userCaptcha == session['captcha']:
            session['user_info'] = user_is_checked()
            return redirect(url_for('home'))
        else:
            return redirect(url_for('main'))



    return render_template('main.html', mycaptcha=mycaptcha)


@app.route('/home')
@is_checked
def home():
    return render_template('home.html', kapcza=MyCaptcha())







