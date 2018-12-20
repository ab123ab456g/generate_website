from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.config import Config
from app import routes, models, errors, logs

app.config.from_object(Config)