import os
import psycopg2
from models.input.order import Order
from models.dtos.order import Order as OrderDTO


class OrderRepository:
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

        self.orders_table = "orders"
        self.credit_cards_table = "credit_cards"

        create_credit_cards_table = f"""
        CREATE TABLE IF NOT EXISTS {self.credit_cards_table} (
            id SERIAL PRIMARY KEY,
            card_number VARCHAR NOT NULL,
            expiration_month INTEGER NOT NULL,
            expiration_year INTEGER NOT NULL,
            cvc INTEGER NOT NULL
        )
        """

        create_orders_table = f"""
        CREATE TABLE IF NOT EXISTS {self.orders_table} (
            id SERIAL PRIMARY KEY,
            product_id INTEGER NOT NULL,
            merchant_id INTEGER NOT NULL,
            buyer_id INTEGER NOT NULL,
            credit_card_id INTEGER REFERENCES {self.credit_cards_table}(id),
            discount FLOAT NOT NULL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.cur.execute(create_credit_cards_table)
        self.cur.execute(create_orders_table)
        self.conn.commit()


    def save_order(self, order: Order) -> int:
        credit_card_insert = f"""
        INSERT INTO {self.credit_cards_table} 
        (card_number, expiration_month, expiration_year, cvc) 
        VALUES (%s, %s, %s, %s) RETURNING id
        """
        self.cur.execute(credit_card_insert, (
            order.creditCard.cardNumber,
            order.creditCard.expirationMonth,
            order.creditCard.expirationYear,
            order.creditCard.cvc
        ))
        credit_card_id = self.cur.fetchone()[0]

        order_insert = f"""
        INSERT INTO {self.orders_table} 
        (product_id, merchant_id, buyer_id, credit_card_id, discount) 
        VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        self.cur.execute(order_insert, (
            order.productId,
            order.merchantId,
            order.buyerId,
            credit_card_id,
            order.discount
        ))
        order_id = self.cur.fetchone()[0]
        self.conn.commit()
        return order_id


    def get_order(self, id: int) -> OrderDTO:
        select_query = f"""
        SELECT o.product_id, o.merchant_id, o.buyer_id, 
               cc.card_number, o.discount
        FROM {self.orders_table} o
        JOIN {self.credit_cards_table} cc ON o.credit_card_id = cc.id
        WHERE o.id = %s
        """
        self.cur.execute(select_query, (id,))
        result = self.cur.fetchone()
        
        if result:
            product_id, merchant_id, buyer_id, card_number, discount = result
            total_price = discount  
            return OrderDTO(
                productId=product_id,
                merchantId=merchant_id,
                buyerId=buyer_id,
                cardNumber=card_number,
                totalPrice=total_price
            )
        return None
