import os

import psycopg2
import psycopg2.extras

from .buyer_dto import BuyerDTO

class BuyerRepository:
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
        self.dict_cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        self.table_name = "buyers"

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            ssn VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            phone_number VARCHAR NOT NULL
        )
        """
        self.cur.execute(create_table_query)
        self.conn.commit()

    def save_buyer(self, buyer) -> int:
        insert_query = f"""
        INSERT INTO {self.table_name} 
        (name, ssn, email, phone_number) 
        VALUES (%s, %s, %s, %s) 
        RETURNING id
        """
        self.cur.execute(
            insert_query,
            (buyer.name, buyer.ssn, buyer.email, buyer.phone_number)
        )
        _id = self.cur.fetchone()
        self.conn.commit()
        return _id[0]

    def get_buyer(self, id: int):
        select_query = f"""
        SELECT *
        FROM {self.table_name} 
        WHERE id = %s
        """
        self.dict_cur.execute(select_query, (id,))
        result = self.dict_cur.fetchone()
        if not result:
            return None
        buyer_data = dict(result)
        buyer_data.pop("id", None)
        result = BuyerDTO(**buyer_data)
        return result
