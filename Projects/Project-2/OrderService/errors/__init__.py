class OrderServiceError(Exception):
    """Base class for order service related errors."""

    default_message = "Order service error"

    def __init__(self, message=None):
        super().__init__(self.default_message if message is None else message)


class MerchantNotFoundError(OrderServiceError):
    default_message = "Merchant does not exist"


class BuyerNotFoundError(OrderServiceError):
    default_message = "Buyer does not exist"

class ProductNotFoundError(OrderServiceError):
    default_message = "Product does not exist"

class DiscountNotAllowedError(OrderServiceError):
    default_message = "Merchant does not allow discount"


class ExternalServiceCommunicationError(OrderServiceError):
    default_message = "Failed to communicate with service"