from functools import wraps
from datetime import datetime
from flask import session, redirect, url_for



def make_empty_user():
    user_info = {
        'is_checked': False,
        'count': 0,
        'date_log': None
    }

    return user_info

def user_is_checked():
    user_info = {
        'is_checked': True,
        'count': 3,
        'date_log': datetime.now()
    }

    return user_info


############################################
#### Dekorator do sprawdzania czy użytkownik przeszedł Podstawowy Test (Captcha na głównej stronie) #####

def is_checked(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if (session.get('user_info')['is_checked'] == True) and (session.get('user_info')['count'] > 0):
            return f(*args, **kwargs)
        elif (session.get('user_info')['is_checked'] == True) and (session.get('user_info')['count'] < 1):
            return redirect(url_for('anty_spam'))

        else:
            return redirect(url_for('main'))
    return decorated_func