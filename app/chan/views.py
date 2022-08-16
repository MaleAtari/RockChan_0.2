from flask import Blueprint, render_template
from app.users.func import is_checked

blueprint_Chan = Blueprint('chan', __name__, template_folder='templates')

@blueprint_Chan.route('/')
@is_checked
def home():
    return render_template('chan/home.html')


