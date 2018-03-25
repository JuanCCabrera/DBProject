from flask import jsonify, request
from dao.groupchat import ChatDAO
class GroupChatHandler:

    def mapToDict(self, row):
        result = {}
        result['GID'] = row[0]
        result['GNAME'] = row[1]
        return result
    def mapToSupDict(self, row):
        result = {}
        result['GID'] = row[0]
        result['GNAME'] = row[1]
        return result

    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(GroupChat=mapped_result)

    def getChatById(self, id):
        dao = ChatDAO()
        result = dao.getChatById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(GroupChat=mapped)


    def getNameByChatId(self, id):
        dao = ChatDAO()
        result = dao.getNameByChatId(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Name=mapped_result)

    def searchName(self, args):
        name = args.get('name')
        dao = ChatDAO()
        result = dao.searchByName(name)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(GroupChat=mapped_result)


