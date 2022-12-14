from app import app
from flask import render_template, request, redirect, url_for, session
from app.my_captcha import MyCaptcha
from app.users.func import is_checked, make_empty_user, user_is_checked


@app.route('/', methods=['POST', 'GET'])
def main():

    if request.method == 'GET':
        # if session.get('user_info', 'count'):
        try:
            if session['user_info']['count'] > 0:
                return redirect(url_for('home'))
        except:
            pass

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
    mycaptcha = MyCaptcha()
    return render_template('home.html', kapcza=MyCaptcha(), mycaptcha=mycaptcha)



@app.route('/ohh_noo')
def ohh_noo():
    return render_template('no_enter.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/anty_spam', methods=['POST', 'GET'])
def anty_spam():
    if session['user_info']['count'] > 0:
        return redirect(url_for('home'))
    if request.method == 'GET':
        mycaptcha = MyCaptcha(char_count=4)
        session['captcha'] = mycaptcha.captcha_text

    if request.method == 'POST':
        userCaptcha = request.form['userCaptcha']

        if userCaptcha == session['captcha']:
            session['user_info'] = user_is_checked()

            # pobieramy id boardu i postu, ktory wczesniej napisalismy
            dest = session.get('last_post')
            if dest:
                return redirect(url_for('chan.board', id=dest[0], _anchor=f'post{dest[1]}'))
            else:
                return redirect(url_for('home'))

        else:

            return redirect(url_for('anty_spam'))

    return render_template('anty_spam.html', mycaptcha=mycaptcha)

