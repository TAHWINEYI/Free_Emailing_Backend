from flask import Flask, request, jsonify, session 
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from app import create_app
#from app.models import db

if __name__ == "__main__":
    # Create the Flask application
    app = create_app()
    #with app.app_context(): 
        # db.create_all() 
    # Run the Flask application
    app.run(debug=True, port=5500)

