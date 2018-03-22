class PartDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [122, 'Bolt', 0.5, 'blue']
        P2 = [74, 'Wire', 1.5, 'silver']
        P3 = [849, 'Wood', 5.00, 'brown']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)


    def getAllParts(self):
        #P1 = [122, 'Bolt', 0.5, 'blue']
        #P2 = [74, 'Wire', 1.50, 'silver']
        #P3 = [849, 'Wood', 5.00, 'brown']
        #result = []
        #result.append(P1)
        #result.append(P2)
        #result.append(P3)
        return self.data

    def getPartById(self,pid):
        result = []
        for r in self.data:
            if pid == r[0]:
                result.append(self.data[0])

    def searchPartsByColor(self,color):





