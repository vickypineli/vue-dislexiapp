import sqlite3

class Wordbyword:
    def__init__(self, text):
       self.text = text
    
    def to_dict(self):
        return {
            'text': self.text
        }
class WordbywordRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists activities (
                text varchar
            )
            
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_texts(self):
        sql = """select * from activities"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor.fetchall()