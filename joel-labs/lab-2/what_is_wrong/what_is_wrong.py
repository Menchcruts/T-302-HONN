from dataclasses import asdict, dataclass
import json
from typing import List
from pathlib import Path


@dataclass
class Buyer:
    username: str
    allowed_products: List[str]


@dataclass
class Merchant:
    username: str
    name: str
    product: str


@dataclass
class Order:
    merchant_username: str
    buyer_username: str
    price: float
    product: str
    description: str


@dataclass
class OrderInfo:
    product: str
    price: float
    description: str


class ApplicationException(Exception):
    pass


class EntityNotFound(ApplicationException):
    def __init__(self, entity: str, id: str) -> None:
        super().__init__(f"{entity} entity with id {id} not found")


def create_order_old(username_1: str, username_2: str, product: str, order_price: float, order_description: str) -> None:
    file1 = open("merchants.json", "r")
    file2 = open("buyers.json", "r")
    data1 = json.load(file1)
    data2 = json.load(file2)

    try:
        merchant_json = next(
            (merchant for merchant in data1 if merchant["username"] == username_1))
    except StopIteration:
        raise EntityNotFound("merchant", username_1)

    merchant = Merchant(**merchant_json)

    try:
        buyer_json = next(
            buyer for buyer in data2 if buyer["username"] == username_2)
    except StopIteration:
        raise EntityNotFound("buyer", username_2)
    file1.close()
    file2.close()

    buyer = Buyer(**buyer_json)

    if product == merchant.product and product in buyer.allowed_products:
        order = Order(
            merchant_username=merchant.username,
            buyer_username=buyer.username,
            price=order_price,
            product=product,
            description=order_description)
        file = open("orders.json", "r")
        existing_orders_json = json.load(file)
        file.close()

        existing_orders_json.append(asdict(order))
        file = open("orders.json", "w")
        json.dump(existing_orders_json, file, indent=4, separators=(',', ': '))
        file.close()

    else:
        raise ApplicationException(
            f"Product {product} not allowed for buyer {username_2} and merchant {username_1}")


def create_buyer(username: str, allowed_products: List[str]) -> Buyer:
    return Buyer(username, allowed_products)

def create_merchant(username: str, name: str, product: str) -> Merchant:
    return Merchant(username, name, product)


def read_json_file(path: Path) -> List[dict]:
    path = Path(path)
    with path.open("r") as file:
        return json.load(file)
    return list()


def get_buyer(username: str) -> Buyer:
    data = read_json_file("buyers.json")
    try:
        buyer = next(user for user in data if user["username"] == username)
        return create_buyer(**buyer)
    except StopIteration:
        raise EntityNotFound("buyer", username)

def get_merchant(username: str) -> Buyer:
    data = read_json_file("merchants.json")
    try:
        merchant = next(user for user in data if user["username"] == username)
        return create_merchant(**merchant)
    except StopIteration:
        raise EntityNotFound("merchant", username)


def is_valid_product(product:str, merchant: Merchant, buyer: Buyer) -> bool:
    return product in buyer.allowed_products and merchant.product == product


def get_existing_orders() -> List[dict]:
    return read_json_file("orders.json")


def save_order(order: Order) -> None:
    orders = get_existing_orders()
    orders.append(asdict(order))
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=4, separators=(',', ': '))


def create_order(merchant_username: str, buyer_username: str, order_info: OrderInfo) -> None:
    """
    Create and save order to the database.
    Args:
        merchant_username (str): Username of the merchant
        buyer_username (str): Username of the buyer
        order_info (OrderInfo): Info about the order (product, price and description).
    Returns:
        None
    Raises:
        ApplicationException: If the product does not match the merchant or is not in the buyers allowed product. 
    """
    buyer = get_buyer(buyer_username)
    merchant = get_merchant(merchant_username)
    
    if is_valid_product(order_info.product, merchant, buyer):
        order = Order(
            merchant_username=merchant.username,
            buyer_username=buyer.username,
            price=order_info.price,
            product=order_info.product,
            description=order_info.description
        )
        save_order(order)
    else:
        raise ApplicationException(f"Product {order_info.product} not allowed for buyer {buyer.username} and merchant {merchant.username}")


if __name__ == '__main__':
    create_order("eggo", "Eleven", OrderInfo("Eggo", 12, "some description"))
