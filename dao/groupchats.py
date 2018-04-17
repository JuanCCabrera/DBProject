
import datetime
from config.dbconfig import pg_config
#import psycopg2

class GroupChatDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])
        #self.conn = psycopg2._connect(connection_url)

        #Fase1
        # P1 = [787, 'DB Class', '03/22/18', 102]
        # P2 = [563, 'TestChat', '06/04/01', 100]
        # P3 = [97, 'SikitrakeChat', '02/21/17', 101]
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)

    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "Select * From GroupChat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        #return self.data

    def getGroupChatsByName(self,name):
        cursor = self.conn.cursor()
        query = "Select * From GroupChat Where GName = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if name == r[1]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getGroupChatsById(self,gid):
        cursor = self.conn.cursor()
        query = "Select * From GroupChat Where GID = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if gid == r[0]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getGroupChatNameById(self,gid):
        cursor = self.conn.cursor()
        query = "Select GName From GroupChat Where GID = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if gid == r[0]:
        #         result.append(r[1])
        # if not result:
        #     return None
        # else:
        #     return result

    def getGroupChatInfoByName(self,name):
        cursor = self.conn.cursor()
        query = "Select * From GroupChat Where GName = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for r in self.data:
        #     if name == r[1]:
        #         temp = []
        #         temp.append(r[0])
        #         temp.append(r[2])
        #         temp.append(r[3])
        #         result.append(temp)
        # if not result:
        #     return None
        # else:
        #     return result

    def getGroupChatByOwner(self,uid):
        cursor = self.conn.cursor()
        query = "Select * from GroupChat natural inner join Users Where UID = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result=[]
        # for r in self.data:
        #     if uid == r[3]:
        #         temp = []
        #         temp.append(r[0])
        #         temp.append(r[1])
        #         temp.append(r[2])
        #         result.append(temp)
        # if not result:
        #     return None
        # else:
        #     return result
