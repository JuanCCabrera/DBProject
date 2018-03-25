class ChatDAO:
    def __init__(self):
        P1 = [122, 'OS']
        P2 = [74, 'DB']
        P3 = [849, 'JAVA']
        P4 = [757, 'SW']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllChats(self):
        P1 = [122, 'OS']
        P2 = [74, 'DB']
        P3 = [849, 'JAVA']
        P4 = [757, 'SW']
        result = []
        result.append(P1)
        result.append(P2)
        result.append(P3)
        return self.data

    def getChatById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getNameByChatId(self, id):
        if id == 122:
            return [[122, 'OS']]
        elif id == 74:
            T = []
            T.append([74, 'DB'])
            return T
        elif id == 849:
            T = []
            T.append(['849', 'DB'])
            T.append(['849', 'Calculus'])
            T.append(['849', 'Circuits X'])
            T.append(['849', 'ININ'])
            return T
        elif id == 757:
            T = []
            T.append([757, 'SW'])
            T.append(['757', 'Circuits'])
            T.append(['757', 'Circuits II'])
            T.append(['757', 'Circuits II'])
            return T
        else:
            return[]


    def searchByName(self, name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)
        return result
