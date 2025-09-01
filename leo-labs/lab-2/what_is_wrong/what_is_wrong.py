from dataclasses import asdict, dataclass
import json
from typing import List, Dict

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

class OrderData:
    price: float
    product: str
    description: str


class ApplicationException(Exception):
    pass


class EntityNotFound(ApplicationException):
    def __init__(self, entity: str, id: str) -> None:
        super().__init__(f"{entity} entity with id {id} not found")


def read_json_file(filename: str) -> List[Dict]:
    with open(filename, "r") as file:
        content = file.read().strip()
        if not content:
            return []
        return json.loads(content)

def get_merchant_data(merchant_username: str, filename: str) -> Merchant:
    merchants_json = read_json_file(filename) 
    try:
        merchant_data = next(
            (merchant for merchant in merchants_json if merchant["username"] == merchant_username))
        return Merchant(**merchant_data)
    
    except StopIteration:
        raise EntityNotFound("merchant", merchant_username)

def get_buyer_data(buyer_username: str, filename: str) -> Buyer:
    buyers_json = read_json_file(filename)
    try:
        buyer_data = next(
            (buyer for buyer in buyers_json if buyer["username"] == buyer_username))
        return Buyer(**buyer_data)
    except StopIteration:
        raise EntityNotFound("buyer", buyer_username)
    
def write_json_file(filename: str, data: List[Dict]) -> None:      
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, separators=(',', ': '))

def can_create_order(merchant: Merchant, buyer: Buyer, product: str) -> bool:
    return product == merchant.product and product in buyer.allowed_products

def save_order(merchant: Merchant, buyer: Buyer, order: Order) -> None:
    new_order = Order(
        merchant_username=merchant.username,
        buyer_username=buyer.username,
        price = order.price,
        product = order.product,
        description = order.description)
    orders_data = read_json_file("orders.json")
    orders_data.append(asdict(new_order))
    write_json_file("orders.json", orders_data)

def validate_order(merchant: Merchant, buyer: Buyer, order: Order) -> None:
    if not can_create_order(merchant, buyer, order.product):
        raise ApplicationException(
            f"Product {order.product} not allowed for buyer {buyer.username} and merchant {merchant.username}"
        )

def create_order(order: Order) -> None:
    merchant = get_merchant_data(order.merchant_username, "merchants.json")
    buyer = get_buyer_data(order.buyer_username, "buyers.json")
    validate_order(merchant, buyer, order)
    save_order(merchant, buyer, order)


if __name__ == '__main__':
    create_order(Order("eggo", "Eleven", 12, "Eggo", "some description"))