from sqlite3 import *

class database:
    def __init__(self,db):
        self.con = connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''create table if not exists info_bot 
        (id integer primary key,token text,create_at text,
        status text,owner_id integer)''')
        self.cur.execute('create table if not exists text_bot (id integer primary key,name text,text text)')
        self.con.commit()

    def inser_infobot(self,token,create_at,stutus,owner_id):
        self.cur.execute('INSERT INTO info_bot  VALUES (null,?,?,?,?)',(token,create_at,stutus,owner_id))
        self.con.commit()

    def read_admin(self):
        self.cur.execute('select owner_id from info_bot')
        result = self.cur.fetchone()
        return list(result)

    def read_token(self):
        self.cur.execute('select token from info_bot where id = 1')
        result = self.cur.fetchone()
        if result is None:
            return None
        else:
            return result[0]

    def read_text(self,name):
        self.cur.execute('select text from text_bot where name = ?',(name,))
        result = self.cur.fetchone()
        return result[0]
        
         
db = database('database.db')