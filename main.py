from flask import Flask, jsonify, request
from handler.Hashtags import HashtagsHandler
from handler.Users import UsersHandler
from handler.Message import MessageHandler

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

@app.route('/SikitraqueChat/Users')
def Users():
    handler = UsersHandler()
    return handler.getAllUsers()

@app.route('/SikitraqueChat/Users/<int:UID>')
def getUsersByUId(UID):
    handler = UsersHandler()
    return handler.getUsersByUId(UID)

@app.route('/SikitraqueChat/Message')
def Message():
    handler = MessageHandler()
    return handler.getAllMessage()

if __name__ == '__main__':
    app.run()