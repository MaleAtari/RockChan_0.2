from app import db
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()





# # # BAZA DANYCH # # #

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    role = db.Column(db.Integer)
    date_add = db.Column(db.DateTime, default=datetime.now)
    date_log = db.Column(db.DateTime, default=datetime.now)
    points = db.Column(db.Integer, default=0)
    posts = db.relationship('Posts', backref='user')


    def __init__(self, name, password, role=5):
        self.name = name
        self.password = bcrypt.generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def show_date_add(self):
        return self.date_add.strftime("%D  %H:%M:%S")

    def show_date_log(self):
        return self.date_log.strftime("%D  %H:%M:%S")



class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    info = db.Column(db.Text)
    date_add = db.Column(db.DateTime, default=datetime.now)
    open = db.Column(db.Boolean, default=True)
    posts = db.relationship('Posts', backref='board')



    def show_date_add(self):
        return self.date_add.strftime("%D  %H:%M")

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    auth = db.Column(db.String(128))
    content = db.Column(db.Text)
    date_add = db.Column(db.DateTime, default=datetime.now)
    date_edit = db.Column(db.DateTime)
    board_id = db.Column(db.ForeignKey(Board.id))
    user_id = db.Column(db.ForeignKey(Users.id))
