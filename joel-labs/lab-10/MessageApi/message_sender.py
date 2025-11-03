import os

import pika
from retry import retry


class MessageSender:
    def __init__(self) -> None:
        self.queue = "messages"
        self.conn = self.__get_connection()
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.queue)

    def send_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message
        )

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST")))