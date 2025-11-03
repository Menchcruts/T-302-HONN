import os

import pika
from retry import retry


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST")))


def callback(ch, method, properties, body: bytes):
    print(body.decode(encoding="utf-8"), flush=True)


def main():
    queue = "messages"
    conn = get_connection()
    channel = conn.channel()
    channel.queue_declare(queue=queue)
    
    channel.basic_consume(
        queue=queue,
        auto_ack=True,
        on_message_callback=callback
    )

    channel.start_consuming()

if __name__ == '__main__':
    main()