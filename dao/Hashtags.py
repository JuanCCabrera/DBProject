class HashtagsDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [122, 'Bolt']
        P2 = [74, 'Wire']
        P3 = [849, 'Wood']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllHashtags(self):
        return self.data