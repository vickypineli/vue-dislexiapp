import sqlite3

class Activity:
    def __init__ (self, id, user_id, name):
        self.id = id
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name
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
                "id" PRIMARY KEY,
                "user_id" varchar,
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

    # def save(self, activity):
    #     sql = """insert into activities (id, name) values (:id, :name
    #     ) """
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         sql,
    #         activity.to_dict()
    #     )
    #     conn.commit()

    def search_by_user_id(self, user_id):
        sql = """select * from activities where id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchall()

        activities = []
        for item in data:
            activity = Activity(**item)
            activities.append(activity)

        return activities

    
    

     
 
