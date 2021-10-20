import pytest
from sqlalchemy_utils import database_exists, create_database, drop_database

import config as config
from app import create_app
from app.models import db

def create_testing_app():
    return create_app({
        'TESTING': True,
        'SQLALCHEMY_ECHO': False,
        'SQLALCHEMY_DATABASE_URI': config.SQLALCHEMY_DATABASE_URI
    })


def set_up_db():
  print("Dropping database...")
  if database_exists(config.SQLALCHEMY_DATABASE_URI):
    drop_database(config.SQLALCHEMY_DATABASE_URI)

  print("Creating database...")
  create_database(config.SQLALCHEMY_DATABASE_URI)

  app = create_testing_app()
  with app.app_context():
    db.init_app(app)
    db.create_all()


set_up_db()


@pytest.fixture
def app():
  return create_testing_app()


@pytest.fixture
def client(app):
    return app.test_client()
