from config.dbconfig import pg_config
import psycopg2

class MessageDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "Select * From Messages;" #verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self,mid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where MID = %s" #verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesbyChatID(self,cid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where GID = %s;" #falta hacer el query
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesbyChatIDAndUser(self,cid, uid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where GID = %s and UID = %s;" #verificar si corre bien
        cursor.execute(query, (cid,uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesperMessage(self,mid):
        cursor = self.conn.cursor()
        query = "select count(*), m.mid " \
                "from messages as m, reactions as r " \
                "where m.mid = r.mid and mreaction = true and m.mid = %s " \
                "group by m.mid; "
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesperMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*), m.mid " \
                "from messages as m, reactions as r " \
                "where m.mid = r.mid and mreaction = false and m.mid = %s " \
                "group by m.mid; "
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result