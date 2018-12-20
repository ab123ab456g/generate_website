from flask import Flask

app = Flask(__name__)

from app.config import Config
from app import routes, models, errors, logs

app.config.from_object(Config)