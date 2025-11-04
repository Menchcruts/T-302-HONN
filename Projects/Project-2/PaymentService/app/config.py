import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL")

    # Inbound (from OrderService)
    ORDERS_EXCHANGE: str = os.getenv("ORDER_EVENTS_EXCHANGE", "orders.event")
    ORDER_CREATED_ROUTING_KEY: str = os.getenv("ORDER_CREATED_ROUTING_KEY", "order.created")
    PAYMENT_QUEUE: str = os.getenv("PAYMENT_QUEUE", "orders.order.created.payment")
    
    # Outbound (to others)
    PAYMENTS_EXCHANGE: str = os.getenv("PAYMENTS_EXCHANGE", "payments.events")
    PAYMENT_SUCCESS_KEY: str = os.getenv("PAYMENT_SUCCESS_KEY", "payment.success")
    PAYMENT_FAILURE_KEY: str = os.getenv("PAYMENT_FAILURE_KEY", "payment.failure")

settings = Settings()