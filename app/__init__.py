from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=config.DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    from app import models
    from app.chan.views import blueprint_Chan
    app.register_blueprint(blueprint_Chan, url_prefix='/chan')

    return app

app = create_app()





