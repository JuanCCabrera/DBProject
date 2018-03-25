class MessageDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [56, 'Hola Mundo','January/01/2018',True]
        P2 = [57, 'No explota como Siquitrake','January/01/2018',False]
        P3 = [58, 'Jaaaajajajaja','January/02/2018',True]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllMessage(self):
        return self.data