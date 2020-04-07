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
    from models import Message, Topic  # All models must be imported here for flask-migrate to pick up migrations

    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from routes.api.v1 import api_bp as api_v1
    from routes.api.v2 import api_bp as api_v2
    from routes.web import web_bp

    app.register_blueprint(api_v1, url_prefix='/api')
    app.register_blueprint(api_v2, url_prefix='/api')
    app.register_blueprint(web_bp, url_prefix='')


app = create_app()
