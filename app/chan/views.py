from flask import Blueprint, render_template

blueprint_Chan = Blueprint('chan', __name__, template_folder='templates')

@blueprint_Chan.route('/')
def home():
    return render_template('chan/home.html')


