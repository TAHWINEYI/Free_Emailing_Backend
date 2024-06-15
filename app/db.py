from werkzeug.security import generate_password_hash
from app.models import User, Email, Error
from app.models import Email, User, db
from flask_login import UserMixin, login_user, logout_user, current_user 
from werkzeug.security import check_password_hash
                                                                                                                                  
def register_user(username, email, password):
     password_hash = generate_password_hash(password)
     new_user = User(username=username, email=email, password_hash=password_hash)
     db.session.add(new_user)
     db.session.commit()
                                                                                                                                  
def authenticate_user(email, password):
     user = User.query.filter_by(email=email).first()
     if user and check_password_hash(user.password_hash, password):
         return user
     return None
                                                                                                                                                     
def create_email(sender_id, recipient_id, subject, body):
     new_email = Email(sender_id=sender_id, recipient_id=recipient_id, subject=subject, body=body)
     db.session.add(new_email)
     db.session.commit()    
     
def get_inbox(user_id):
     emails = Email.query.filter_by(recipient_id=user_id).order_by(Email.timestamp.desc()).all()
     return emails
                                                                                                                                  
def get_outbox(user_id):
     emails = Email.query.filter_by(sender_id=user_id).order_by(Email.timestamp.desc()).all()
     return emails


