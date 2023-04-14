import sqlite3

class DataInsertion:


    def __init__(self, id_number =-1, power="", total=""):
        self.id_number = id_number
        self.power = power
        self.total = total

        self.database = sqlite3.connect('data.db')
        self.cursor = self.database.cursor()


    def create_data(self):

        self.database.execute("""
        CREATE TABLE IF NOT EXISTS data (
        
        id INTEGER PRIMARY KEY, 
        power INTEGER,
        total INTEGER
        )
        """)



    def load_data(self, id_number):
        self.cursor.execute("""
            SELECT * FROM data
            WHERE id = {}
        """.format(id_number))

        result = self.cursor.fetchone()

        self.id_number = id_number
        self.power_data = result[1]
        self.total_power = result[2]


    def insert_data(self):

        self.cursor.execute("""
        INSERT INTO data VALUES
        ({}, {}, {})
        """.format(self.id_number, self.power, self.total))


        self.database.commit()
        

    def data_ending(self):

        self.database.commit()

        self.database.close()  
