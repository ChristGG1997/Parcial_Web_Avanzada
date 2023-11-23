from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# ---------------------------------------------------------------------------- #
#                                   CONFIG DB                                  #
# ---------------------------------------------------------------------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://christgg1997:F74df747f@christgg1997.mysql.pythonanywhere-services.com/christgg1997$shoe_stores'
app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = False

app.secret_key = "WebAvanzada"

db = SQLAlchemy(app)
ma = Marshmallow(app)