from app.email_consumer import EmailEventConsumer


def create_consumer() -> EmailEventConsumer:
    return EmailEventConsumer()


consumer = create_consumer()


def main() -> None:
    consumer.start()


if __name__ == "__main__":
    main()
