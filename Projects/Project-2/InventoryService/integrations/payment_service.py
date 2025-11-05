import os
import json

import pika
from pika.exchange_type import ExchangeType

from app.product_repo import ProductRepository

class PaymentEventConsumer:
    def __init__(self, product_repo: ProductRepository):
        self._product_repo = product_repo

        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=os.getenv("RABBITMQ_PORT"),
            credentials=pika.PlainCredentials(
                username=os.getenv("RABBITMQ_USER"),
                password=os.getenv("RABBITMQ_PASS")
            )
        )

        self._exchange = os.getenv("PAYMENT_EVENTS_EXCHANGE", "payments.events")
        self._queue = os.getenv("INVENTORY_EVENTS_QUEUE", "inventory.payments.events")
        self._routing_key_success = os.getenv("PAYMENTS_SUCCESS_KEY", "payments.success")
        self._routing_key_failed = os.getenv("PAYMENTS_FAILED_KEY", "payments.failed")

        self._connection = pika.BlockingConnection(parameters=params)
        
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type=ExchangeType.topic, durable=True)
        
        self._channel.queue_declare(queue=self._queue, durable=True)
        self._channel.queue_bind(exchange=self._exchange, queue=self._queue, routing_key=self._routing_key_success)
        self._channel.queue_bind(exchange=self._exchange, queue=self._queue, routing_key=self._routing_key_failed)


    def _handle_message(self, channel, method, properties, body: bytes) -> None:
        print("Consumed event...", flush=True)
        payload: dict = json.loads(body)
        print(payload, flush=True)

        product_id = payload.get("product_id")
        result = payload.get("result")
        success = result == "success"
        
        if not product_id:
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

        if success:
            self._product_repo.lower_quantity(product_id)
        self._product_repo.unreserve_product(product_id)

        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start(self) -> None:
        print("InventoryService started consuming...", flush=True)
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(queue=self._queue, on_message_callback=self._handle_message)
        self._channel.start_consuming()

def main():
    print("Consuming thread started...", flush=True)
    consumer = PaymentEventConsumer(ProductRepository())
    consumer.start()

if __name__ == "__main__":
    main()
