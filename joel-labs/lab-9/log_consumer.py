import pika

def log_to_file(log_entry: str):
    with open('./log.log', 'a+') as log_file:
        log_file.write(log_entry + '\n')
        log_file.flush()

def callback(ch, method, properties, body: bytes):
    log_to_file(body.decode())

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="lab-9")

    channel.basic_consume(
        queue="lab-9",
        auto_ack=True,
        on_message_callback=callback
    )

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
