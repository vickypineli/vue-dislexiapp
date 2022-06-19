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
    
    def save(self, chainedword):
            sql = """insert into chainedword (id, level, question, answer) 
                        values (:id, :level, :question, :answer 
                        ) """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(
                sql, 
                chainedword.to_dict()
                )
            conn.commit()
    
    def get_phrases_list_by_level(self, level):
        sql = """ SELECT * FROM chainedword WHERE level = :level"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"level":level})

        data = cursor.fetchall()
        result = []
        for item in data:
            chainedword = Chainedword(**item)
            result.append(chainedword)

        return result

        # phrases = Chainedword(**data)
        # return phrases

    def get_phrase_by_random(self,level):
        sql = """ SELECT * FROM chainedword WHERE level = :level ORDER BY RANDOM() LIMIT 2"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"level":level})

        data = cursor.fetchmany(2)
        result = []
        for item in data:
            phrase = Chainedword(**item)
            result.append(phrase)

        return result