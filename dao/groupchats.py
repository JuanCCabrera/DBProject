import datetime

class GroupChatDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [787, 'DB Class', '03/22/18', 102]
        P2 = [563, 'TestChat', '06/04/01', 100]
        P3 = [97, 'SikitrakeChat', '02/21/17', 101]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllGroupChats(self):
        return self.data

    def getGroupChatsByName(self,name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getGroupChatsById(self,gid):
        result = []
        for r in self.data:
            if gid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getGroupChatNameById(self,gid):
        result = []
        for r in self.data:
            if gid == r[0]:
                result.append(r[1])
        if not result:
            return None
        else:
            return result

    def getGroupChatInfoByName(self,name):
        result = []
        for r in self.data:
            if name == r[1]:
                temp = []
                temp.append(r[0])
                temp.append(r[2])
                temp.append(r[3])
                result.append(temp)
        if not result:
            return None
        else:
            return result

    def getGroupChatByOwner(self,uid):
        result=[]
        for r in self.data:
            if uid == r[3]:
                temp = []
                temp.append(r[0])
                temp.append(r[1])
                temp.append(r[2])
                result.append(temp)
        if not result:
            return None
        else:
            return result