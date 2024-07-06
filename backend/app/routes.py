from email.message import EmailMessage
import smtplib
from flask import app, jsonify, request, redirect, url_for, render_template
from flask_login import LoginManager, current_user, login_user, logout_user
from app.db import register_user
from app.models import Email, Error, User
from flask import Blueprint
from app.db import db

@LoginManager.user_loader 
def load_user(user_id): 
    return User.query.get(int(user_id)) 

@app.route('/login', methods=['POST']) 
def login(): 
    data = request.get_json() 
    user = User.query.filter_by(username=data['username']).first() 
    if user and user.check_password(data['password']): 
        login_user(user) 
        return jsonify({'message': 'Login successful'}), 200 
    else: 
        return jsonify({'message': 'Invalid username or password'}), 401                                                                                                                                  

@app.route('/register', methods=['POST']) 
def register(): 
    data = request.get_json() 
    user = User(username=data['username']) 
    user.set_password(data['password']) 
    db.session.add(user) 
    db.session.commit() 
    return jsonify({'message': 'User registered successfully'}), 201 
                                                                                                                                  
@app.route('/search', methods=['GET'])
def search_emails():
     query = request.args.get('query')
     search = "%{}%".format(query)
     emails = Email.query.filter(Email.subject.like(search)).all()
     return render_template('search_results.html', emails=emails)
                                                                                                                                                                                                                                                                 
@app.route('/outbox', methods=['GET'])
def show_outbox():
     # Sorting by timestamp in descending order so the newest emails come first
     emails = Email.query.order_by(Email.timestamp.desc()).all()
     return render_template('inbox.html', emails=emails)

@app.route('/logout', methods=['POST']) 
def logout(): 
    logout_user() 
    return jsonify({'message': 'Logout successful'}), 200 
 
@app.route('/inbox', methods=['GET']) 
def inbox(): 
    emails = current_user.emails.order_by(Email.timestamp.desc()).all() 
    return jsonify([email.to_dict() for email in emails]) 
 
@app.route('/compose', methods=['POST']) 
def compose(): 
    data = request.get_json() 
    email = Email( 
        subject=data['subject'], 
        body=data['body'], 
        sender=current_user.username, 
        recipient=data['recipient'], 
        timestamp=db.func.current_timestamp(), 
        user_id=current_user.id 
    ) 
    db.session.add(email) 
    db.session.commit() 
 
    msg = EmailMessage() 
    msg['Subject'] = email.subject 
    msg['From'] = email.sender 
    msg['To'] = email.recipient 
    msg.set_content(email.body) 
 
    with smtplib.SMTP('localhost', 25) as smtp: 
        smtp.send_message(msg) 
 
    return jsonify({'message': 'Email sent successfully'}), 200 