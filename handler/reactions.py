
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

    def build_reaction_attributes(self, RID, MReaction, MID, ROwner):
        result = {}
        result['RID'] = RID
        result['MReaction'] = MReaction
        result['MID'] = MID
        result['ROwner'] = ROwner
        return result

    def deleteReaction(self, rid):
        dao = ReactionDAO()
        if not dao.getReactionsById(rid):
            return jsonify(Error = "Reaction not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def insertReaction(self,form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            RID = form['RID']
            MReaction = form['MReaction']
            MID = form['MID']
            ROwner = form['ROwner']
            if RID and MReaction and MID and ROwner:
                dao = ReactionDAO()
                dao.insert(RID, MReaction, MID, ROwner)
                result = self.build_reaction_attributes(RID, MReaction, MID, ROwner)
                return jsonify(Reaction=result),201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateReaction(self,rid,form):
        dao = ReactionDAO()
        if not dao.getReactionsById(rid):
            return jsonify(Error="Malformed update request"), 400
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"),400
            else:
                RID = form['RID']
                MReaction = form['MReaction']
                MID = form['MID']
                ROwner = form['ROwner']
                if RID and MReaction and MID and ROwner:
                    dao.update(RID,MReaction,MID,ROwner)
                    result = self.build_reaction_attributes(RID,MReaction,MID,ROwner)
                    return jsonify(Reaction=result),200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
