import pika, json
from app.publisher import publish_payment_event
from app.luhn_validator import luhn_check
from app.database import SessionLocal
from app.models import Payment
from app.config import settings

def _process(body: bytes):
    data = json.loads(body)
    order_id = data["order_id"]
    card = data["credit_card"]
    valid = (
        luhn_check(card["card_number"])
        and 1 <= card["expiration_month"] <= 12
        and len(str(card["expiration_year"])) == 4
        and len(str(card["cvc"])) == 3
    )
    result = "success" if valid else "failure"

    db = SessionLocal()
    try:
        db.add(Payment(order_id=order_id, result=result))
        db.commit()
    finally:
        db.close()

    publish_payment_event(order_id, result)

def callback(ch, method, properties, body: bytes):
    print("Consumed event")
    print(body.decode())
    try:
        _process(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as exc:
        # NACK and requeue=false to avoid poison-loop; optionally DLX here
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def start_consumer():
    print("Starting consumer...")
    params = pika.URLParameters(settings.RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    ch = connection.channel()

    # 1) Make sure the inbound exchange exists
    ch.exchange_declare(exchange=settings.ORDERS_EXCHANGE, exchange_type="topic", durable=True)

    # 2) Declare a durable queue that all PaymentService replicas share
    #    (so they "take turns" within PaymentService)
    ch.queue_declare(queue=settings.PAYMENT_QUEUE, durable=True)

    # 3) Bind that queue to the exchange with the routing key you care about
    ch.queue_bind(
        exchange=settings.ORDERS_EXCHANGE,
        queue=settings.PAYMENT_QUEUE,
        routing_key=settings.ORDER_CREATED_ROUTING_KEY,
    )

    # (Nice to have) fair dispatch
    ch.basic_qos(prefetch_count=1)

    ch.basic_consume(queue=settings.PAYMENT_QUEUE, on_message_callback=callback)
    print(f"PaymentService waiting for {settings.ORDERS_EXCHANGE} events via exchange...")
    ch.start_consuming()
