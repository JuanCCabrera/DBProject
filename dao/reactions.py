class ReactionDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [122, 1, 57, 101]
        P2 = [74, 1, 59, 100]
        P3 = [849, 0, 58, 102]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllReactions(self):
        return self.data

    def getReactionsById(self,rid):
        result = []
        for r in self.data:
            if rid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getAllLikes(self):
        result = []
        for r in self.data:
            if 1 == r[1]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getAllDislikes(self):
        result = []
        for r in self.data:
            if 0 == r[1]:
                result.append(r)
        if not result:
            return None
        else:
            return result