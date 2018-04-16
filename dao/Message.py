from config.dbconfig import pg_config
#import psycopg2

class MessageDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        ##Verificar que conincida con el que es##
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        #self.conn = psycopg2._connect(connection_url)

        ##Primera Parte##
        # P1 = [56, 'Hola Mundo #helloWorld #Thefirst','01/01/2018',True, 97, 100]
        # P2 = [59, 'estoy escribiendo de nuevo','01/01/2018',False, 97, 100]
        # P3 = [57, 'No explota como Siquitrake','01/01/2018',False, 563, 101]
        # P4 = [58, 'Jaaaajajajaja #tru #hard','01/02/2018',True, 787, 102]
        # P5 = [60, 'esto es una prueba','01/01/2018',False, 97, 101]
        # P6 = [61, 'estoy probando tambien', '01/01/2018', False, 97, 102]
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)
        # self.data.append(P4)
        # self.data.append(P5)
        # self.data.append(P6)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "Select * From Messages;" #verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        #return self.data

    def getMessageById(self,mid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where MID = %s" #verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        # result = []
        # for r in self.data:
        #     if mid == r[0]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getMessagesbyChatID(self,cid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where GID = %s;" #falta hacer el query
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        # result = []
        # for r in self.data:
        #     if cid == r[4] :
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getMessagesbyChatIDAndUser(self,cid, uid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where GID = %s and UID = %s;" #verificar si corre bien
        cursor.execute(query, (cid,uid))
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        # result = []
        # for r in self.data:
        #     if cid == r[4] :
        #         if uid == r[5]:
        #             result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result