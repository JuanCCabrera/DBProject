from flask import Flask, jsonify, request
from handler.reactions import ReactionHandler
from handler.groupchats import GroupChatHandler
from handler.Users import UsersHandler
from handler.Message import MessageHandler
from handler.hashtags import HashtagHandler

app = Flask(__name__)

@app.route('/SikitrakeChat')
def home():
    return 'Welcome to SikitrakeChat!'

@app.route('/login')
def login():
    return "Login Not Currently Available"

@app.route('/SikitrakeChat/Reactions')
def reactions():
    handler = ReactionHandler()
    return handler.getAllReactions()

@app.route('/SikitrakeChat/Reactions/ID/<int:rid>')
def getReactionsById(rid):
    return ReactionHandler().getReactionsById(rid)

@app.route('/SikitrakeChat/Reactions/Likes')
def getAllLikes():
    return ReactionHandler().getAllLikes()

#Happy Hour 1
@app.route('/SikitrakeChat/Message/<int:mid>/Reactions/Likes')
def getLikesByMessageID(mid):
    return ReactionHandler().getLikesByMessageID()

#Happy Hour 1
@app.route('/SikitrakeChat/Message/<int:mid>/Reactions/DisLikes')
def getDisLikesByMessageID(mid):
    return ReactionHandler().getDisLikesByMessageID()

@app.route('/SikitrakeChat/Reactions/Dislikes')
def getAllDislikes():
    return ReactionHandler().getAllDislikes()

@app.route('/SikitrakeChat/Messages/<int:mid>/Reactions')
def getAllReactionsbyMessageID(mid):
    handler = ReactionHandler()
    return handler.getAllReactionsbyMessageID(mid)

@app.route('/SikitrakeChat/GroupChats')
def getAllGroupChats():
    return GroupChatHandler().getAllGroupChats()

@app.route('/SikitrakeChat/GroupChats/name/<string:name>')
def getGroupChatsByName(name):
    return GroupChatHandler().getGroupChatsByName(name)

@app.route('/SikitrakeChat/GroupChats/ID/<int:gid>')
def getGroupChatsById(gid):
    return GroupChatHandler().getGroupChatsById(gid)

@app.route('/SikitrakeChat/GroupChats/ID/<int:gid>/name')
def getGroupChatNameById(gid):
    return GroupChatHandler().getGroupChatNameById(gid)

@app.route('/SikitrakeChat/GroupChats/name/<string:name>/info')
def getGroupChatInfoByName(name):
    return GroupChatHandler().getGroupChatInfoByName(name)

@app.route('/SikitrakeChat/Users')
def getAllUsers():
    return UsersHandler().getAllUsers()

@app.route('/SikitrakeChat/Users/ID/<int:UID>')
def getUsersByUId(UID):
    handler = UsersHandler()
    return handler.getUsersByUId(UID)

@app.route('/SikitrakeChat/Users/phone/<string:phone>')
def getUsersByPhone(phone):
    handler = UsersHandler()
    return handler.getUsersByPhone(phone)

@app.route('/SikitrakeChat/Users/email/<string:email>')
def getUsersByEmail(email):
    handler = UsersHandler()
    return handler.getUsersByEmail(email)

@app.route('/SikitrakeChat/Users/contacts/<int:UID>')
def getContactsByUserID(UID):
    handler = UsersHandler()
    return handler.getContactsByUserID(UID)

@app.route('/SikitrakeChat/Messages')
def getAllMessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/SikitrakeChat/Messages/ID/<int:mid>')
def getMessageById(mid):
    return MessageHandler().getMessageById(mid)

@app.route('/SikitrakeChat/Messages/GroupChats/<int:cid>')
def getMessagesbyChatID(cid):
    handler = MessageHandler()
    return handler.getMessagesbyChatID(cid)

@app.route('/SikitrakeChat/Messages/GroupChats/<int:cid>/UserId/<int:uid>')
def getMessagesbyChatIDAndUser(cid, uid):
    handler = MessageHandler()
    return handler.getMessagesbyChatIDAndUser(cid, uid)

@app.route('/SikitrakeChat/Hashtags')
def getAllHashtags():
    handler = HashtagHandler()
    return handler.getAllHashtags()

@app.route('/SikitrakeChat/Hashtags/ID/<int:htid>')
def getHashtagsById(htid):
    handler = HashtagHandler()
    return handler.getHashtagsById(htid)

@app.route('/SikitrakeChat/Messages/ID/<int:mid>/Hashtags')
def getHashtagsByMessageId(mid):
    handler = HashtagHandler()
    return handler.getHashtagsByMessageId(mid)

#Happy Hour 1
@app.route('/SikitrakeChat/Hashtags/<string:hashtags>/Messages')
def getMessagesByHashtags(hashtags):
    handler = HashtagHandler()
    return handler.getMessagesByHashtags(hashtags)

if __name__=='__main__':
    app.run()
