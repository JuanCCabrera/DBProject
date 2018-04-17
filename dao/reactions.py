#from config.dbconfig import pf_config
#import psycopg2

class ReactionDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_irl = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])
        #self.conn = psycopg2._connect(connection_url)

        #Fase1
        # P1 = [122, 1, 57, 101]
        # P2 = [74, 1, 57, 100]
        # P3 = [849, 0, 58, 102]
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

        #Fase1
        #return self.data

    def getReactionsById(self,rid):
        cursor = self.conn.cursor()
        query = "Select * From Messages Where RID = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if rid == r[0]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getAllLikes(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions Where MReaction = True;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        #Fase1
        # result = []
        # for r in self.data:
        #     if 1 == r[1]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getAllDislikes(self):
        cursor = self.conn.cursor()
        query = "Select * From Reactions Where MReaction = False;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        # Fase 1
        #result = []
        # for r in self.data:
        #     if 0 == r[1]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    def getAllReactionsbyMessageID(self,mid):
        cursor = self.conn.cursor()
        query = "Select * From Reactions natural inner join Message Where MID = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for r in self.data:
        #     if mid == r[2]:
        #         result.append(r)
        # if not result:
        #     return None
        # else:
        #     return result

    # def insert(self, RID, MReaction, MID, ROwner):
    #     cursor = self.conn.cursor()
    #     query = "insert into Reactions(RID, MReaction, MID, Rowner) values (%s, &s, %s, %s) returning RID;"
    #     cursor.execute(query, (RID, MReaction, MID, ROwner,))
    #     RID = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return RID
    #
    # def delete(self, rid):
    #     cursor = self.conn.cursor()
    #     query = "delete from reactions where rid = %s;"
    #     cursor.execute(query, (rid))
    #     self.conn.commit()
    #     return rid
    #
    # def update(self,RID, MReaction, MID, ROwner):
    #     cursor = self.conn.cursor()
    #     query = "update reactions set RID = %s, MReaction = %s, MID = %s, ROwner = %s;"
    #     cursor.execute(query, (RID, MReaction, MID, ROwner,))
    #     self.conn.commit()
    #     return RID