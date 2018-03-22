from flask import jsonify, request
from dao.parts import PartDAO

class PartHandler:

    def mapToDict(self,row):
        result = {}
        result['ppid'] = row[0]
        result['pname'] = row[1]
        result['pprice'] = row[2]
        result['pmaterial'] = row[3]
        return result

    def mapToSupDict(self,row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]


    def getAllParts(self):
        dao = PartDAO()
        result = dao.getAllParts()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Part=mapped_result)

    def getPartById(self, pid):
        dao = PartDAO()
        result = dao.getPartById(pid)
        if result == None:
            return jsonify(Error="NOT FOUND", 404)
        else:
            mapped = self.mapToDict(result)
            return jsonify(Part=mapped)

   # def getSuppliersByPartId(self,pid):

    def searchParts(self,args):
        color = args.get('pcolor') #assumes we only have one parameter
        result = PartDAO().searchByColor(color)
        if result == None:
            return jsonify(Error="NOT FOUND", 404)
        else:
            mapped = self.mapToDict(result)
            return jsonify(Part=mapped)

