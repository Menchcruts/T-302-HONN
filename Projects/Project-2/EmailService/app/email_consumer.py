import json
import os
from typing import Any, Dict, Optional

import pika
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailEventConsumer:
    def __init__(self) -> None:
        params = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=int(os.getenv("RABBITMQ_PORT")),
        )


        self._order_exchange = os.getenv("ORDER_EVENTS_EXCHANGE")
        self._order_queue = os.getenv("EMAIL_EVENTS_QUEUE")
        self._order_routing_key = os.getenv("ORDER_CREATED_ROUTING_KEY")

        self._payments_exchange = os.getenv("PAYMENTS_EVENTS_EXCHANGE")
        self._payments_queue = os.getenv("PAYMENT_EVENTS_QUEUE")
        self._payment_success_routing_key = os.getenv("PAYMENT_SUCCESS_KEY")
        self._payment_failure_routing_key = os.getenv("PAYMENT_FAILURE_KEY")

        self._from_email = os.getenv("SENDGRID_SENDER_EMAIL")
        if not self._from_email:
            raise RuntimeError("SENDGRID_SENDER_EMAIL env variable is required for the email service.")

        api_key = os.getenv("SENDGRID_API_KEY")
        if not api_key:
            raise RuntimeError("SENDGRID_API_KEY env variable is required for the email service.")

        self._sendgrid = SendGridAPIClient(api_key)

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()

        self._channel.exchange_declare(exchange=self._order_exchange, exchange_type="topic", durable=True)
        self._channel.exchange_declare(exchange=self._payments_exchange, exchange_type="topic", durable=True)

        self._channel.queue_declare(queue=self._order_queue, durable=True)
        self._channel.queue_bind(
            exchange=self._order_exchange,
            queue=self._order_queue,
            routing_key=self._order_routing_key,
        )

        self._channel.queue_declare(queue=self._payments_queue, durable=True)
        self._channel.queue_bind(
            exchange=self._payments_exchange,
            queue=self._payments_queue,
            routing_key=self._payment_success_routing_key,
        )
        self._channel.queue_bind(
            exchange=self._payments_exchange,
            queue=self._payments_queue,
            routing_key=self._payment_failure_routing_key,
        )

    def start(self) -> None:
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(queue=self._order_queue, on_message_callback=self._handle_order_created)
        self._channel.basic_consume(queue=self._payments_queue, on_message_callback=self._handle_payment_event)
        print("EmailEventConsumer listening for order and payment events...", flush=True)
        self._channel.start_consuming()

    def _handle_order_created(self, channel, method, properties, body) -> None:
        payload = json.loads(body.decode())
        subject = "Order has been created"
        recipients = [
            {"name": payload.get("buyer_name"), "email": payload.get("buyer_email")},
            {"name": payload.get("merchant_name"), "email": payload.get("merchant_email")},
        ]

        success = True
        for recipient in recipients:
            html_content = self._build_order_created_email(payload, recipient.get("name"))
            if not self._send_email(recipient.get("email"), subject, html_content):
                success = False

        if success:
            channel.basic_ack(delivery_tag=method.delivery_tag)
        else:
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def _handle_payment_event(self, channel, method, properties, body) -> None:
        print("+-------------------- testing --------------------+", flush=True)
        payload = json.loads(body.decode())
        order_id = payload.get("order_id")
        routing_key = method.routing_key
        is_success = routing_key == self._payment_success_routing_key
        subject = "Order has been purchased" if is_success else "Order purchase failed"
        message = (
            f"Order {order_id} has been successfully purchased"
            if is_success
            else f"Order {order_id} purchase has failed"
        )

        recipients = [
            {
                "name": payload.get("buyer_name"),
                "email": payload.get("buyer_email"),
            },
            {
                "name": payload.get("merchant_name"),
                "email": payload.get("merchant_email"),
            },
        ]

        success = True
        for recipient in recipients:
            html_content = self._build_payment_email_html(message)
            if not self._send_email(recipient.get("email"), subject, html_content):
                success = False

        if success:
            channel.basic_ack(delivery_tag=method.delivery_tag)
        else:
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def _send_email(self, to_email:str, subject: str, html_content: str) -> bool:
        try:
            message = Mail(
                from_email=self._from_email,
                to_emails=to_email,
                subject=subject,
                html_content=html_content,
            )
            response = self._sendgrid.send(message)
            print(f"[EmailService] Sent '{subject}' to {to_email}")
            return True
        except Exception as e:
            print(f"[EmailService] Failed to send '{subject}' to {to_email}: {e}")
            print(f"[EmailService] Error details - From: {self._from_email}, To: {to_email}, Subject: {subject}")
            return False

    def _build_order_created_email(self, payload: Dict[str, Any], recipient_name: Optional[str]) -> str:
        greeting = recipient_name
        order_id = payload.get("order_id")
        product_name = payload.get("product_name")
        total_price = payload.get("total_price")
        total_price_str = f"{float(total_price):.2f}"
        pending_message = "Your order has been created and is currently pending confirmation."

        return (
            "<html>"
            "<body>"
            "<h2>Order has been created</h2>"
            f"<p>Hi {greeting},</p>"
            f"<p>{pending_message}</p>"
            f"<p><strong>Order ID:</strong> #{order_id}<br>"
            f"<strong>Product:</strong> {product_name}<br>"
            f"<strong>Total price:</strong> {total_price_str}</p>"
            "<p>We will send another email once the order status changes.</p>"
            "</body>"
            "</html>"
        )

    def _build_payment_email_html(self, message: str) -> str:
        return (
            "<html>"
            "<body>"
            f"<p>{message}</p>"
            "</body>"
            "</html>"
        )
