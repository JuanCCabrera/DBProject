from flask import Flask, jsonify, request
from handler.Hashtags import HashtagsHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the DB App!'

@app.route('/Login')
def LogIn():
    return 'No Login for you!!!'

@app.route('/SikitraqueChat/Hashtags')
def Hashtags():
    handler = HashtagsHandler()
    return handler.getAllHashtags()

if __name__ == '__main__':
    app.run()