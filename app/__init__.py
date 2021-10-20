from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize SQLAlchemy / register the database commands
    from app.models import db
    db.init_app(app)

    # Initialize routes / apply the blueprints to the app
    from app.routes import routes
    app.register_blueprint(routes)

    if test_config:
      app.config.update(test_config)

    return app
