import sqlite3
from unittest import result

class User:
    def __init__(self, id, name, password="NO-PASSWORD"):
        self.id = id
        self.name = name
        self.password = password       

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
        }

class UserRepository:
        def __init__(self, database_path):
            self.database_path = database_path
            self.init_tables()

        def create_conn(self):
            conn = sqlite3.connect(self.database_path)
            conn.row_factory = sqlite3.Row
            return conn

        def init_tables(self):
            sql = """
                CREATE TABLE if not exists users(
                    "id" varchar PRIMARY KEY,
                    "name" varchar,
                    "password" varchar
                )
            """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

        def get_all_users(self):
            sql = """select * from users"""
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql)

            data = cursor.fetchall()

            result = [User(**item) for item in data]
            return result
            
        def save(self, user):
            sql = """insert into users (id, name, password) values (:id, :name, :password
            ) """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute ( sql, {"id":user.id, "name":user.name, "password":user.password})
            conn.commit()           

        def get_user_by_id(self, id):
            sql = """SELECT * FROM users WHERE id=:id"""
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql, {"id":id})

            data = cursor.fetchone()
            if data is None:
                return None
            else:
                user = User(**data)
                
            return user

        