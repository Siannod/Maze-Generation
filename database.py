import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect("data\data.db") #creates connection to databse
        self.cursor = self.connection.cursor() #assigns connection to object
        self.time = ["df", "prim"]
        self.user = ""

    def new_user(self, name, passw): #creates a new user
        self.cursor.execute(f"""INSERT INTO login("user", "password") VALUES ("{name}", "{passw}")""")
        for entry in self.time: #creates entries in the time tables
            self.cursor.execute(f"""INSERT INTO {entry} VALUES ("{name}", 1000, 1000, 1000)""")
        self.cursor.execute(f"SELECT * FROM prim WHERE user = ?", (name,))
        self.user = name
        self.connection.commit()

    def check_user(self, name): #checks if the username is take
        self.cursor.execute(f"SELECT user FROM login WHERE user = ?", (name,))
        res = self.cursor.fetchall()
        if len(res) == 0:
            return False
        else:
            return True


    def check_login(self, name, passw): #confirms user and password correcr
        self.cursor.execute(f"SELECT password FROM login WHERE user = ?", (name, ))
        res = self.cursor.fetchall()
        if len(res) == 0:
            return False
        elif res[0][0] == passw:
            self.user = name
            return True
        else:
            return False

    def get_data(self, table): # gets highscores from given table
        self.cursor.execute(f"SELECT * FROM {table} ORDER BY time ASC")
        row = self.cursor.fetchall()[0:7]
        return row

    def write_time(self, time, maze):
        self.cursor.execute(f"SELECT * FROM {maze} WHERE user = ?", (self.user,)) # get users times for a maze
        self.times = self.cursor.fetchall()[0][1:]
        self.new = []
        for tim in self.times: #checks if new time is lower than current
            if tim < time:
                self.new.append(tim)
            else:
                self.new.append(time)
                self.new.append(tim)
                time = 1000
        self.cursor.execute(f"""UPDATE {maze} SET time_one = {self.new[0]}, time_two = {self.new[1]}, 
                             time_three = {self.new[2]} WHERE user = "{self.user}"; """)
        self.connection.commit()

  
    def close(self): #closes the database connection
        self.connection.commit()
        self.connection.close()
