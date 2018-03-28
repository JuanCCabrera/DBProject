from flask import jsonify, request
from dao.groupchats import GroupChatDAO

class GroupChatHandler:
    def mapToDict(self, row):
        result = {}
        result['GID'] = row[0]
        result['GName'] = row[1]
        result['GCDate'] = row[2]
        return result

    def mapToDictIdtoName(self,row):
        result = {}
        result['GName'] = row
        return result

    def mapToDictInfoByName(self,row):
        result = {}
        result['GID'] = row[0]
        result['GCDATE'] = row[1]
        return result

    def getAllGroupChats(self):
        dao = GroupChatDAO()
        result = dao.getAllGroupChats()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatsByName(self,name):
        dao = GroupChatDAO()
        result = dao.getGroupChatsByName(name)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(
                    self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatsById(self,gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatsById(gid)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatNameById(self,gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatNameById(gid)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            mapped_result.append(self.mapToDictIdtoName(result))
            return jsonify(GroupChats=mapped_result)

    def getGroupChatInfoByName(self,name):
        dao = GroupChatDAO()
        result = dao.getGroupChatInfoByName(name)
        if(result == None):
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictInfoByName(r))
            return jsonify(GroupChats=mapped_result)