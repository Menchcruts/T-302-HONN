import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="hello")

# TODO: You need to implement the consumption logic and connection to RabbitMQ here.


def log_to_file(log_entry: str):
    with open('./log.log', 'a+') as log_file:
        log_file.write(log_entry + '\n')
        log_file.flush()


print('Waiting for logs....')
# TODO: consume logs here
