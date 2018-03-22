from flask import jsonify, request
from dao.Hashtags import HashtagsDAO

class HashtagsHandler:

    def mapToDict(self,row):
        result = {}
        result['HTID'] = row[0]
        result['Hashtag'] = row[1]
        return result


    def getAllHashtags(self):
        dao = HashtagsDAO()
        result = dao.getAllHashtags()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Part=mapped_result)