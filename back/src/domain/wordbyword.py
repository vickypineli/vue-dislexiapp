import sqlite3

class Wordbyword:
    def __init__(self, language, text):
        self.language = language



        self.text = text

    def to_dict(self):
        return {
            'language': self.language,
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
                "language" varchar,
                "text" text
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_texts(self):
        sql = """select * from wordbyword"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            wordbyword = Wordbyword(**item)
            result.append(wordbyword)

        return result

    def save(self, wordbyword):
        sql = """insert into wordbyword (language, text) values (:language, :text
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            wordbyword.to_dict()
        )
        conn.commit()

    def get_text_by_language(self, language):
        sql = """ SELECT * FROM wordbyword WHERE language= :language"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"language":language})

        data = cursor.fetchone()
        textselected = Wordbyword(**data)
        return textselected
            
     