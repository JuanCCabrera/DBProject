class HashtagDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [87, 'helloWorld']
        P2 = [91, None]
        P3 = [33, 'tru']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllHashtags(self):
        return self.data

    def getHashtagsById(self,htid):
        result = []
        for r in self.data:
            if htid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result
