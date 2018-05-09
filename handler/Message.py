from flask import jsonify, request
from dao.Message import MessageDAO


class MessageHandler:

    def mapToDict(self,row):
        result = {}
        result['MID'] = row[0]
        result['Message'] = row[1]
        result['MDate'] = row[2]
        result['MHashtag'] = row[3]
        return result

    def mapToDictWithLikesAndDislikes(self,row):
        dao = MessageDAO()
        likes = dao.getLikesperMessage(row[0])
        dislikes = dao.getDislikesperMessage(row[0])
        result = {}
        result['id'] = row[0]
        result['text'] = row[1]
        result['author'] = row[2]
        result['date'] = row[3]
        if not likes:
            result['like'] = 0
        else:
            result['like'] = likes[0][0]
        if not dislikes:
            result['nolike'] = 0
        else:
            result['nolike'] = dislikes[0][0]
        return result

    def insert_MessageinChatGroup_dict(Self, Message, MDate, MHashtag, UID, GID):
        result = {}
        result['Message'] = Message
        result['MDate'] = MDate
        result['MHashtag'] = MHashtag
        result['UID'] = UID
        result['GID'] = GID
        return result

    def messagebyhashtag_dict(self,row):
        result = {}
        result['MID'] = row[0]
        result['Message'] = row[1]
        result['MDate'] = row[2]
        result['UID'] = row[3]
        result['HTID'] = row[4]
        result['HText'] = row[5]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getMessageById(self,mid):
        dao = MessageDAO()
        result = dao.getMessageById(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getMessagesbyChatID(self, cid):
        dao = MessageDAO()
        result = dao.getMessagesbyChatID(cid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getMessagesbyChatIDAndUser(self, cid, uid):
        dao = MessageDAO()
        result = dao.getMessagesbyChatIDAndUser(cid, uid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getMessagesWithLikesAndDislikes(self):
        dao = MessageDAO()
        result = dao.getAllMessagesWithAuthor()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictWithLikesAndDislikes(r))
            return jsonify(Messages=mapped_result)

    # Phase III #
    def insertMessageinChatGroup(self, form):
        dao = MessageDAO()
        if len(form) != 4:
            return jsonify(Error="Malformed insert request"), 400
        else:
            Message = form['Message']
            print('Message : ', Message)
            MDate = form['MDate']
            print('MDate : ', MDate)
            MHashtag = False # tengo que hacer la rutina para verificar si tiene hashtag o no un mensaje
            print('MHashtag : ', MHashtag)
            UID = form['UID']
            print('UID : ', UID)
            GID = form['GID']
            print ('GID : ', GID )
            if Message and MDate and UID and GID :
                row = dao.insertMessageinChatGroup(Message, MDate, MHashtag, int(UID), int(GID))
                if row == None:
                    return jsonify(Error="Invalid Insert"), 404
                else:
                    self.contains_hashtags(Message, row)
                    result = self.insert_MessageinChatGroup_dict(Message, MDate, MHashtag, UID, GID)
                    return jsonify(User=result)
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def getMessagesWithLikesAndDislikesByChatGroup(self, form):
        GID = form['GID']
        dao = MessageDAO()
        result = dao.getMessagesWithLikesAndDislikesByChatGroup(GID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictWithLikesAndDislikes(r))
            return jsonify(Messages=mapped_result)

    def getAllMessagesByHashtag(self, form):
        HID = form['HID']
        dao = MessageDAO()
        result = dao.getAllMessagesByHashtag(HID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.messagebyhashtag_dict(r))
            return jsonify(Messages=mapped_result)

    def contains_hashtags(self, message, mid):
        message = 'Hola esto es una #prueba para probar que guardo los' \
                  'hashtags #real'
        string = message.split(' ')
        Hashtags = []
        for word in string:
            if word.startswith('#'):
                Hashtags.append(word)
        print ('Hashtags : ', Hashtags)