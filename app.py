from flask import Flask

from config import config


"""
Update template hrefs to use url_for instead of relative pathing
Add a set of API endpoints
Remove LCO-specific text from the format
Properly format any message JSON
Implement message detail page
"""


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
    from routes.web import web_bp

    app.register_blueprint(web_bp)


app = create_app()
