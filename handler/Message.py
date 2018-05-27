from flask import jsonify, request
from dao.Message import MessageDAO
from dao.hashtags import HashtagDAO
import datetime

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

    def insert_MessageinChatGroup_dict(Self, Message, MDate, MHashtag, UID, GID, MID):
        result = {}
        result['Message'] = Message
        result['MDate'] = MDate
        result['MHashtag'] = MHashtag
        result['UID'] = UID
        result['GID'] = GID
        result['MID'] = MID
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
        hdao = HashtagDAO()
        if len(form) != 3:
            return jsonify(Error="Malformed insert request"), 400
        else:
            Message = form['Message']
            #Para probar:
            #Message = "Esto es una prueba #funciona #thebest"
            Hashtags = self.contains_hashtags(Message)
            MDate = datetime.datetime.today().strftime('%d-%m-%Y')
            UID = form['UID']
            GID = form['GID']
            MHashtag = False
            if len(Hashtags) !=0:
                MHashtag = True
            if Message and MDate and UID and GID :
                Message = Message.replace('~', '#')
                row = dao.insertMessageinChatGroup(Message, MDate, MHashtag, int(UID), int(GID))
                if row == None:
                    return jsonify(Error="Invalid Insert"), 404
                else:
                    for htext in Hashtags:
                        hdao.insertHashtag(htext, row)
                    result = self.insert_MessageinChatGroup_dict(Message, MDate, MHashtag, UID, GID, row)
                    return jsonify(Message=result)
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

    def getAllMessagesByHashtaginGC(self, form):
        Htext = form['Htext'].replace('~', '#')
        GID = form['GID']
        dao = MessageDAO()
        result = dao.getAllMessagesByHashtaginGC(Htext, GID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.messagebyhashtag_dict(r))
            return jsonify(Messages=mapped_result)

    def contains_hashtags(self, message):
        m = message.replace('~', '#')
        print ('Mesage with # : ', m)
        string = m.split(' ')
        Hashtags = []
        for word in string:
            if word.startswith('#'):
                Hashtags.append(word)
        return Hashtags

    def insertReplyMessage(self, form):
        print('Estoy en el reply handler')
        dao = MessageDAO()
        Or_msg_ID = form['Or_msg_ID']
        print ('original message id: ' + Or_msg_ID)
        Or_msg = dao.getMessageById(Or_msg_ID)[0][1]
        print ('Original Message : ' + Or_msg)
        Message = form['Message'] + '\n' + 'Re:\' ' + Or_msg + ' \''
        print ('Message : ', Message)
        UID = form['UID']
        GID = form['GID']
        r_msg_id = self.insertReplyMessageinChatGroup(UID, GID, Message)
        dao.insertReplyMessage(Or_msg_ID, r_msg_id)
        result = dao.getMessageById(r_msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def insertReplyMessageinChatGroup(self, UID, GID, Message):
        dao = MessageDAO()
        hdao = HashtagDAO()
        if UID == None or GID == None or Message == None:
            return jsonify(Error="Malformed insert request"), 400
        else:
            Message = Message
            #Para probar:
            #Message = "Esto es una prueba #funciona #thebest"
            Hashtags = self.contains_hashtags(Message)
            MDate = datetime.datetime.today().strftime('%d-%m-%Y')
            UID = UID
            GID = GID
            MHashtag = False
            if len(Hashtags) !=0:
                MHashtag = True
            if Message and MDate and UID and GID :
                row = dao.insertMessageinChatGroup(Message, MDate, MHashtag, int(UID), int(GID))
                if row == None:
                    return jsonify(Error="Invalid Insert"), 404
                else:
                    for htext in Hashtags:
                        hdao.insertHashtag(htext, row)
                    return row
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400