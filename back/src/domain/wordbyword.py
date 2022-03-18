import sqlite3

<<<<<<< HEAD
class Wordbyword:
    def __init__(self, text):
        self.text = text

    def to_dict(self):
        return {"text": self.text}

=======
<<<<<<<< HEAD:back/src/domain/wordbyword.py
class Wordbyword:
    def __init__(self, text):
       self.text = text
    
    def to_dict(self):
        return {
            'text': self.text,
========
class Activity:
    def __init__(self,id,text):
        self.id = id
        self.text = text

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text
>>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735:back/src/domain/activity.py
        }
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735

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
<<<<<<< HEAD
            create table if not exists wordbyword (
                "text" TEXT
=======
<<<<<<<< HEAD:back/src/domain/wordbyword.py
            create table if not exists wordbyword (
========
            create table if not exists activities (
                id varchar primary key,
>>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735:back/src/domain/activity.py
                text varchar
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_texts(self):
<<<<<<< HEAD
        sql = """select * from wordbyword"""
=======
        sql = """select * from activities"""
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

<<<<<<< HEAD
        return cursor.fetchall()

    def save(self, wordbyword):
        sql = """insert OR REPLACE into wordbyword (text) VALUES (:text)
         """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            wordbyword.to_dict(),
        )
        conn.commit()
=======
        return cursor.fetchall()
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
