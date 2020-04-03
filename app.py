from flask import Flask

from config import config


def create_app():
    """
    The structure of this Flask app was taken from this wonderful blog post by Tracy Chou:
    https://tracy.dev/how-to-mitigate-import-hell-in-flask/
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    from extensions import db, migrate
    from models import Message, Topic

    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from routes import routes_bp

    app.register_blueprint(routes_bp)


app = create_app()
