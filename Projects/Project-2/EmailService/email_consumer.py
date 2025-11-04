import json
import os

import pika
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Any, Dict

class EmailEventConsumer:
    def __init__(self) -> None:
        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
            port=int(os.getenv("RABBITMQ_PORT", 5672)),
        )

        self._exchange = os.getenv("ORDER_EVENTS_EXCHANGE")
        self._queue = os.getenv("EMAIL_EVENTS_QUEUE")
        self._routing_key = os.getenv("ORDER_CREATED_ROUTING_KEY", "order.created")
        self._from_email = os.getenv("EMAIL_FROM_ADDRESS", "no-reply@example.com")
        api_key = os.getenv("SENDGRID_API_KEY")
        if not api_key:
            raise RuntimeError("SENDGRID_API_KEY env variable is required for the email service.")
        self._sendgrid = SendGridAPIClient(api_key)

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
        print(f"Received order event payload:\n{json.dumps(payload, indent=2)}")

        recipients = [
            {"name": payload.get("buyer_name"), "email": payload.get("buyer_email")},
            {"name": payload.get("merchant_name"), "email": payload.get("merchant_email")},
        ]

        for recipient in recipients:
            email = recipient.get("email")
            if not email:
                continue
            message = Mail(
                from_email=self._from_email,
                to_emails=email,
                subject="Order has been created",
                html_content=self._build_email_html(payload, recipient.get("name")),
            )
            self._sendgrid.send(message)

        channel.basic_ack(delivery_tag=method.delivery_tag)

    def _build_email_html(self, payload: Dict[str, Any], recipient_name: str) -> str:
        name = recipient_name
        order_id = payload.get("order_id", "N/A")
        product_name = payload.get("product_name", "your product")
        total_price = payload.get("total_price")
        total_price_str = f"{float(total_price):.2f}" if total_price is not None else "N/A"
        pending_message = "Your order has been created and is currently pending confirmation."

        return (
            "<html>"
            "<body>"
            f"<h2>Order has been created</h2>"
            f"<p>Hi {name},</p>"
            f"<p>{pending_message}</p>"
            f"<p><strong>Order ID:</strong> #{order_id}<br>"
            f"<strong>Product:</strong> {product_name}<br>"
            f"<strong>Total price:</strong> {total_price_str}<br>"
            "<p>We will send another email once the order status changes.</p>"
            "</body>"
            "</html>"
        )

def main() -> None:
    consumer = EmailEventConsumer()
    consumer.start()


if __name__ == "__main__":
    main()
