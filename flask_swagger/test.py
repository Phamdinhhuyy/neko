from urllib import response
from flask import request
from dotenv import load_dotenv, find_dotenv
import os
"""
BASE = 'http://127.0.0.1:5000'

data = {
    "username": 'neko3',
    'password': "789",
    'email': 'neko3@gmail.com'
}

#response = requests.post(BASE + "/register", json=data)
#response = requests.get(BASE + "/login", json={'username': 'neko', 'password': '123'})
#response = requests.get(BASE +"/verifyemail", json={'email': 'neko1@gmail.com'})
response = requests.get(BASE + '/login/product/quantity')
print(response)
"""

load_dotenv(find_dotenv())
password = os.environ.get("DBPASS")
print(password)

if os.environ.get("FLASK_ENV") == "test":
    print(".....test mode.....")