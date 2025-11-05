import pika, json
from app.config import settings

def publish_payment_event(order_id: int, product_id: int, result: str, data: dict):
    rk = settings.PAYMENT_SUCCESS_KEY if result == "success" else settings.PAYMENT_FAILURE_KEY
    connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
    ch = connection.channel()

    ch.exchange_declare(exchange=settings.PAYMENTS_EXCHANGE, exchange_type="topic", durable=True)

    payload = {"order_id": order_id, "product_id": product_id, "result": result, "data": data}

    ch.basic_publish(
        exchange=settings.PAYMENTS_EXCHANGE,
        routing_key=rk,
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2),  # make message persistent
    )
    print(f"Publishing event: {payload}", flush=True)
    connection.close()