from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'This is my first API call!'
