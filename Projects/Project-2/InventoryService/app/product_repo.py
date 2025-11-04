import os

import psycopg2
import psycopg2.extras

from app.product import Product
from app.create_product_dto import CreateProductDto

class ProductRepository:
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

        self.table_name = "inventory"

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id SERIAL PRIMARY KEY,
            merchant_id INTEGER NOT NULL,
            product_name VARCHAR NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            reserved INTEGER DEFAULT 0
        )
        """
        self.cur.execute(create_table_query)
        self.conn.commit()
    
    def save_product(self, product: CreateProductDto) -> int:
        insert_query = f"""
        INSERT INTO {self.table_name}
        (merchant_id, product_name, price, quantity)
        VALUES ({product.merchant_id}, '{product.product_name}', {product.price}, {product.quantity})
        RETURNING id
        """
        self.dict_cur.execute(insert_query)
        res = self.dict_cur.fetchone()
        self.conn.commit()
        return res["id"]
    
    def get_product(self, id: int) -> Product | None:
        select_query = f"SELECT * FROM {self.table_name} WHERE id = {id}"
        self.dict_cur.execute(select_query)
        result = self.dict_cur.fetchone()
        if result:
            result = dict(result)
            result.pop("id")
            return Product(**result)
        return None
    
    def reserve_product(self, id: int) -> None:
        update_query = f"""
        UPDATE {self.table_name}
        SET reserved = reserved + 1
        WHERE id = {id}
        """
        self.cur.execute(update_query)
        self.conn.commit()

    def unreserve_product(self, id: int) -> None:
        update_query = f"""
        UPDATE {self.table_name}
        SET reserved = reserved - 1
        WHERE id = {id}
        """
        self.cur.execute(update_query)
        self.conn.commit()

    def lower_quantity(self, id: int) -> None:
        update_query = f"""
        UPDATE {self.table_name}
        SET quantity = quantity - 1
        WHERE id = {id}
        """
        self.cur.execute(update_query)
        self.conn.commit()
    
    def __del__(self) -> None:
        print("Closing connection")
        self.conn.close()