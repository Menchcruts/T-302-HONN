import os
import psycopg2


class MessageRepository:
    def __init__(self):

        DB_NAME = os.getenv("POSTGRES_DB")
        DB_USER = os.getenv("POSTGRES_USER")
        DB_PASS = os.getenv("POSTGRES_PASSWORD")
        DB_HOST = os.getenv("POSTGRES_HOST")
        DB_PORT = os.getenv("POSTGRES_PORT")

        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )

        self.cur = self.conn.cursor()

        self.table_name = "messages"

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id SERIAL PRIMARY KEY,
            message VARCHAR NOT NULL,
        )
        """
        self.cur.execute(create_table_query)
        self.conn.commit()


    def save_message(self, message) -> int:
        insert_query = f"INSERT INTO {self.table_name} (message) VALUES ('{message}') RETURNING id"
        self.cur.execute(insert_query)
        _id = self.cur.fetchone()
        self.conn.commit()
        return _id[0]
        

    def get_message(self, id: int) -> str:
        select_query = f"SELECT FROM {self.table_name} message WHERE id={id}"
        self.cur.execute(select_query)
        msg = self.cur.fetchone()
        return msg[0]
