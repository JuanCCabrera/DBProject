class UsersDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [100, 'Coralis', 'Camacho', '7871234567', 'coralis.camacho1@upr.edu']
        P2 = [101, 'Carlos', 'Rodriguez', '7872345678', 'carlos.rodriguez75@upr.edu']
        P3 = [102, 'Juan', 'Cabrera', '7873456789', 'juan.cabrera2@upr.edu']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

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