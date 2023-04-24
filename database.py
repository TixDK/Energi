import sqlite3



class DataCollector:
    
    
    def __init__(self):
        self.database = sqlite3.connect('Data.db')
        
    def create_database(self):
        
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id integer primary key autoincrement, 
                pwower INTEGER, 
                total INTEGER,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                
            )                      
                                            
        """)
        
    def load_data(self, timer_tween, time_end):
        
        cursor = self.database.cursor()
        
        cursor.execute("""
            SELECT * FROM data
            WHERE DATETIME(t) BETWEEN ? AND ?               
        """, (timer_tween, time_end))
        
        result = cursor.fetchall()
        return result
    
    
    def insert_data(self, total, power):
        cursor = self.database.cursor()
        
        cursor.execute("""
            INSERT INTO data(power, total)
            VALUES(?,?)               
                       
        """, (power, total))
        
        self.database.commit()
    
    
    def data_closer(self):
        self.database.commit()
               
        self.database.close()
        
    
        
