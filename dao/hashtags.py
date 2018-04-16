from config.dbconfig import pg_config
#import psycopg2

class HashtagDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

       # self.conn = psycopg2._connect(connection_url)
    
        ##Primera Parte##
        # P1 = [87, 'helloWorld', 56]
        # P2 = [88, 'Thefirst', 56]
        # P3 = [91, None, 57]
        # P4 = [33, 'tru', 58]
        # P5 = [34, 'hard', 58]
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)
        # self.data.append(P4)
        # self.data.append(P5)

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags;" #verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        #return self.data

    def getHashtagsById(self,htid):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags Where HTID = %s;" #verificar si corre bien
        cursor.execute(query, (htid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        # result = []
        # for r in self.data:
        #     if htid == r[0]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getHashtagsByMessageId(self,mid):
        cursor = self.conn.cursor()
        query = "Select * From Hashtags Where MID = %s;" #verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        ##Primera Parte##
        # result = []
        # for r in self.data:
        #     if mid == r[2]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result