from flask import Flask, request, jsonify, session 
from flask_sqlalchemy import SQLAlchemy 
#from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash 
import smtplib 
from email.message import EmailMessage 


def create_app():
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///communication_app.db' 
    app.config['SECRET_KEY'] = 'your-secret-key' 
    db = SQLAlchemy(app) 
    #login_manager = login_manager(app) 
    
    return app













