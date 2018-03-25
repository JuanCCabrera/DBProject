from flask import Flask, request
from handler.groupchats import GroupChatHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def login():
    return "No Login  for you!!!"

@app.route('/GroupChat/chats')
def parts():
    if request.args:
        return GroupChatHandler().searchChats(request.args)
    else:
        handler = GroupChatHandler()
        return handler.getAllChats()

@app.route('/GroupChat/chats/<int:pid>')
def getChatById(pid):
    return GroupChatHandler().getNameByChatId(pid)

@app.route('/GroupChat/chats/<int:pid>/names')
def getNameByChatId(pid):
    return GroupChatHandler().getNameByChatId(pid)

if __name__ == '__main__':
    app.run()