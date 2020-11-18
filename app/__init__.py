from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# import config
app.config.from_object(Config)
# databases
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# login
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
