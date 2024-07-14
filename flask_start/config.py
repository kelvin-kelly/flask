from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE_SQLALCHEMY_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'dbs/db.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app)

