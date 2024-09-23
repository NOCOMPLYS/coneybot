import sqlite3 as sq

class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, nick) VALUES (?, ?)", (user_id, nickname,))
        
    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id,))
    
    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM users").fetchall()
    
    def get_admins(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM admins").fetchall()
    
    def get_name(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,)).fetchone()
    
    def get_age(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,)).fetchone()
        
    def set_waiting(self, user_id, waiting):
        with self.connection:
            return self.cursor.execute("UPDATE admins SET waiting = ? WHERE user_id = ?", (waiting, user_id,)) 

    def get_waiting(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT waiting FROM admins WHERE user_id = ?", (user_id,)).fetchone()


db = Database('database.db')
if db.connection:
    print('The data base has been successfully connected')
else:
    print('Failed to connect to data base')