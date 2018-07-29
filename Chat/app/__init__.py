# coding : utf8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import  pymysql
pymysql.install_as_MySQLdb()


import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/chat?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'chat'
app.debug = True
db = SQLAlchemy(app)
socketio = SocketIO(app)
async_mode = "eventlet"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404