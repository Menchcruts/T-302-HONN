import json
import os

import pika


class OrderEventPublisher:
    def __init__(self) -> None:
        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
            port=int(os.getenv("RABBITMQ_PORT", 5672)),
        )
        self._exchange = os.getenv("ORDER_EVENTS_EXCHANGE", "orders.events")
        self._routing_key = os.getenv("ORDER_CREATED_ROUTING_KEY", "order.created")

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type="topic", durable=True)

    def publish(self, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=body,
            properties=pika.BasicProperties(content_type="application/json", delivery_mode=2),
        )
