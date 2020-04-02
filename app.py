from flask import Flask

from config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    from extensions import db

    db.init_app(app)

    with app.app_context():
        db.create_all()


def register_blueprints(app):
    from routes import routes_bp

    app.register_blueprint(routes_bp)


app = create_app()
