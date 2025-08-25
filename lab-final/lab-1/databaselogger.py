import psycopg2
from dotenv import load_dotenv
import os
from logger import Logger

#2.4 Bonus Database logger (20 points)

#1. (Total points: 20) Implement the concrete class DatabaseLogger
#• The class should be in a file named databaselogger.py
#• DatabaseLogger implements the Logger interface
#• log_info, log_warning and log_error log to a PostgreSQL database
#• The database should have one log table


class DatabaseLogger(Logger):  
    def __init__(self):
        load_dotenv() 

        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")

        self.conn = psycopg2.connect(
            dbname=DB_NAME,    
            user=DB_USER,        
            password=DB_PASSWORD,  
            host=DB_HOST,       
            port=DB_PORT             
        )
            
        self.cur = self.conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS log (
            id SERIAL PRIMARY KEY,
            eventLevel VARCHAR NOT NULL,
            message VARCHAR NOT NULL,
            exception VARCHAR
        )
        """
        self.cur.execute(create_table_query)
        self.conn.commit()

        
    def log_error(self, message: str, exception: Exception) -> None:
        insert_query = "INSERT INTO log (eventLevel, message, exception) VALUES (%s, %s, %s)"
        self.cur.execute(insert_query,("Error", message, str(exception)))
        self.conn.commit()

    def log_info(self, message: str) -> None:
        insert_query = "INSERT INTO log (eventLevel, message) VALUES (%s, %s)"
        self.cur.execute(insert_query,("Info", str(message)))
        self.conn.commit()
    
    def log_warning(self, message: str) -> None:
        insert_query = "INSERT INTO log (eventLevel, message) VALUES (%s, %s)"
        self.cur.execute(insert_query,("Warning", str(message)))
        self.conn.commit()

    def __del__(self):
        self.__close()

    def __close(self) -> None:
        self.cur.close()
        self.conn.close()
