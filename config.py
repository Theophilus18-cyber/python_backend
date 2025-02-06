import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import urllib.parse

load_dotenv()

db = SQLAlchemy()

class Config:
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_DATABASE = os.getenv('DB_DATABASE')

    if not all([DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER]):
        raise ValueError('The DB config is incomplete')

    # URL-encode the password
    DB_PASSWORD_ENCODED = urllib.parse.quote_plus(DB_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}/{DB_DATABASE}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def init_db(app):
    with app.app_context():
        db.create_all()