import json
import os

import pika


class OrderEventPublisher:
    def __init__(self) -> None:
        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=int(os.getenv("RABBITMQ_PORT")),
        )
        self._exchange = os.getenv("ORDER_EVENTS_EXCHANGE")
        self._routing_key = os.getenv("ORDER_CREATED_ROUTING_KEY")

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type="topic", durable=True)

    def _ensure_connection(self) -> None:
        if self._connection.is_closed or self._channel.is_closed:
            params = pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_HOST"),
                port=int(os.getenv("RABBITMQ_PORT")),
            )
            self._connection = pika.BlockingConnection(params)
            self._channel = self._connection.channel()
            self._channel.exchange_declare(exchange=self._exchange, exchange_type="topic", durable=True)

    def publish(self, payload: dict) -> None:
        self._ensure_connection()
        body = json.dumps(payload).encode()
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=body,
            properties=pika.BasicProperties(content_type="application/json", delivery_mode=2),
        )
