import sqlite3

class Chainedword:
    def __init__(self, id, level, question, answer):
        self.id = id
        self.level = level
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'question': self.question,
            'answer': self.answer
        }

class ChainedwordRepository:
    def __init__ (self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists chainedword(
                "id" varchar PRIMARY KEY, 
                "level" varchar,
                "question" varchar,
                "answer" varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_phrases(self):
        sql = """select * from chainedword"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            chainedword = Chainedword(**item)
            result.append(chainedword)

        return result
    
    def save(self, countletters):
            sql = """insert into countletters (id, word, img, letters, syllables) 
                        values (:id, :word, :img, :letters, :syllables 
                        ) """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(
                sql, 
                countletters.to_dict()
                )
            conn.commit()
    
    def get_phrase_by_id(self, id):
        sql = """ SELECT * FROM countletters WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"id":id})

        data = cursor.fetchone()
        word = Chainedword(**data)
        return word

    def get_phrase_by_random(self):
        sql = """ SELECT * FROM chainedword ORDER BY RANDOM() LIMIT 1"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchmany(1)
        result = []
        for item in data:
            chainedword = Chainedword(**item)
            result.append(chainedword)

        return result