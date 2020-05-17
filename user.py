import sqlite3

class User:
    def __init__(self,_id, username, password):
        self.id = _id
        self.username = username
        self.password = password
@classmethod
def find_by_usename(cls, usename):
    connection = sqlite3.connect(data.db)
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE usename=?"
    result = cursor.execute(query, (username))
    row =result.fetchone()
    if row:

        user = cls(*row)
    else:
        user = None

    connection.close()
    return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor =connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchcone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
        
