from config.dbconfig import pg_config
import psycopg2

class GroupChatDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "Select * from groupchats;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsByName(self,name):
        cursor = self.conn.cursor()
        query = "Select * from groupchats where gname = %s;"  # verificar si corre bien
        cursor.execute(query,(name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsById(self,gid):
        cursor = self.conn.cursor()
        query = "Select * from groupchats where gid = %s;"  # verificar si corre bien
        cursor.execute(query,(gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatNameById(self,gid):
        cursor = self.conn.cursor()
        query = "Select gname from groupchats where gid = %s;"  # verificar si corre bien
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatInfoByName(self,name):
        cursor = self.conn.cursor()
        query = "Select gid, gcdate, uid From groupchats where gname = %s;"  # verificar si corre bien
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatByOwner(self,uid):
        cursor = self.conn.cursor()
        query = "Select gid, gname, gcdate From groupchats where uid = %s;"  # verificar si corre bien
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


