import sqlite3
from sys import path

class Activity:
    def __init__ (self, id, user_id, route, name):
        self.id = id
        self.user_id = user_id
        self.route = route
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "path": self.route,
            "name": self.name,
        }

class ActivityRepository:
    def __init__ (self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists activities  (
                "id" varchar PRIMARY KEY,
                "user_id" varchar,
                "route" varchar,
                "name" varchar
            )  
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from activities"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        
        result = []
        for item in data:
            activity = Activity(**item)
            result.append(activity)
        return result

    def save(self, activity):
        sql = """insert into activities (id, user_id, route, name) values (:id, :user_id, :route, :name
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute ( 
                        sql, 
                        {"id":activity.id, "user_id":activity.user_id, "route":activity.route, "name":activity.name}
                        )
        conn.commit()
        
    def get_activity_by_id(self, id):
        sql = """SELECT * FROM activities WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is not None:
            activity = None
        else:
            activity = Activity(**data)
            
        return activity

    def search_activities_by_user_id(self, user_id):
        sql = """select * from activities where user_id=:user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id":user_id})

        data = cursor.fetchall()

        result = []
        for item in data:
            activity = Activity(**item)
            result.append(activity)

        return result



    

     
 
