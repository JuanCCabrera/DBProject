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
            for r in likes:
                result['like'] = r[0]
        if not dislikes:
            result['nolike'] = '0'
        else:
            for r in dislikes:
                result['nolike'] = r[0]
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
        result = dao.getAllMessages()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictWithLikesAndDislikes(r))
            return jsonify(Messages=mapped_result)
