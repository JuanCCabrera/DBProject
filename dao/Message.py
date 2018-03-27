class MessageDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [56, 'Hola Mundo #helloWorld','01/01/2018',True]
        P2 = [57, 'No explota como Siquitrake','01/01/2018',False]
        P3 = [58, 'Jaaaajajajaja #tru','01/02/2018',True]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

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
