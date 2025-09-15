from Validation import Validation
from models.Order import Order, OrderStatus

class OrderIsUnpaidValidation(Validation):
    def __init__(self, order: Order):
        super().__init__()
        self.order = order

    def validate(self):
        return self.order.status == OrderStatus.Unpaid
