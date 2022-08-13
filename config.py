
class Config:
    ### BASE CONFIG ###
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    ### Development Config ###
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///baza_dev.sqlite'

