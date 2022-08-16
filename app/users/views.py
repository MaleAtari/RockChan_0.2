from flask import Blueprint, render_template

blueprint_Users = Blueprint('users', __name__, template_folder='templates')

@blueprint_Users.route('/')
def home():
    return render_template('users/home.html')


