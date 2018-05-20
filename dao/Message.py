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

    def getAllMessagesWithAuthor(self):
        cursor = self.conn.cursor()
        query = "Select mid, message, udispname, mdate from Messages inner join Users using(uid);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Phase III
    def insertMessageinChatGroup(self, Message, MDate, MHashtag, UID, GID):
        cursor = self.conn.cursor()
        print ('Estoy en el insert')
        query = "insert into messages (message, mdate, mhashtag, uid, gid) " \
                "values (%s,%s,%s,%s,%s) " \
                "returning mid; "
        cursor.execute(query, (Message, MDate, MHashtag, int(UID), int(GID), ))
        result = cursor.fetchone()[0]
        self.conn.commit()
        print ('Result : ', result)
        return result

    def getMessagesWithLikesAndDislikesByChatGroup(self, GID):
        cursor = self.conn.cursor()
        query = "Select mid, message, udispname, mdate " \
                "from Messages inner join Users using(uid) " \
                "where gid = %s " \
                "order by mid desc; "
        cursor.execute(query, (GID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesByHashtag(self, HID):
        cursor = self.conn.cursor()
        query = "Select mid, message, mdate, uid, htid, htext " \
                "from messages natural inner join hashashtags natural inner join hashtags " \
                "where htid = %s;"
        cursor.execute(query, (HID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertReplyMessage(self, Or_msg_ID, r_msg_id):
        cursor = self.conn.cursor()
        print ('Estoy en el insert')
        query = "insert into isreply (or_msg_id, r_msg_id) " \
                "values (%s,%s); "
        cursor.execute(query, (Or_msg_ID, r_msg_id, ))
        self.conn.commit()
        return