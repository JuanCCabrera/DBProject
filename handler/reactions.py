
from flask import jsonify, request
from dao.reactions import ReactionDAO

class ReactionHandler:
    def mapToDict(self, row):
        result = {}
        result['RID'] = row[0]
        result['MReaction'] = row[1]
        result['MID'] = row[2]
        result['ROwner'] = row[3]
        return result

    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getReactionsById(self,rid):
        dao = ReactionDAO()
        result = dao.getReactionsById(rid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllLikes(self):
        dao = ReactionDAO()
        result = dao.getAllLikes()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllDislikes(self):
        dao = ReactionDAO()
        result = dao.getAllDislikes()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)

    def getAllReactionsbyMessageID(self,mid):
        dao = ReactionDAO()
        result = dao.getAllReactionsbyMessageID(mid)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reactions=mapped_result)