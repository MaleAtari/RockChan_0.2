from flask import Blueprint, render_template, redirect, url_for, session
from app.users.func import is_checked
from app.models import db, Board, Posts
from app.chan.forms import PostForm

blueprint_Chan = Blueprint('chan', __name__, template_folder='templates')

@blueprint_Chan.route('/')
@is_checked
def home():
    boards = Board.query.all()
    return render_template('chan/home.html', boards=boards)

@blueprint_Chan.route('/board/<id>', methods=['POST', 'GET'])
@is_checked
def board(id):

    board = Board.query.get(id)
    form = PostForm()

    if form.validate_on_submit():
        new_post = Posts(auth=form.name.data,
                         content=form.text.data,
                         board_id=board.id,
                         user_id=None)
        db.session.add(new_post)
        db.session.commit()
        points = int(session['user_info']['count']) - 1
        session['user_info']['count'] = points
        session.modified = True

        return redirect(url_for('chan.board', id=board.id, _anchor=f'post{new_post.id}'))

    return render_template('chan/posts.html', board=board, form=form)


