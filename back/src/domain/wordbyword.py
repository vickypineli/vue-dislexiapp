import sqlite3

class Wordbyword:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text
        }

class WordbywordRepository:
    def __init__ (self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists wordbyword (
                "id" varchar,
                "text" text
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_texts(self):
        sql = """select * from wordbyword"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    def save(self, wordbyword):
        sql = """insert into wordbyword (id, text) values (:id, :text
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            wordbyword.to_dict()
        )
        conn.commit()

