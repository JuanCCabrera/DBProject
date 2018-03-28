class MessageDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [56, 'Hola Mundo #helloWorld #Thefirst','01/01/2018',True, 97, 100]
        P2 = [59, 'estoy escribiendo de nuevo','01/01/2018',False, 97, 100]
        P3 = [57, 'No explota como Siquitrake','01/01/2018',False, 563, 101]
        P4 = [58, 'Jaaaajajajaja #tru #hard','01/02/2018',True, 787, 102]
        P5 = [60, 'esto es una prueba','01/01/2018',False, 97, 101]
        P6 = [61, 'estoy probando tambien', '01/01/2018', False, 97, 102]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)

    def getAllMessages(self):
        return self.data

    def getMessageById(self,mid):
        result = []
        for r in self.data:
            if mid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getMessagesbyChatID(self,cid):
        result = []
        for r in self.data:
            if cid == r[4] :
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getMessagesbyChatIDAndUser(self,cid, uid):
        result = []
        for r in self.data:
            if cid == r[4] :
                if uid == r[5]:
                    result.append(r)
        if not result:
            return None
        else:
            return result