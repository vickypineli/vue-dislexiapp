import sqlite3

class Chainedword:
    def __init__(self, id, level, img, question, answer):
        self.id = id
        self.level = level
        self.img = img
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'img':self.img,
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
                "img" varchar,
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
            sql = """insert into chainedword (id, level, img, question, answer) 
                        values (:id, :level, :img, :question, :answer 
                        ) """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(
                sql, 
                chainedword.to_dict()
                )
            conn.commit()
    
    # def get_list_of_phrases_by_level(self, level):
    #     sql = """ SELECT * FROM chainedword WHERE level = :level"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql,{"level":level})

    #     data = cursor.fetchall()

    #     result = []
    #     for item in data:
    #         chainedword = Chainedword(**item)
    #         result.append(chainedword)

    #     return result

    def get_phrase_one_by_one(self, level):
        sql = """ SELECT * FROM chainedword WHERE level=:level ORDER BY RANDOM() LIMIT 1"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql,{"level":level})

        data = cursor.fetchmany(1)
        result = []
        for item in data:
            phrase = Chainedword(**item)
            result.append(phrase)

        return result