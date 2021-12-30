import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .commands import reset_items

def create_app():
  app = Flask(__name__)

  uri = os.getenv('DATABASE_URL')
  if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)

  app.config['SQLALCHEMY_DATABASE_URI'] = uri
  
  db.init_app(app)

  from .views import api
  app.register_blueprint(api)

  app.cli.add_command(reset_items)

  return app
