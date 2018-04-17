from config.dbconfig import pg_config
#import psycopg2
class UsersDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])
        # self.conn = psycopg2._connect(connection_url)

        #Fase1
        # P1 = [100, 'Coralis', 'Camacho', '7871234567', 'coralis.camacho1@upr.edu', 'Coraliscamacho1','872g73g92']
        # P2 = [101, 'Carlos', 'Rodriguez', '7872345678', 'carlos.rodriguez75@upr.edu', 'carlosrodriguez75','298h38gw']
        # P3 = [102, 'Juan', 'Cabrera', '7873456789', 'juan.cabrera2@upr.edu', 'juancabrera2', '982h489g']
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)
        #
        # P4 = [100,'Coraliscamacho1',101,'carlosrodriguez75']
        # P5 = [100,'Coraliscamacho1',102,'juancabrera2']
        # P6 = [101,'carlosrodriguez75',100,'Coraliscamacho1']
        # P7 = [101,'carlosrodriguez75',102,'juancabrera2']
        # P8 = [102,'juancabrera2',100,'Coraliscamacho1']
        # self.cdata = []
        # self.cdata.append(P4)
        # self.cdata.append(P5)
        # self.cdata.append(P6)
        # self.cdata.append(P7)
        # self.cdata.append(P8)
        #
        # P9 = [100, 'Coraliscamacho1', 787, 'DB Class']
        # P10 = [100, 'Coraliscamacho1', 563, 'TestChat']
        # P11 = [101, 'carlosrodriguez75', 97, 'SikitrakeChat']
        # P12 = [101, 'carlosrodriguez75', 563, 'TestChat']
        # P13 = [102, 'juancabrera2', 787, 'DB Class']
        # self.pdata = []
        # self.pdata.append(P9)
        # self.pdata.append(P10)
        # self.pdata.append(P11)
        # self.pdata.append(P12)
        # self.pdata.append(P13)


    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "Select * From Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        #return self.data

    def getUsersByUId(self,UID):
        cursor = self.conn.cursor()
        query = "Select * From Users Where UID = %s;"
        cursor.execute(query, (UID,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if UID == r[0]:
        #         return r
        # return None

    def getUsersByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "Select * From Users Where UPhone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for r in self.data:
        #     if phone == r[3]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getUsersByEmail(self,email):
        cursor = self.conn.cursor()
        query = "Select * From Users Where UEmail = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if email == r[4]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getContactsByUserID(self,UID):
        cursor = self.conn.cursor()
        query = "Select CL_Contact From Users natural inner join Contacts Where UID = %s;"
        cursor.execute(query, (UID,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.cdata:
        #     if UID == r[0]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getUsersInGroupChatByID(self, gid):
        cursor = self.conn.cursor()
        query = "Select UID, UDispName From Users natural inner join GroupChat Where GID = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.pdata:
        #     if gid == r[2]:
        #         temp = []
        #         temp.append(r[0])
        #         temp.append(r[1])
        #         result.append(temp)
        # if not result:
        #     return None
        # else:
        #     return result

    def getUsersInGroupChatByName(self, gname):
        cursor = self.conn.cursor()
        query = "Select UID, UDispName From Users natural inner join GroupChat Where GName = %s;"
        cursor.execute(query, (gname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.pdata:
        #     if gname == r[3]:
        #         temp = []
        #         temp.append(r[0])
        #         temp.append(r[1])
        #         result.append(temp)
        # if not result:
        #     return None
        # else:
        #     return result

    def getUserByUsername(self,uname):
        cursor = self.conn.cursor()
        query = "Select * From Users natural inner join GroupChat Where UName = %s;"
        cursor.execute(query, (uname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if uname == r[5]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result