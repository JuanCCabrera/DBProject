class UsersDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [100, 'Coralis', 'Camacho', '7871234567', 'coralis.camacho1@upr.edu', 'Coraliscamacho1','872g73g92']
        P2 = [101, 'Carlos', 'Rodriguez', '7872345678', 'carlos.rodriguez75@upr.edu', 'carlosrodriguez75','298h38gw']
        P3 = [102, 'Juan', 'Cabrera', '7873456789', 'juan.cabrera2@upr.edu', 'juancabrera2', '982h489g']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

        P4 = [100,'Coraliscamacho1',101,'carlosrodriguez75']
        P5 = [100,'Coraliscamacho1',102,'juancabrera2']
        P6 = [101,'carlosrodriguez75',100,'Coraliscamacho1']
        P7 = [101,'carlosrodriguez75',102,'juancabrera2']
        P8 = [102,'juancabrera2',100,'Coraliscamacho1']
        self.cdata = []
        self.cdata.append(P4)
        self.cdata.append(P5)
        self.cdata.append(P6)
        self.cdata.append(P7)
        self.cdata.append(P8)


    def getAllUsers(self):
        return self.data

    def getUsersByUId(self,UID):
        result = []
        for r in self.data:
            if UID == r[0]:
                return r
        return None

    def getUsersByPhone(self,phone):
        result = []
        for r in self.data:
            if phone == r[3]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getUsersByEmail(self,email):
        result = []
        for r in self.data:
            if email == r[4]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getContactsByUserID(self,UID):
        result = []
        for r in self.cdata:
            if UID == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result