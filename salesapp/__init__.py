from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.secret_key = "@^!$I!$@!H#*&HBHSAdfsas1434"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/labsaledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 4

db = SQLAlchemy(app=app)

