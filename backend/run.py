from fastapi import requests
from flask import Flask, request, jsonify, session 
from flask_sqlalchemy import SQLAlchemy  
from app import create_app
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

api_key ='46e20ed31f31fd1f57dc8970d9941688d4e85e4050dd63b5c697b7c5cd3a48cb'
project_id = 4507554898116688
organization_slug = 'lee-4g'
sentry_sdk.init(
    dsn="https://291ed29b6f36daef24ef7102c281d6d8@o4507554888613888.ingest.de.sentry.io/4507554898116688",
    traces_sample_rate=1.0,
    debug=True,
    integrations=[FlaskIntegration()],
)

def receive_error_data():
    url = f"https://sentry.io/api/0/projects/{organization_slug}/{project_id}/issues/"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    error_data  = requests.get(url, headers=headers)
    print(error_data.content)
    return  error_data.json()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5500)

