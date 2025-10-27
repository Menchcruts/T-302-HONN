import string
import time
import random

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="lab-9")


def random_log() -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def main():
    while True:
        log_entry = random_log()
        print(f'Publishing log: {log_entry}')
        channel.basic_publish(
            exchange='',
            routing_key="lab-9",
            body=log_entry
        )
        time.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        connection.close()