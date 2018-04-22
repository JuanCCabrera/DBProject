class UsersDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['password'])

        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "Select * From Users;"  # verificar si corre bien
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByUId(self,UID):
        cursor = self.conn.cursor()
        query = "Select * From Users where uid = %s;"  # verificar si corre bien
        cursor.execute(query,(UID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "Select * From Users where uphone = %s;"  # verificar si corre bien
        cursor.execute(query,(phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByEmail(self,email):
        cursor = self.conn.cursor()
        query = "Select * From Users where uemail = %s;"  # verificar si corre bien
        cursor.execute(query,(email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactsByUserID(self,UID):
        cursor = self.conn.cursor()
        query = "Select U1.uid, U1.udispname, U2.uid, U2.udispname From (Users as U1 natural inner join Contacts as C) inner join Users as U2 on U2.uid = C.cuid where uid = %s;"  # verificar si corre bien
        cursor.execute(query,(UID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersInGroupChatByID(self, gid):
        cursor = self.conn.cursor()
        query = "Select uid, udispname From Users natural inner join Participates where gid = %s;"  # verificar si corre bien
        cursor.execute(query,(gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersInGroupChatByName(self, gname):
        cursor = self.conn.cursor()
        query = "Select uid, udispname From (Users natural inner join Participates) natural inner join Groupchats where gname = %s;"  # verificar si corre bien
        cursor.execute(query,(gname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self,uname):
        cursor = self.conn.cursor()
        query = "Select * From Users where udispname = %s;"  # verificar si corre bien
        cursor.execute(query,(uname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersThatLikedMessage(self,mid):
        cursor = self.conn.cursor()
        query = "Select uid, udispname, upassword, ufirst_name, ulast_name, uphone, uemail From Users natural inner join Reactions where mid = %s AND mreaction = TRUE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersThatDislikedMessage(self,mid):
        cursor = self.conn.cursor()
        query = "Select uid, udispname, upassword, ufirst_name, ulast_name, uphone, uemail From Users natural inner join Reactions where mid = %s AND mreaction = FALSE;"  # verificar si corre bien
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result