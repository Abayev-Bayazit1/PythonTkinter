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
