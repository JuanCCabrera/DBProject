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


    def getAllMessage(self):
        dao = MessageDAO()
        result = dao.getAllMessage()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Part=mapped_result)