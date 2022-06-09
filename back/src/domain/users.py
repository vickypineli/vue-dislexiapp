import sqlite3

class User:
    def __init__(self, user_id, name, password="NO-PASSWORD"):
        self.user_id = user_id
        self.name = name
        self.password = password       

    def to_dict(self,):
        return {
            "id": self.user_id,
            "name": self.name
            
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

        def get_users(self):
            sql = """select * from users"""
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql)

            data = cursor.fetchall()

            users = [User(**item) for item in data]
            return users

        def save(self, user):
            sql = """insert into users (user_id, name, password) values (:user_id, :name :password
            ) """
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(
                sql, 
                 {"user_id" :user.id, "name" :user.name, "password" :user.password}
                )
            conn.commit()

        def get_user_by_id(self, id):
            sql = """SELECT * FROM users WHERE user_id = :user_id"""
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql, {"user_id" :user.id})

            data = cursor.fetchone()
            if data is None:
                return None
            else:
                user = User(**data)
                
            return user
            