from client.infrastructure.settings.settings import Settings
from client.models.order import Order


class OrderRepository:
    def __init__(self, settings: Settings):
        self.__settings = settings

    def save(self, order: Order):
        with open(self.__settings.order_file_path, "a", encoding='utf-8') as file:
            file.write(order.description + "\n")
            file.flush()
