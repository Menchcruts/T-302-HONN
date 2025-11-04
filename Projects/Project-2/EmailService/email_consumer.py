import json
import os

import pika

from email_inputmodel import EmailMessageDTO


class EmailEventConsumer:
    def __init__(self) -> None:
        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
            port=int(os.getenv("RABBITMQ_PORT", 5672)),
            credentials=pika.PlainCredentials(
                os.getenv("RABBITMQ_USER", "guest"),
                os.getenv("RABBITMQ_PASS", "guest"),
            ),
        )

        self._exchange = os.getenv("ORDER_EVENTS_EXCHANGE", "orders.events")
        self._queue = os.getenv("EMAIL_EVENTS_QUEUE", "email.order.created")
        self._routing_key = os.getenv("ORDER_CREATED_ROUTING_KEY", "order.created")

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type="topic", durable=True)
        self._channel.queue_declare(queue=self._queue, durable=True)
        self._channel.queue_bind(exchange=self._exchange, queue=self._queue, routing_key=self._routing_key)

    def start(self) -> None:
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(queue=self._queue, on_message_callback=self._handle_message)
        self._channel.start_consuming()

    def _handle_message(self, channel, method, properties, body) -> None:
        payload = json.loads(body.decode())

        email_dto = EmailMessageDTO(
            to_emails=payload["buyer"]["emails"],
            template_id="order-confirmation",
            dynamic_data={"order": payload["order"]},
        )

        # TODO: send email using SendGrid

        channel.basic_ack(delivery_tag=method.delivery_tag)


def main() -> None:
    consumer = EmailEventConsumer()
    consumer.start()


if __name__ == "__main__":
    main()
