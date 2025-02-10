import  psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname = "sample",
                                     user = "postgres",
                                     password = "0000",
                                     host = "localhost",
                                     port = "5432"
                                     )
        self.cursor = self.conn.cursor()


    def add_user(self, username, password):

        try:
            self.cursor.execute("""INSERT INTO users (username, password) VALUES (%s, %s)""", (username, password))
            self.conn.commit()

            return True
        except psycopg2.IntegrityError:
            self.conn.rollback()

            return False


    def login(self, username, password):
        self.cursor.execute("SELECT username, password FROM users WHERE username = %s AND password =%s",(username,password))
        user = self.cursor.fetchone()
        return user is not None


    def update_password(self, username, password):
        try:
            self.cursor.execute("UPDATE users SET password = %s WHERE username = %s", (password, username))
            self.conn.commit()

            return True
        except psycopg2.IntegrityError:
            self.conn.rollback()

            return False
